from django.shortcuts import render_to_response

from urllib import quote_plus
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Blog
from blog.form import BlogForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from django.shortcuts import render
from django.template import loader
from django.contrib import auth
from .models import Registration
from .models import Student
from .models import Parent
from .models import Staff
from .models import Staff_Position
from .models import Grade
from .models import Subject
from .models import Salarie
from .models import Payment
from .models import Payroll
from .models import UserLog
from .models import AcademicYear
from .models import StudentMark
from .models import ClassSchedule
from .models import StudentAttendance


@csrf_protect
def profile(request):
    return HttpResponseRedirect('/admin/')


def index(request):
    template = loader.get_template('index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def home(request):
    template = loader.get_template('home.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def notification(request):
    template = loader.get_template('notification.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def schooldetails(request):
    template = loader.get_template('schooldetails.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def studentprofile(request):
    template = loader.get_template('profile.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def login(request):
    c = {}
    # c.update(csrf_protect(request))
    return render(request, 'profile.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_superuser:
        auth.login(request, user)
        return HttpResponseRedirect('/students/')

    elif user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/studentloggedin/')
    else:
        return HttpResponseRedirect('/home/')


def studentloggedin(request):
    username = request.user.username
    student = Student.objects.get(users=request.user)
    try:
        parent = Parent.objects.get(student=student)
    except Parent.DoesNotExist:
        parent = None
    try:
        payment = Payment.objects.filter(student=student)
    except Payment.DoesNotExist:
        payment = None
    try:
        academicyear = AcademicYear.objects.get(student=student)
    except AcademicYear.DoesNotExist:
        academicyear = None
    try:
        studentmark = StudentMark.objects.filter(student=student)
    except StudentMark.DoesNotExist:
        studentmark = None
    try:
        studentattendance = StudentAttendance.objects.filter(student=student).order_by('-day')
    except StudentAttendance.DoesNotExist:
        studentattendance = None
    try:
        gradedetails = Grade.objects.get(student=student)
    except Grade.DoesNotExist:
        gradedetails = None
    # alluser = UserLog.objects.get(user=request.user),
    context = {
        'username': username,
        'student': student,
        'parent': parent,
        'payment': payment,
        'academicyear': academicyear,
        'studentmark': studentmark,
        'studentattendance': studentattendance,
        'gradedetails': gradedetails,
    }
    return render(request, "studentloggedin.html", context)


def blog(request):
    queryset_list = Blog.objects.all()  # .order_by("-record_added")
    paginator = Paginator(queryset_list, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "blog": queryset,
        "title": "Blog Posts"
    }
    return render(request, "blog.html", context)


def blog_detail(request, slug=None):
    instance = get_object_or_404(Blog, slug=slug)
    share_string = quote_plus(instance.title)
    context = {
        "title": instance.title,
        "instance": instance,
        "share_string": share_string
    }
    return render(request, "blog_detail.html", context)


def administration(request):
    template = loader.get_template('administration.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def students(request):
    student_list = Student.objects.all()
    query = request.GET.get("q")
    if query:
        student_list = student_list.filter(
                                          Q(studentID__icontains=query) |
                                          Q(level__icontains=query) |
                                          Q(enrollment_status__icontains=query)
                                           )
    paginator = Paginator(student_list, 25)

    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    context = {
        "students": students,
        "title": "Students"
    }

    return render(request, "students.html", context)


def studentdetails(request, id):
    try:
        instance = Student.objects.get(id=id)
        registration = Registration.objects.get(id=id)
        gradedetails = Grade.objects.get(id=id)
    except Student.DoesNotExist:
        instance = None
    except Registration.DoesNotExist:
        registration = None
    except Grade.DoesNotExist:
        gradedetails = None
    try:
        parent = Parent.objects.get(id=id)
    except Parent.DoesNotExist:
        parent = None
    try:
        payment = Payment.objects.filter(student=instance)
    except Payment.DoesNotExist:
        payment = None
    try:
        academicyear = AcademicYear.objects.get(student=instance)
    except AcademicYear.DoesNotExist:
        academicyear = None
    try:
        studentmark = StudentMark.objects.filter(student=instance)
    except StudentMark.DoesNotExist:
        studentmark = None
    try:
        studentattendance = StudentAttendance.objects.filter(student=instance).order_by('-day')
    except StudentAttendance.DoesNotExist:
        studentattendance = None
    context = {
        "instance": instance,
        "registration": registration,
        "gradedetails": gradedetails,
        "parent": parent,
        "payment": payment,
        "academicyear": academicyear,
        "studentmark": studentmark,
        "studentattendance": studentattendance,
    }
    return render(request, "studentdetails.html", context)


def staff(request):
    staff_list = Staff.objects.all()
    query = request.GET.get("q")
    if query:
        staff_list = staff_list.filter(
                                          Q(staffID__icontains=query) |
                                          Q(firstName__icontains=query) |
                                          Q(middleName__icontains=query) |
                                          Q(lastName__icontains=query) |
                                          Q(qualification__icontains=query)
                                           )
    paginator = Paginator(staff_list, 25)

    page = request.GET.get('page')
    try:
        staffs = paginator.page(page)
    except PageNotAnInteger:
        staffs = paginator.page(1)
    except EmptyPage:
        staffs = paginator.page(paginator.num_pages)

    context = {
        "staffs": staffs,
        "title": "Staffs"
    }

    return render(request, "staff.html", context)


def staffdetails(request, id):
    try:
        staff = Staff.objects.get(id=id)
        staff_position = Staff_Position.objects.get(id=id)
        grade = Grade.objects.get(id=id)
    except Staff.DoesNotExist:
        staff = None
    except Staff_Position.DoesNotExist:
        staff_position = None
    except Grade.DoesNotExist:
        grade = None
    try:
        subject = Subject.objects.filter(staff=staff)
    except Parent.DoesNotExist:
        subject = None
    try:
        salary = Salarie.objects.get(id=id)
    except Salarie.DoesNotExist:
        salary = None
    try:
        payroll = Payroll.objects.filter(staff=staff)
    except Payroll.DoesNotExist:
        payroll = None
    try:
        class_schedule = ClassSchedule.objects.filter(staff=staff)
    except ClassSchedule.DoesNotExist:
        class_schedule = None
    context = {
        "staff": staff,
        "staff_position": staff_position,
        "grade": grade,
        "subject": subject,
        "salary": salary,
        "payroll": payroll,
        "class_schedule": class_schedule,
    }
    return render(request, "staffdetails.html", context)


def payroll(request):
    payroll_list = Payroll.objects.all()
    query = request.GET.get("q")
    if query:
        payroll_list = payroll_list.filter(
                                          Q(accountnumber__icontains=query) |
                                          Q(contractperiod__icontains=query)
                                           )
    paginator = Paginator(payroll_list, 25)

    page = request.GET.get('page')
    try:
        payrolls = paginator.page(page)
    except PageNotAnInteger:
        payrolls = paginator.page(1)
    except EmptyPage:
        payrolls = paginator.page(paginator.num_pages)

    context = {
        "payrolls": payrolls,
        "title": "Payroll"
    }

    return render(request, "payroll.html", context)


def payrolldetails(request, id):
    template = loader.get_template('payrolldetails.html')
    context = {
        'staff': Staff.objects.get(id=id),
        'staff_position': Staff_Position.objects.get(id=id),
        'grade': Grade.objects.get(id=id),
        'subject': Subject.objects.get(id=id),
        'payroll': Payroll.objects.get(id=id),
        'class_schedule': ClassSchedule.objects.get(id=id)
    }
    return HttpResponse(template.render(context, request))


def schedule(request):
    schedule_list = ClassSchedule.objects.all()
    query = request.GET.get("q")
    if query:
        schedule_list = schedule_list.filter(
                                          Q(day__icontains=query) |
                                          Q(classTime__icontains=query)
                                           )
    paginator = Paginator(schedule_list, 25)

    page = request.GET.get('page')
    try:
        schedules = paginator.page(page)
    except PageNotAnInteger:
        schedules = paginator.page(1)
    except EmptyPage:
        schedules = paginator.page(paginator.num_pages)

    context = {
        "schedules": schedules,
        "title": "Schedule"
    }

    return render(request, "schedule.html", context)


def scheduledetails(request, id):
    template = loader.get_template('scheduledetails.html')
    context = {
        'staff': Staff.objects.get(id=id),
        'staff_position': Staff_Position.objects.get(id=id),
        'grade': Grade.objects.get(id=id),
        'subject': Subject.objects.get(id=id),
        'payroll': Payroll.objects.get(id=id),
        'class_schedule': ClassSchedule.objects.get(id=id)
    }
    return HttpResponse(template.render(context, request))
