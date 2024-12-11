class Campus:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.employees = []
        self.courses = []
        self.income = 0

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_course(self, course):
        self.courses.append(course)

    def get_student_count(self):
        return len(self.students)

    def get_teacher_count(self):
        return len(self.teachers)

    def get_employee_count(self):
        return len(self.employees)

    def get_income(self):
        return self.income

    def add_income(self, amount):
        self.income += amount


class Student:
    def __init__(self, name, phone, campus, student_id):
        self.name = name
        self.phone = phone
        self.campus = campus
        self.student_id = student_id
        self.courses = []
        self.tuition_paid = 0

    def enroll_course(self, course):
        self.courses.append(course)
        self.campus.add_income(course.price)
        self.tuition_paid += course.price

    def get_info(self):
        return f"Name: {self.name}, Phone: {self.phone}, Campus: {self.campus.name}, Student ID: {self.student_id}"

    def get_courses(self):
        return [course.name for course in self.courses]

class Teacher:
    def __init__(self, name, phone, campus, teacher_id):
        self.name = name
        self.phone = phone
        self.campus = campus
        self.teacher_id = teacher_id
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def get_info(self):
        return f"Name: {self.name}, Phone: {self.phone}, Campus: {self.campus.name}, Teacher ID: {self.teacher_id}"

    def get_courses(self):
        return [course.name for course in self.courses]

class Course:
    def __init__(self, name, price, campus):
        self.name = name
        self.price = price
        self.campus = campus
        self.teacher = None
        self.students = []

    def assign_teacher(self, teacher):
        self.teacher = teacher
        teacher.add_course(self)

    def enroll_student(self, student):
        self.students.append(student)
        student.enroll_course(self)

    def get_students(self):
        return [student.name for student in self.students]

class Employee:
    def __init__(self, name, employee_id, campus):
        self.name = name
        self.employee_id = employee_id
        self.campus = campus

    def get_info(self):
        return f"Name: {self.name}, Employee ID: {self.employee_id}, Campus: {self.campus.name}"

class SupportStaff(Employee):
    def __init__(self, name, employee_id, campus):
        super().__init__(name, employee_id, campus)
        self.type = "Support Staff"

class FinanceStaff(Employee):
    def __init__(self, name, employee_id, campus):
        super().__init__(name, employee_id, campus)
        self.type = "Finance Staff"

class AdministrativeStaff(Employee):
    def __init__(self, name, employee_id, campus):
        super().__init__(name, employee_id, campus)
        self.type = "Administrative Staff"

class TrainingInstitute:
    def __init__(self):
        self.headquarters = Campus("八里台校区")
        self.branch_campuses = {
            "津南校区": Campus("津南校区"),
            "泰达校区": Campus("泰达校区")
        }

    def add_student(self, name, phone, campus_name, student_id):
        campus = self.get_campus(campus_name)
        student = Student(name, phone, campus, student_id)
        campus.add_student(student)
        return student

    def add_teacher(self, name, phone, campus_name, teacher_id):
        campus = self.get_campus(campus_name)
        teacher = Teacher(name, phone, campus, teacher_id)
        campus.add_teacher(teacher)
        return teacher

    def add_course(self, name, price, campus_name):
        campus = self.get_campus(campus_name)
        course = Course(name, price, campus)
        campus.add_course(course)
        return course

    def add_employee(self, name, employee_id, campus_name, employee_type):
        campus = self.get_campus(campus_name)
        if employee_type == "Support Staff":
            employee = SupportStaff(name, employee_id, campus)
        elif employee_type == "Finance Staff":
            employee = FinanceStaff(name, employee_id, campus)
        elif employee_type == "Administrative Staff":
            employee = AdministrativeStaff(name, employee_id, campus)
        else:
            raise ValueError("Invalid employee type")
        campus.add_employee(employee)
        return employee

    def get_campus(self, campus_name):
        if campus_name == "八里台校区":
            return self.headquarters
        elif campus_name in self.branch_campuses:
            return self.branch_campuses[campus_name]
        else:
            raise ValueError("Invalid campus name")

    def get_campus_info(self, campus_name):
        campus = self.get_campus(campus_name)
        return {
            "Student Count": campus.get_student_count(),
            "Teacher Count": campus.get_teacher_count(),
            "Employee Count": campus.get_employee_count(),
            "Income": campus.get_income()
        }

    def get_student_info(self, student_id):
        for campus in [self.headquarters] + list(self.branch_campuses.values()):
            for student in campus.students:
                if student.student_id == student_id:
                    return student.get_info()
        return "Student not found"

    def get_teacher_info(self, teacher_id):
        for campus in [self.headquarters] + list(self.branch_campuses.values()):
            for teacher in campus.teachers:
                if teacher.teacher_id == teacher_id:
                    return teacher.get_info()
        return "Teacher not found"

    def get_employee_info(self, employee_id):
        for campus in [self.headquarters] + list(self.branch_campuses.values()):
            for employee in campus.employees:
                if employee.employee_id == employee_id:
                    return employee.get_info()
        return "Employee not found"

    def get_course_students(self, course_name):
        for campus in [self.headquarters] + list(self.branch_campuses.values()):
            for course in campus.courses:
                if course.name == course_name:
                    return course.get_students()
        return "Course not found"

if __name__ == "__main__":
    institute = TrainingInstitute()

    # 添加学生
    student1 = institute.add_student("Alice", "1234567890", "八里台校区", "S001")
    student2 = institute.add_student("Bob", "0987654321", "津南校区", "S002")

    # 添加教师
    teacher1 = institute.add_teacher("Tom", "1111111111", "八里台校区", "T001")
    teacher2 = institute.add_teacher("Jerry", "2222222222", "泰达校区", "T002")

    # 添加课程
    course1 = institute.add_course("Math", 1000, "八里台校区")
    course2 = institute.add_course("Science", 1200, "津南校区")

    # 指定课程教师
    course1.assign_teacher(teacher1)
    course2.assign_teacher(teacher2)

    # 学生报名课程
    course1.enroll_student(student1)
    course2.enroll_student(student2)

    # 添加员工
    institute.add_employee("John", "E001", "八里台校区", "Support Staff")
    institute.add_employee("Mary", "E002", "津南校区", "Finance Staff")

    # 查看校区信息
    print(institute.get_campus_info("八里台校区"))
    print(institute.get_campus_info("津南校区"))

    # 查看学生信息
    print(institute.get_student_info("S001"))
    print(institute.get_student_info("S002"))

    # 查看教师信息
    print(institute.get_teacher_info("T001"))
    print(institute.get_teacher_info("T002"))

    # 查看员工信息
    print(institute.get_employee_info("E001"))
    print(institute.get_employee_info("E002"))

    # 查看课程学生列表
    print(institute.get_course_students("Math"))
    print(institute.get_course_students("Science"))