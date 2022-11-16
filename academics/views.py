import csv, io
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import CustomUserCreationForm
from .models import Student, Course, CourseRegistrationAndResult, StudentGrade
from django.db.models import Sum
from django.http import HttpResponse



def loginView(request):       
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email OR Password is incorrect.')
    return render(request, 'academics/login.html')

def logoutView(request):
    logout(request)
    return redirect('login')


def registerView(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            user.username = user.username.lower()
            user.email = user.email.lower()
            user.is_active = True
            user.save()
            messages.success(request, 'Your profile has been created.')

            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'An error occurred while creating your account.')

    context = {'form': form}

    return render(request, 'academics/register.html', context)


def homeView(request):    
    student = request.user    
    completion = Student.objects.filter(user=student)    
    
    for stud in completion:
        number = stud.profile_completion        
        if number < 100:
            return redirect('profile-update')
         
    return render(request, 'academics/home.html')


@login_required(login_url='login')
def profileUpdateView(request):
    student = request.user
    studentProfile = Student.objects.filter(user=student.id)
    print (studentProfile)
    
    if request.method == 'POST':
        for stud in studentProfile:
            stud.matric_no = request.POST['matric_no']
            stud.entry_date = request.POST['entry_date']            
            stud.dob = request.POST['dob']
            stud.gender = request.POST['gender']           
            stud.profile_completion = 100
            stud.save()           
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('home')    
    return render(request, 'academics/profile_update.html')


@login_required(login_url='login')
def viewRegistration(request):   
    students = Student.objects.filter(user=request.user)
    global val2
    def val2():
        return students

    # Checking student level and semester
    check_student = Student.objects.get(user=request.user)
    check_level = check_student.level
    check_semester = check_student.semester      
       
    selected_level = ''
    selected_semester = ''        
    all_courses = Course.objects.filter(Q(level=selected_level) & Q(semester=selected_semester))
    total_credits = all_courses.aggregate(Sum('credits'))['credits__sum'] 

    if request.method == 'POST':
        level_semester = request.POST['level_semester']          
        if level_semester == '1st Semester - 300L':
            selected_level = '300'
            selected_semester = 'First'        
            all_courses = Course.objects.filter(
            Q(level=selected_level) & Q(semester=selected_semester)
        )
            total_credits = all_courses.aggregate(Sum('credits'))['credits__sum'] 
            
        elif level_semester == '2nd Semester - 300L':
             selected_level = '300'
             selected_semester = 'Second'        
             all_courses = Course.objects.filter(
             Q(level=selected_level) & Q(semester=selected_semester)
        )
             total_credits = all_courses.aggregate(Sum('credits'))['credits__sum']

        elif level_semester == '1st Semester - 400L':
             selected_level = '400'
             selected_semester = 'First'        
             all_courses = Course.objects.filter(
             Q(level=selected_level) & Q(semester=selected_semester)
        )
             total_credits = all_courses.aggregate(Sum('credits'))['credits__sum']

        elif level_semester == '2nd Semester - 400L':
             selected_level = '400'
             selected_semester = 'Second'        
             all_courses = Course.objects.filter(
             Q(level=selected_level) & Q(semester=selected_semester)
        )
             total_credits = all_courses.aggregate(Sum('credits'))['credits__sum']  

        elif level_semester == '1st Semester - 500L':
             selected_level = '500'
             selected_semester = 'First'        
             all_courses = Course.objects.filter(
             Q(level=selected_level) & Q(semester=selected_semester)
        )
             total_credits = all_courses.aggregate(Sum('credits'))['credits__sum']

        elif level_semester == '2nd Semester - 500L':
             selected_level = '500'
             selected_semester = 'Second'        
             all_courses = Course.objects.filter(
             Q(level=selected_level) & Q(semester=selected_semester)
        )
             total_credits = all_courses.aggregate(Sum('credits'))['credits__sum'] 

        global val 
        def val():
            return all_courses

        global val3
        def val3():
            return selected_level

        global val4
        def val4():
            return selected_semester     
      
    context = {
        'all_courses': all_courses,
        'total_credits': total_credits,
        'check_level': check_level,
        'check_semester': check_semester,
        }
    return render(request, 'academics/course_registration.html', context)


def courseRegistration(request):
    if request.method == 'POST':               
        
        for course in val():            
            selected_course = course

            for student in val2():
                selected_student = student        

            register_course = CourseRegistrationAndResult.objects.create(
                student=selected_student, 
                course=selected_course,
                level=val3(),
                semester=val4()
            )
            
    student_update = Student.objects.get(user=request.user)
    student_update.level = val3()
    student_update.semester = val4()
    student_update.save() 
    messages.success(request, 'Your course registration was successfully.')  
    return redirect('home')           
    return render(request, 'academics/course_registration.html')

    
