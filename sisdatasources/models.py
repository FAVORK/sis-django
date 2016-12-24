from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils.translation import ugettext as _


GENDER_CHOICES = (
    (u"MALE", u"MALE"),
    (u"FEMALE", u"FEMALE"),
)


COUNTY_CHOICES = (
    (u"BOMI", u"BOMI"),
    (u"BONG", u"BONG"),
    (u"GBARPOLU", u"GBARPOLU"),
    (u"GRAND BASSA", u"GRAND BASSA"),
    (u"GRAND GEDEH", u"GRAND GEDEH"),
    (u"GRAND KRU", u"GRAND KRU"),
    (u"GRAND CAPE MOUNT", u"GRAND CAPE MOUNT"),
    (u"MARGIBI", u"MARGIBI"),
    (u"MARYLAND", u"MARYLAND"),
    (u"MONTSERRADO", u"MONTSERRADO"),
    (u"NIMBA", u"NIMBA"),
    (u"LOFA", u"LOFA"),
    (u"RIVERCESS", u"RIVERCESS"),
    (u"RIVERGEE", u"RIVERGEE"),
    (u"SINOE", u"SINOE"),
)

LEVEL_CHOICES = (
    (u"ELEMENTARY", u"ELEMENTARY"),
    (u"JUNIOR HIGH", u"JUNIOR HIGH"),
    (u"SENIOR HIGH", u"SENIOR HIGH"),
)

CLASS_CHOICES = (
    (u"1st", u"1st"),
    (u"2nd", u"2nd"),
    (u"3rd", u"3rd"),
    (u"4th", u"4th"),
    (u"5th", u"5th"),
    (u"6th", u"6th"),
    (u"7th", u"7th"),
    (u"8th", u"8th"),
    (u"9th", u"9th"),
    (u"10th", u"10th"),
    (u"11th", u"11th"),
    (u"12th", u"12th"),
)

ENROLLMENT_CHOICES = (
    (u"ENROLLED", u"ENROLLED"),
    (u"DID NOT ENROLL", u"DID NOT ENROLL"),
    (u"DROPPED", u"DROPPED"),
    (u"EXPELLED", u"EXPELLED"),
)

SUBJECT_CHOICES = (
    (u"ENGLISH", u"ENGLISH"),
    (u"MATH", u"MATH"),
    (u"HISTORY", u"HISTORY"),
)

SCHEDULE_CHOICES = (
    (u"MONDAY", u"MONDAY"),
    (u"TUESDAY", u"TUESDAY"),
    (u"WEDNESDAY", u"WEDNESDAY"),
    (u"THURSDAY", u"THURSDAY"),
    (u"FRIDAY", u"FRIDAY"),
)

POSITION_CHOICES = (
    (u"TEACHER", u"TEACHER"),
    (u"PRINCIPAL", u"PRINCIPAL"),
    (u"VICE PRINCIPAL", u"VICE PRINCIPAL"),
    (u"ACCOUNTANT", u"ACCOUNTANT"),
)

MONTH_CHOICES = (
    (u"JANUARY", u"JANUARY"),
    (u"FEBRUARY", u"FEBRUARY"),
    (u"MARCH", u"MARCH"),
    (u"APRIL", u"APRIL"),
    (u"MAY", u"MAY"),
    (u"JUNE", u"JUNE"),
    (u"JULY", u"JULY"),
    (u"AUGUST", u"AUGUST"),
    (u"SEPTEMBER", u"SEPTEMBER"),
    (u"OCTOBER", u"OCTOBER"),
    (u"NOVEMBER", u"NOVEMBER"),
    (u"DECEMBER", u"DECEMBER"),
)

SEMESTER_CHOICES = (
    (u"1st SEMESTER", u"1st SEMESTER"),
    (u"2nd SEMESTER", u"2nd SEMESTER"),
)

ACTIVE_CHOICES = (
    (u"YES", u"YES"),
    (u"NO", u"NO"),
)

PERIOD_CHOICES = (
    (u"1st PERIOD", u"1st PERIOD"),
    (u"2nd PERIOD", u"2nd PERIOD"),
    (u"3rd PERIOD", u"3rd PERIOD"),
    (u"1st SEMESTER EXAM", u"1st SEMESTER EXAM"),
    (u"4th PERIOD", u"4th PERIOD"),
    (u"5th PERIOD", u"5th PERIOD"),
    (u"6th PERIOD", u"6th PERIOD"),
    (u"2nd SEMESTER EXAM", u"2nd SEMESTER EXAM"),
)

