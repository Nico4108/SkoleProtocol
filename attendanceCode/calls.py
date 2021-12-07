from student.models import Student
from subject.models import StudentHasSubject
from django.db import connection
from attendanceCode.models import AttendanceLog, AttendanceCode


def get_statstic(keaclass, subject):
    try:
        data = []
        LessonsList = AttendanceCode.objects.filter(
            keaclass=keaclass, subject=subject)
        Lessoncount = LessonsList.count()
        students = Student.objects.filter(Class=keaclass)
        for student in students:
            if StudentHasSubject.objects.filter(
                    student_name_id=student, subject_name_id=subject):
                AttendanceList = AttendanceLog.objects.filter(
                    keaclass_id=keaclass, subject_id=subject, username_fk=student)
                countAttendance = AttendanceList.count()
                first = Student.objects.get(username=student).First_name
                last = Student.objects.get(username=student).Last_name
                studentwhole = first + " " + last
                data.append({
                    "name": studentwhole,
                    "countAttendance": countAttendance,
                    "countLessons": Lessoncount,
                })

        print(data)
        return data

    except BaseException:
        Exception


def get_statstic_class(keaclass, subject):
    try:
        data = []
        LessonsList = AttendanceCode.objects.filter(keaclass=keaclass)
        Lessoncount = LessonsList.count()
        students = Student.objects.filter(Class=keaclass)
        for student in students:
            AttendanceList = AttendanceLog.objects.filter(
                keaclass_id=keaclass, username_fk=student)
            countAttendance = AttendanceList.count()
            first = Student.objects.get(username=student).First_name
            last = Student.objects.get(username=student).Last_name
            studentwhole = first + " " + last
            data.append({
                "name": studentwhole,
                "countAttendance": countAttendance,
                "countLessons": Lessoncount,
            })

        print(data)
        return data

    except BaseException:
        Exception