def generateResult(request):
    student = Student.objects.get(user=request.user)
    logged_in_student = student.id

    # for django template rendering
    template_students = Student.objects.filter(user=request.user)    
    result_courses21 = None
    total_semester_credits2 = None
    level_semester2 = None
    total_semester_grade_point2 = None
    cgpa2 = None
    gpa2 = None    
    gpa_sum2 = 0.00
    final = None
    status2 = None
    pgpa = None
    c_p_gpa = None
    
      
    
    if request.method == 'POST':
        level_semester = request.POST['level_semester'] 

        if level_semester == '1st Semester - 300L':
            result_level = '300'
            result_semester = 'First'

        elif level_semester == '2nd Semester - 300L':
             result_level = '300'
             result_semester = 'Second'

        elif level_semester == '1st Semester - 400L':
             result_level = '400'
             result_semester = 'First' 

        elif level_semester == '2nd Semester - 400L':
             result_level = '400'
             result_semester = 'Second'
    
   
    
        result_courses = CourseRegistrationAndResult.objects.filter(student=logged_in_student)    
        all_semester_courses = Course.objects.filter(Q(level=result_level) & Q(semester=result_semester))
        total_semester_credits = all_semester_courses.aggregate(Sum('credits'))['credits__sum']  

        for course in result_courses:
            
            if course.exam_score >= 70:
                grade = 'A'
                point = 5
            elif course.exam_score >= 60:
                grade = 'B'
                point = 4
            elif course.exam_score >= 50:
                grade = 'C'
                point = 3
            elif course.exam_score >= 40:
                grade = 'D'
                point = 2
            else:
                grade = 'F'
                point = 0
            
            global val5
            def val5():
                return grade

            if course.grade_point is None:
                grade_point = course.course.credits * point
                course.grade_point = grade_point
                course.save()        
            
        # Save the student's GPA
        result_courses2 = CourseRegistrationAndResult.objects.filter(
            Q(student=logged_in_student) & Q(level=result_level) & Q(semester=result_semester)
        )  
        total_semester_grade_point = result_courses2.aggregate(Sum('grade_point'))['grade_point__sum']
        gpa = total_semester_grade_point/total_semester_credits   
    
        obj, created = StudentGrade.objects.get_or_create(
                    student=student, 
                    level=result_level,
                    semester=result_semester,
                    gpa=round(gpa, 2),
                    status='Completed'
                )
        
        # Update the student's CGPA
        student_gpa = StudentGrade.objects.filter(student=logged_in_student)
        result_count = student_gpa.count()
        gpa_sum = student_gpa.aggregate(Sum('gpa'))['gpa__sum']
        cgpa = gpa_sum/result_count
        
        if result_count >= 4:
            student.cgpa = round(cgpa, 2)
            student.status = 'Completed'
        else:
            student.cgpa = round(cgpa, 2)       
            student.save() 

                
        # Template status and previous grade point
        level_semester3 = request.POST['level_semester'] 

        if level_semester3 == '1st Semester - 300L':
            result_level2 = '300'
            result_semester2 = 'First'            
            

        elif level_semester3 == '2nd Semester - 300L':
             result_level2 = '300'
             result_semester2 = 'First'             
             

        elif level_semester3 == '1st Semester - 400L':
             result_level2 = '300'
             result_semester2 = 'Second'              
             

        elif level_semester3 == '2nd Semester - 400L':
             result_level2 = '400'
             result_semester2 = 'First'
             final = 'Grade Description'          
             
   
        student_grade = StudentGrade.objects.filter(
        Q(student=logged_in_student) & Q(level=result_level2) & Q(semester=result_semester2)
    ) 
        for stud in student_grade:
            request.session['status'] = stud.status
            request.session['pgpa'] = str(stud.gpa)      
        
        result_courses21 = result_courses2
        total_semester_credits2 = total_semester_credits
        level_semester2 = level_semester
        total_semester_grade_point2 = total_semester_grade_point        
        # gpa_sum2 = gpa_sum
        cgpa2 =  round(cgpa, 2)
        gpa2 = round(gpa, 2)
        status2 = request.session['status']
        pgpa = float(request.session['pgpa'])
        c_p_gpa = round((gpa_sum2), 2)
        
        
    context ={
        'result_courses21': result_courses21,
        'total_semester_credits2': total_semester_credits2,        
        'template_students' : template_students,
        'level_semester2' : level_semester2,
        'total_semester_grade_point2' : total_semester_grade_point2,
        'cgpa2' : cgpa2,
        'gpa2' : gpa2,
        'status2' : status2,
        'pgpa' : pgpa,
        'c_p_gpa' : c_p_gpa,
        'final' : final,
    }
    return render(request, 'academics/result.html', context)

@permission_required('admin.can_add_log_entry')
def upload_exam_scores(request):
    
    if request.method == 'GET':
        return render(request, 'academics/upload_score.html')
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a valid CSV file')
    
    data_set = csv_file.read().decode('utf-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    # Get the csv file data excluding the header 
    data = csv.reader(io_string, delimiter=',', quotechar="|")

    # Convert the data to a list data
    data2 = list(data)

    # Update the CourseRegistrationAndResult model with the list data        
    for column in data2:
        course_reg_result = CourseRegistrationAndResult.objects.get(
            Q(course = Course.objects.get(id=int(column[1]))) & Q(student = Student.objects.get(id=int(column[2])))
        )
        course_reg_result.exam_score = int(column[0])                    
        course_reg_result.save()
        messages.success(request, 'Upload was successful!')

    context = {}
    return render(request, 'academics/upload_score.html', context)

@permission_required('admin.can_add_log_entry')
def export_course_reg(request):
    course_reg = CourseRegistrationAndResult.objects.all()
   
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename="course_reg.csv'
    writer = csv.writer(response)
    writer.writerow(['exam_score', 'course_id', 'student_id', 'grade_point', 'level', 'semester'])   
    course_reg_fields = course_reg.values_list('exam_score', 'course', 'student', 'grade_point', 'level', 'semester')
    for course in course_reg_fields:
        writer.writerow(course)
    return response
