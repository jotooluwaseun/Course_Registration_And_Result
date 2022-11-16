from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    PROGRAM = (
        ('Part-Time', 'Part-Time'),
        ('HND Conversion', 'HND Conversion'),
    )

    STATUS = (
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    matric_no = models.CharField(max_length=150, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=6, null=True, blank=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True, default=1)
    level = models.CharField(max_length=50, null=True, blank=True)
    semester = models.CharField(max_length=50, null=True, blank=True)
    entry_date = models.DateField(null=True, blank=True)
    graduated_date = models.DateField(null=True, blank=True)
    program = models.CharField(choices=PROGRAM, max_length=150, default='HND Conversion', null=True, blank=True)
    cgpa = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, null=True, blank=True)    
    status =models.CharField(choices=STATUS, max_length=20, default='In Progress', null=True, blank=True)
    profile_completion = models.IntegerField(default=50, null=True, blank=True)

    def __str__(self):        
        return  self.first_name + ' ' + self.last_name  + ' - ' + str(self.matric_no)
    
    class Meta:
        verbose_name_plural = 'Students'


class Department(models.Model):
    FACULTY = (
        ('Faculty of Natural Sciences','Faculty of Natural Sciences'),
    )
    name = models.CharField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=15, null=True, blank=True)
    faculty = models.CharField(choices=FACULTY, max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Departments'


class Course(models.Model):
    LEVEL = (
        ('300', '300'),
        ('400', '400'),
        ('500', '500'),
    )

    SEMESTER = (
        ('First', 'First'),
        ('Second', 'Second'),
    )

    STATUS = (
        ('C', 'C'),
        ('R', 'R'),
        ('E', 'E'),
    )
    title = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=15, null=True, blank=True)
    credits = models.IntegerField(null=True, blank=True)
    level = models.CharField(choices=LEVEL, max_length=3, null=True, blank=True)
    semester = models.CharField(choices=SEMESTER, max_length=20, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=20, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    lecturer = models.ForeignKey('Lecturer', on_delete=models.CASCADE, null=True, blank=True)
    selected = models.BooleanField(default=True)

    def __str__(self):
        return self.title + ' - ' + self.level
    
    class Meta:
        verbose_name_plural = 'Courses'


class Lecturer(models.Model):
    TITLE = (
        ('Mr.', 'Mr.'),
        ('Mrs.', 'Mrs.'),
        ('Ms.', 'Ms.'),
        ('Dr.', 'Dr.'),
        ('Prof.', 'Prof.'),
    )
    title = models.CharField(choices=TITLE, max_length=10, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    

    def __str__(self):
        return self.title + ' ' + self.last_name + ' ' + self.first_name
    
    class Meta:
        verbose_name_plural = 'Lecturers'


class CourseRegistrationAndResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    exam_score = models.PositiveIntegerField(null=True, blank=True)
    grade_point = models.PositiveIntegerField(null=True, blank=True)
    level = models.CharField(max_length=50, null=True, blank=True)
    semester = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.student.matric_no + ' - ' + self.course.code
    
    class Meta:
        verbose_name_plural = 'Course Registration and Results'


class StudentGrade(models.Model):
    LEVEL = (
        ('300', '300'),
        ('400', '400'),
        ('500', '500'),
    )

    SEMESTER = (
        ('First', 'First'),
        ('Second', 'Second'),
    )
    STATUS = (
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)    
    level = models.CharField(choices=LEVEL, max_length=3, null=True, blank=True)
    semester = models.CharField(choices=SEMESTER, max_length=20, null=True, blank=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=20, null=True, blank=True)

    def __str__(self):
        return self.student.matric_no + ' - ' + self.level + ' - ' + self.semester
    
    class Meta:
        verbose_name_plural = 'Student Grades'
    