RANK_CHOICES = (
    (u"PASSED", u"PASSED"),
    (u"FAILED", u"FAILED"),
)

ATTENDANCE_CHOICES = (
    (u"PRESENT", u"PRESENT"),
    (u"ABSENT", u"ABSENT"),
)

INSTALLMENT_CHOICES = (
    (u"FIRST", u"FIRST"),
    (u"SECOND", u"SECOND"),
    (u"THIRD", u"THIRD"),
    (u"FOURTH", u"FOURTH"),
)


class Registration(models.Model):

    """
    This represents a single registration for each student.
    An entry must be done for every student who intends to register
    for admission.
    """

    lastName = models.CharField(
        _('Last Name'),
        max_length=30,
        null=False,
        blank=False
    )

    middleName = models.CharField(
        _('Middle Name'),
        max_length=30,
        null=True,
        blank=True
    )

    firstName = models.CharField(
        _('First Name'),
        max_length=30,
        null=False,
        blank=False
    )

    gender = models.CharField(
        _('Gender'),
        max_length=30,
        choices=GENDER_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    grade = models.CharField(
        _('Class'),
        max_length=30,
        choices=CLASS_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number format: '+999999999'. Up to 15 digits allowed."

    )
    phone_number = models.CharField(
        _('Phone Number'),
        max_length=255,
        validators=[phone_regex],
        blank=True
    )

    email = models.EmailField(
        _('Email Address'),
        max_length=254,
        null=True,
        blank=True
    )

    address = models.CharField(
        _('Address'),
        max_length=255,
        null=False,
        blank=False
    )

    city = models.CharField(
        _('City'),
        max_length=30,
        null=False,
        blank=False
    )

    county = models.CharField(
        _('County'),
        max_length=30,
        choices=COUNTY_CHOICES,
        default=None,
        null=False,
        blank=False
    )

    nationality = models.CharField(
        _('Nationality'),
        max_length=30,
        null=False,
        blank=False
    )

    dateOfBirth = models.DateField(
        _('Date of Birth'),
        max_length=30,
        null=False,
        blank=False
    )

    placeOfBirth = models.CharField(
        _('Place of Birth'),
        max_length=255,
        null=False,
        blank=False
    )

    regDate = models.DateField(
        _('Registration Date'),
        max_length=30,
        null=False,
        blank=False
    )

    country = models.CharField(
        _('Country'),
        max_length=255,
        null=False,
        blank=False
    )

    emergency = models.CharField(
        _('Emergency Contact'),
        max_length=255,
        null=True,
        blank=True
    )

    emergency_phone = models.CharField(
        _('Phone (Emergency Contact)'),
        max_length=255,
        validators=[phone_regex],
        blank=True
    )

    transcript = models.FileField(
        _('Transcript'),
        max_length=255,
        null=True,
        blank=True
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )
    modified = models.DateTimeField(
        _('Date Modified'),
        auto_now_add=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.firstName

    def age(self):
        import datetime
        return int((datetime.date.today() - self.dateOfBirth).days / 365.25)


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Student(models.Model):

    """
    This represents a single student who has decided to enrol.
    It's a foreign key to registration and will get the remaining info
    from the registration table.
    """
    import datetime
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))

    studentID = models.CharField(
        _('Student ID'),
        max_length=30,
        blank=True,
        default=''

    )

    registration = models.ForeignKey(
        Registration
    )

    student_photo = models.ImageField(
        _('Picture'),
        max_length=255,
        null=False,
        blank=False,
        upload_to=upload_location
    )

    previous_school = models.CharField(
        _('Previous School Attended'),
        max_length=255,
        null=False,
        blank=False
    )

    previous_school_address = models.CharField(
        _('Previous School Address'),
        max_length=255,
        null=False,
        blank=False
    )

    last_year_attendance = models.IntegerField(
        _('Last Year of Attendance'),
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year
    )

    level = models.CharField(
        _('Level'),
        max_length=255,
        choices=LEVEL_CHOICES,
        default=None,
        null=False,
        blank=False
    )

    enrollment_status = models.CharField(
        _('Enrollment Status'),
        max_length=255,
        choices=ENROLLMENT_CHOICES,
        default=None,
        null=False,
        blank=False
    )

    enrollment_Date = models.DateField(
        _('Enrollment Date'),
        max_length=30,
        null=False,
        blank=False
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )
    modified = models.DateTimeField(
        _('Date Modified'),
        auto_now_add=True,
        null=False,
        blank=False
    )

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.studentID

    def save(self, force_insert=False, force_update=False):
        if self.studentID == "":
            existing_studentIDs = Student.objects.all().order_by('-studentID')
            if existing_studentIDs.count() > 0:
                new_code = int(existing_studentIDs[0].studentID[1:]) + 1
            else:
                new_code = 0
            self.studentID = 'S%03d' % new_code
        super(Student, self).save(force_insert, force_update)


