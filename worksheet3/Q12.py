class StringManipulator:
    def __init__(self):
        self.s = ""
    
    def get_string(self):
        self.s = input("Enter a string: ")
    
    def print_string(self):
        print(self.s.upper())

# Example usage
string_manipulator = StringManipulator()
string_manipulator.get_string()
string_manipulator.print_string()
