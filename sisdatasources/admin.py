from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import Registration
from .models import Student
from .models import Parent
from .models import Staff
from .models import Staff_Position
from .models import Grade
from .models import Fee
from .models import Subject
from .models import Payment
from .models import Salarie
from .models import Payroll
from .models import AcademicYear
from .models import StudentMark
from .models import ClassSchedule
from .models import StudentAttendance
from .models import UserLog


class RegistrationModelAdmin(admin.ModelAdmin):
    list_display = ["lastName", "middleName", "firstName", "grade", "gender",
                    "phone_number", "email", "address", "city", "county",
                    "nationality", "dateOfBirth", "placeOfBirth", "regDate",
                    "country", "emergency", "emergency_phone", "transcript",
                    "created", "modified"]
    list_display_links = ["lastName"]
    list_filter = ["lastName", "middleName", "firstName"]
    list_editable = ["firstName"]
    search_fields = ["lastName", "firstName"]

    class Meta:
        model = Registration

admin.site.register(Registration, RegistrationModelAdmin)


class StudentModelAdmin(admin.ModelAdmin):
    list_display = ["studentID", "registration", "student_photo",
                    "previous_school", "previous_school_address",
                    "last_year_attendance", "level", "enrollment_status",
                    "enrollment_Date", "created", "modified"]
    list_display_links = ["registration"]
    list_filter = ["enrollment_status", "previous_school"]
    search_fields = ["previous_school", "enrollment_Date"]

    class Meta:
        model = Student

admin.site.register(Student, StudentModelAdmin)


class ParentModelAdmin(admin.ModelAdmin):
    list_display = ["parentID", "student", "lastName", "middleName",
                    "firstName", "gender", "address", "phone_number", "email",
                    "nationality", "occupation", "entity_name",
                    "entity_address", "salary_range", "created", "modified"]
    list_display_links = ["parentID"]
    list_filter = ["lastName", "middleName", "firstName"]
    list_editable = ["firstName"]
    search_fields = ["lastName", "student"]

    class Meta:
        model = Parent

admin.site.register(Parent, ParentModelAdmin)


class StaffModelAdmin(admin.ModelAdmin):
    list_display = ["staffID", "staff_photo", "lastName", "middleName",
                    "firstName", "gender", "phone_number", "email",
                    "dateOfBirth", "placeOfBirth", "nationality",
                    "numberOfSubject", "qualification", "experience",
                    "licence", "age", "created", "modified"]
    list_display_links = ["staffID"]
    list_filter = ["lastName", "middleName", "firstName"]
    list_editable = ["firstName"]
    search_fields = ["lastName", "numberOfSubject"]

    class Meta:
        model = Staff

admin.site.register(Staff, StaffModelAdmin)


class Staff_PositionModelAdmin(admin.ModelAdmin):
    list_display = ["staff", "departmentName", "created"]
    list_display_links = ["staff"]
    list_filter = ["departmentName", "staff"]
    search_fields = ["departmentName"]

    class Meta:
        model = Staff_Position

admin.site.register(Staff_Position, Staff_PositionModelAdmin)


class GradeModelAdmin(admin.ModelAdmin):
    list_display = ["student", "grade", "sponsor", "totalNumberOfStudents",
                    "created"]
    list_display_links = ["grade"]
    list_filter = ["sponsor", "grade"]
    search_fields = ["sponsor", "grade"]

    class Meta:
        model = Grade

admin.site.register(Grade, GradeModelAdmin)


class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ["staff", "subject", "created"]
    list_display_links = ["subject"]
    list_filter = ["staff", "subject"]
    search_fields = ["subject"]

    class Meta:
        model = Subject

admin.site.register(Subject, SubjectModelAdmin)


class FeeModelAdmin(admin.ModelAdmin):
    list_display = ["grade", "totalannualfee", "created", "modified"]
    list_display_links = ["grade"]
    list_filter = ["totalannualfee", "grade"]
    search_fields = ["grade"]

    class Meta:
        model = Fee

admin.site.register(Fee, FeeModelAdmin)


class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ["ReceiptNo", "student", "fee", "installment",
                    "amount", "balance",
                    "digitalSignature",
                    "transaction_Date", "created", "modified"]
    list_display_links = ["student"]
    list_filter = ["installment", "amount"]
    search_fields = ["ReceiptNo"]

    class Meta:
        model = Payment

admin.site.register(Payment, PaymentModelAdmin)


class SalarieModelAdmin(admin.ModelAdmin):
    list_display = ["staff", "grossmonthlysalary", "monthlyincometax",
                    "contractperiod", "grossannualsalary", "accountnumber",
                    "taxDeduct", "yearstart",
                    "yearend", "created", "modified"]
    list_display_links = ["staff"]
    list_filter = ["contractperiod", "grossmonthlysalary"]
    search_fields = ["staff"]

    class Meta:
        model = Salarie

admin.site.register(Salarie, SalarieModelAdmin)


class PayrollModelAdmin(admin.ModelAdmin):
    list_display = ["staff", "monthly",
                    "netmonthlysalary", "month", "salaryDate", "created"]
    list_display_links = ["staff"]
    list_filter = ["monthly"]
    search_fields = ["staff"]

    class Meta:
        model = Payroll

admin.site.register(Payroll, PayrollModelAdmin)


class AcademicYearModelAdmin(admin.ModelAdmin):
    list_display = ["yearstart", "yearend", "semester", "student",
                    "isactive", "created"]
    list_display_links = ["student"]
    list_filter = ["yearstart"]
    search_fields = ["student"]

    class Meta:
        model = AcademicYear

admin.site.register(AcademicYear, AcademicYearModelAdmin)


class StudentMarkModelAdmin(admin.ModelAdmin):
    list_display = ["student", "semester", "subject", "peroid",
                    "gradeScore", "studenRank", "status", "created"]
    list_display_links = ["student"]
    list_filter = ["subject", "peroid"]
    search_fields = ["subject", "gradeScore"]

    class Meta:
        model = StudentMark

admin.site.register(StudentMark, StudentMarkModelAdmin)


class ClassScheduleModelAdmin(admin.ModelAdmin):
    list_display = ["yearstart", "yearend", "grade", "day", "classTimein",
                    "classTimeout", "semester", "subject", "staff",
                    "created", "modified"]
    list_display_links = ["grade"]
    list_filter = ["day", "classTimein"]
    search_fields = ["staff", "subject"]

    class Meta:
        model = ClassSchedule

admin.site.register(ClassSchedule, ClassScheduleModelAdmin)


class StudentAttendanceModelAdmin(admin.ModelAdmin):
    list_display = ["student", "semester", "grade", "day",
                    "reasonAbsent", "absentDate", "created"]
    list_display_links = ["student"]
    list_filter = ["grade", "student"]
    search_fields = ["absent", "reasonAbsent"]

    class Meta:
        model = StudentAttendance

admin.site.register(StudentAttendance, StudentAttendanceModelAdmin)


class ContactInline(admin.StackedInline):
    model = UserLog
    can_delete = False
    verbose_name_plural = 'user'

# Define a new User admin


class UserAdmin(BaseUserAdmin):
    inlines = (ContactInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