class Parent(models.Model):

    """
    This represents a single teacher.
    He/she is teaching many subjects and classes.
    """

    parentID = models.CharField(
        _('Parent ID'),
        max_length=30,
        blank=True,
        default=''

    )

    student = models.ForeignKey(
        Student
    )

    lastName = models.CharField(
        _('Last Name'),
        max_length=30,
        null=False,
        blank=False
    )

    middleName = models.CharField(
        _('Middle Name'),
        max_length=30,
        null=True,
        blank=True
    )

    firstName = models.CharField(
        _('First Name'),
        max_length=30,
        null=False,
        blank=False
    )

    gender = models.CharField(
        _('Gender'),
        max_length=30,
        choices=GENDER_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    address = models.CharField(
        _('Address'),
        max_length=255,
        null=False,
        blank=False
    )

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number format: '+999999999'. Up to 15 digits allowed."

    )

    phone_number = models.CharField(
        _('Phone Number'),
        max_length=255,
        validators=[phone_regex],
        blank=True
    )

    email = models.EmailField(
        _('Email Address'),
        max_length=254,
        null=True,
        blank=True
    )

    nationality = models.CharField(
        _('Nationality'),
        max_length=255,
        null=True,
        blank=True
    )

    occupation = models.CharField(
        _('Occupation'),
        max_length=255,
        null=True,
        blank=True
    )

    entity_name = models.CharField(
        _('Name of Entity'),
        max_length=255,
        null=True,
        blank=True
    )

    entity_address = models.CharField(
        _('Entity Address'),
        max_length=255,
        null=True,
        blank=True
    )

    salary_range = models.IntegerField(
        _('Salary Range'),
        null=True,
        blank=True
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )
    modified = models.DateTimeField(
        _('Date Modified'),
        auto_now_add=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.parentID

    def save(self, force_insert=False, force_update=False):
        if self.parentID == "":
            existing_parentIDs = Parent.objects.all().order_by('-parentID')
            if existing_parentIDs.count() > 0:
                new_code = int(existing_parentIDs[0].parentID[1:]) + 1
            else:
                new_code = 0
            self.parentID = 'P%03d' % new_code
        super(Parent, self).save(force_insert, force_update)


class Staff(models.Model):

    """
    This represents a single teacher.
    He/she is teaching many subjects and classes.
    """

    staffID = models.CharField(
        _('Staff ID'),
        max_length=30,
        blank=True,
        default=''

    )

    staff_photo = models.ImageField(
        _('Teacher Picture'),
        max_length=255,
        null=False,
        blank=False,
        upload_to=upload_location
    )

    lastName = models.CharField(
        _('Last Name'),
        max_length=30,
        null=False,
        blank=False
    )

    middleName = models.CharField(
        _('Middle Name'),
        max_length=30,
        null=True,
        blank=True
    )

    firstName = models.CharField(
        _('First Name'),
        max_length=30,
        null=False,
        blank=False
    )

    gender = models.CharField(
        _('Gender'),
        max_length=30,
        choices=GENDER_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number format: '+999999999'. Up to 15 digits allowed."

    )

    phone_number = models.CharField(
        _('Phone Number'),
        max_length=255,
        validators=[phone_regex],
        blank=True
    )

    email = models.EmailField(
        _('Email Address'),
        max_length=254,
        null=True,
        blank=True
    )

    dateOfBirth = models.DateField(
        _('Date of Birth'),
        max_length=30,
        null=False,
        blank=False
    )

    placeOfBirth = models.CharField(
        _('Place of Birth'),
        max_length=255,
        null=False,
        blank=False
    )

    nationality = models.CharField(
        _('Nationality'),
        max_length=255,
        null=False,
        blank=False
    )

    numberOfSubject = models.IntegerField(
        _('Number of Subject Teaching'),
        null=False,
        blank=False
    )

    qualification = models.CharField(
        _('Highest Qualification'),
        max_length=255,
        null=False,
        blank=False
    )

    experience = models.CharField(
        _('Experience in years'),
        max_length=255,
        null=False,
        blank=False
    )

    licence = models.CharField(
        _('Licence'),
        max_length=255,
        null=False,
        blank=False
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )
    modified = models.DateTimeField(
        _('Date Modified'),
        auto_now_add=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.staffID

    def save(self, force_insert=False, force_update=False):
        if self.staffID == "":
            existing_staffIDs = Staff.objects.all().order_by('-staffID')
            if existing_staffIDs.count() > 0:
                new_code = int(existing_staffIDs[0].staffID[1:]) + 1
            else:
                new_code = 0
            self.staffID = 'T%03d' % new_code
        super(Staff, self).save(force_insert, force_update)

    def age(self):
        import datetime
        return int((datetime.date.today() - self.dateOfBirth).days / 365.25)


class Staff_Position(models.Model):

    """
    This represents a single teacher.
    He/she is teaching many subjects and classes.
    """

    staff = models.ForeignKey(
        Staff
    )

    departmentName = models.CharField(
        _('Staff Position'),
        max_length=30,
        choices=POSITION_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.departmentName


class Grade(models.Model):

    """
    This represents subjects.
    Subjects will be taught by teachers.
    """

    student = models.ForeignKey(
        Student
    )

    grade = models.CharField(
        _('Class'),
        max_length=30,
        choices=CLASS_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    sponsor = models.ForeignKey(
        Staff
    )

    totalNumberOfStudents = models.IntegerField(
        _('Total Number of Students'),
        blank=False,
        null=False,
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.grade


class Subject(models.Model):

    """
    This represents subjects.
    Subjects will be taught by teachers.
    """

    staff = models.ForeignKey(
        Staff,
        null=True
    )

    subject = models.CharField(
        _('Subject'),
        max_length=30,
        choices=SUBJECT_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.subject)


class Fee(models.Model):

    """
    This represents subjects.
    Subjects will be taught by teachers.
    """

    grade = models.CharField(
        _('Class'),
        max_length=30,
        choices=CLASS_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    totalannualfee = models.FloatField(
        _('Total Annual Fee'),
        null=False,
        blank=False,
        default=0.00
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )
    modified = models.DateTimeField(
        _('Date Modified'),
        auto_now_add=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return str(self.totalannualfee)


class Payment(models.Model):

    """
    This represents subjects.
    Subjects will be taught by teachers.
    """

    ReceiptNo = models.CharField(
        _('Receipt Number'),
        max_length=30,
        blank=True,
        default=''

    )

    student = models.ForeignKey(
        Student
    )

    fee = models.ForeignKey(
        Fee
    )

    installment = models.CharField(
        _('Installment'),
        max_length=30,
        choices=INSTALLMENT_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    amount = models.FloatField(
        _('Amount'),
        null=False,
        blank=False,
        default=0.00

    )

    digitalSignature = models.CharField(
        _('Digital Signature'),
        max_length=255,
        null=True,
        blank=True
    )

    transaction_Date = models.DateField(
        _('Date of Transaction'),
        auto_now=True,
        null=True,
        blank=True
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )

    modified = models.DateTimeField(
        _('Date Modified'),
        auto_now_add=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.ReceiptNo

    def save(self, *args, **kwargs):
        if self.ReceiptNo == "":
            existing_ReceiptNos = Payment.objects.all().order_by('-ReceiptNo')
            if existing_ReceiptNos.count() > 0:
                new_code = int(existing_ReceiptNos[0].ReceiptNo[1:]) + 1
            else:
                new_code = 0
            self.ReceiptNo = 'R%03d' % new_code
        super(Payment, self).save(*args, **kwargs)

    @property
    def balance(self):
        if self.installment == "FIRST":
            return self.fee.totalannualfee - self.amount
        # else:
        #     return self.balance - self.amount


class Salarie(models.Model):

    """
    This represents subjects.
    Subjects will be taught by teachers.
    """

    import datetime
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))

    staff = models.ForeignKey(
        Staff
    )

    grossmonthlysalary = models.FloatField(
        _('Monthly Salary'),
        null=False,
        blank=False,
        default=0.00
    )

    monthlyincometax = models.FloatField(
        _('Monthly Income Tax'),
        null=False,
        blank=False
    )

    contractperiod = models.IntegerField(
        _('Contract Period'),
        null=False,
        blank=False
    )

    accountnumber = models.CharField(
        _('Account Number'),
        max_length=255,
        null=False,
        blank=False
    )

    yearstart = models.IntegerField(
        _('Academic Year Start'),
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year
    )

    yearend = models.IntegerField(
        _('Academic Year End'),
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )

    modified = models.DateTimeField(
        _('Date Modified'),
        auto_now_add=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return str(self.grossmonthlysalary)

    @property
    def grossannualsalary(self):
            return self.grossmonthlysalary * self.contractperiod

    @property
    def taxDeduct(self):
            return self.grossmonthlysalary * self.monthlyincometax / 100


class Payroll(models.Model):

    """
    This represents subjects.
    Subjects will be taught by teachers.
    """

    staff = models.ForeignKey(
        Staff
    )

    monthly = models.ForeignKey(
        Salarie
    )

    month = models.CharField(
        _('Month Paid For'),
        max_length=30,
        choices=MONTH_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    salaryDate = models.DateField(
        _('Paid Date'),
        auto_now=True,
        null=True,
        blank=True
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )

    modified = models.DateTimeField(
        _('Date Modified'),
        auto_now_add=True,
        null=False,
        blank=False
    )

    @property
    def netmonthlysalary(self):
            return self.monthly.grossmonthlysalary - self.monthly.taxDeduct


class AcademicYear(models.Model):

    """
    This represents subjects.
    Subjects will be taught by teachers.
    """

    import datetime
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))

    yearstart = models.IntegerField(
        _('Academic Year Start'),
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year
    )

    yearend = models.IntegerField(
        _('Academic Year End'),
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year
    )

    semester = models.CharField(
        _('Semester'),
        max_length=30,
        choices=SEMESTER_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    student = models.ForeignKey(
        Student
    )

    isactive = models.CharField(
        _('Active'),
        max_length=30,
        choices=ACTIVE_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )

    modified = models.DateTimeField(
        _('Date Modified'),
        auto_now_add=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.semester


class StudentMark(models.Model):

    """
    This represents subjects.
    Subjects will be taught by teachers.
    """

    student = models.ForeignKey(
        Student
    )

    semester = models.CharField(
        _('Semester'),
        max_length=30,
        choices=SEMESTER_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    subject = models.ForeignKey(
        Subject
    )

    peroid = models.CharField(
        _('Period Test'),
        max_length=30,
        choices=PERIOD_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    gradeScore = models.CharField(
        _('Grade Scored'),
        max_length=30,
        blank=True,
        default=''

    )

    studenRank = models.CharField(
        _('Student Rank'),
        max_length=30,
        blank=True,
        default=''

    )

    status = models.CharField(
        _('Status'),
        max_length=30,
        choices=RANK_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )

    modified = models.DateTimeField(
        _('Date Modified'),
        auto_now_add=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.status


class ClassSchedule(models.Model):

    """
    This represents subjects.
    Subjects will be taught by teachers.
    """

    import datetime
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))

    yearstart = models.IntegerField(
        _('Academic Year Start'),
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year
    )

    yearend = models.IntegerField(
        _('Academic Year End'),
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year
    )

    grade = models.CharField(
        _('Class'),
        max_length=30,
        choices=CLASS_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    day = models.CharField(
        _('Days'),
        max_length=30,
        choices=SCHEDULE_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    classTimein = models.TimeField(
        _('Time in'),
        null=True,
        blank=True

    )

    classTimeout = models.TimeField(
        _('Time out'),
        null=True,
        blank=True

    )

    semester = models.CharField(
        _('Semester'),
        max_length=30,
        choices=SEMESTER_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    peroid = models.CharField(
        _('Period Test'),
        max_length=30,
        choices=PERIOD_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    subject = models.ForeignKey(
        Subject
    )

    staff = models.ForeignKey(
        Staff
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )

    modified = models.DateTimeField(
        _('Date Modified'),
        auto_now_add=True,
        null=False,
        blank=False
    )


class StudentAttendance(models.Model):

    """
    This represents subjects.
    Subjects will be taught by teachers.
    """

    student = models.ForeignKey(
        Student
    )

    semester = models.CharField(
        _('Semester'),
        max_length=30,
        choices=SEMESTER_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    peroid = models.CharField(
        _('Period Test'),
        max_length=30,
        choices=PERIOD_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    grade = models.CharField(
        _('Class'),
        max_length=30,
        choices=CLASS_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    day = models.CharField(
        _('Days'),
        max_length=30,
        choices=SCHEDULE_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    status = models.CharField(
        _('Status'),
        max_length=30,
        choices=ATTENDANCE_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    reasonAbsent = models.TextField(
        _('Reason Absent'),
        max_length=255,
        blank=True,
        default=''

    )

    absentDate = models.DateField(
        _('Date'),
        auto_now=True,
        null=True,
        blank=True
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )


class UserLog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    student = models.ForeignKey(
        Student,
        null=True,
        blank=True,
        default=None
    )

    staff = models.ForeignKey(
        Staff,
        null=True,
        blank=True,
        default=None
    )

    parent = models.ForeignKey(
        Parent,
        null=True,
        blank=True,
        default=None
    )
