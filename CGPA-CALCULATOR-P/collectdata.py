class Student:
    def __init__(self, name="Anonymous", semester=0, sgpa=0.0):
        self.name = name
        self.sgpa = sgpa
        self.semester = semester
        
    def display(self):
        # Return string so it can be saved to a file
        return f"Name: {self.name}, Semester: {self.semester}, SGPA: {self.sgpa}\n"

class mark_view(Student):
    def __init__(self, name="Anonymous", semester=1, total_sgpa=0.0):
        super().__init__(name, semester, total_sgpa)
    
    def calculate_cgpa(self):
        if self.semester == 0:
            return 0
        cgpa = self.sgpa / self.semester
        print(f"CGPA for {self.name}: {cgpa:.2f}")
        return cgpa
