class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None
    
    def display_attributes(self):
        print(f"ID: {self.student_id}, Name: {self.student_name}, Class: {self.student_class}")

# Example usage
student = Student(1, "John Doe")
student.student_class = "10th Grade"
student.display_attributes()  # Output: ID: 1, Name: John Doe, Class: 10th Grade
