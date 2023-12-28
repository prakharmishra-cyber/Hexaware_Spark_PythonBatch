from services.sis_manager import SISManager


def display_menu():
    print("\nStudent Information System (SIS) Menu:")
    print("1. Enroll Student in Course")
    print("2. Assign Teacher to Course")
    print("3. Record Payment")
    print("4. Get Payment Report")
    print("5. Get Enrollment Report")
    print("6. Calculate Course Statistics")
    print("7. Get Student by ID")
    print("8. Get Payment by ID")
    print("9. Get Course by ID")
    print("10. Get Enrollment by ID")
    print("11. Get Teacher by ID")
    print("0. Exit")

def get_user_input(prompt):
    return input(prompt).strip()

def main():
    sis_manager = SISManager()

    while True:
        display_menu()

        choice = get_user_input("Enter your choice (0-11): ")

        if choice == "0":
            print("Exiting the Student Information System. Goodbye!")
            break
        elif choice == "1":
            # Enroll Student in Course
            student_id = get_user_input("Enter student ID: ")
            course_id = get_user_input("Enter course ID: ")
            student = sis_manager.get_student_by_id(student_id)
            course = sis_manager.get_course_by_id(course_id)
            sis_manager.enroll_student_in_course(course, student)
        elif choice == "2":
            # Assign Teacher to Course
            teacher_id = get_user_input("Enter teacher ID: ")
            course_id = get_user_input("Enter course ID: ")
            teacher = sis_manager.get_teacher_by_id(teacher_id)
            course = sis_manager.get_course_by_id(course_id)
            sis_manager.assign_teacher_to_course(teacher, course)
        elif choice == "3":
            # Record Payment
            student_id = get_user_input("Enter student ID: ")
            amount = float(get_user_input("Enter payment amount: "))
            payment_date = get_user_input("Enter payment date (YYYY-MM-DD): ")
            student = sis_manager.get_student_by_id(student_id)
            sis_manager.record_payment(student, amount, payment_date)
        elif choice == "4":
            # Get Payment Report
            student_id = get_user_input("Enter student ID: ")
            student = sis_manager.get_student_by_id(student_id)
            sis_manager.get_payment_report(student)
        elif choice == "5":
            # Get Enrollment Report
            course_id = get_user_input("Enter course ID: ")
            course = sis_manager.get_course_by_id(course_id)
            sis_manager.get_enrollment_report(course)
        elif choice == "6":
            # Calculate Course Statistics
            course_id = get_user_input("Enter course ID: ")
            course = sis_manager.get_course_by_id(course_id)
            sis_manager.calculate_course_statistics(course)
        elif choice == "7":
            # Get Student by ID
            student_id = get_user_input("Enter student ID: ")
            student = sis_manager.get_student_by_id(student_id)
            print(student.display_student_info())
        elif choice == "8":
            # Get Payment by ID
            payment_id = get_user_input("Enter payment ID: ")
            payment = sis_manager.get_payment_by_id(payment_id)
            print(payment.display_payment_info())
        elif choice == "9":
            # Get Course by ID
            course_id = get_user_input("Enter course ID: ")
            course = sis_manager.get_course_by_id(course_id)
            print(course.display_course_info())
        elif choice == "10":
            # Get Enrollment by ID
            enrollment_id = get_user_input("Enter enrollment ID: ")
            enrollment = sis_manager.get_enrollment_by_id(enrollment_id)
            print(enrollment.display_enrollment_info())
        elif choice == "11":
            # Get Teacher by ID
            teacher_id = get_user_input("Enter teacher ID: ")
            teacher = sis_manager.get_teacher_by_id(teacher_id)
            print(teacher.display_teacher_info())
        else:
            print("Invalid choice. Please enter a number between 0 and 11.")

if __name__ == "__main__":
    main()
