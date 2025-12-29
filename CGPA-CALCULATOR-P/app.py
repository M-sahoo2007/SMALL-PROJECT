# from collectdata import *

# def calculate():
#     name = input("Enter your name: ")
#     sgpa = float(input("Enter your SGPA sum: "))
#     semester = int(input("Enter your Total Semesters: "))
    
#     # 1. Create an instance of mark_view (the subclass)
#     mark = mark_view(name, semester, sgpa)
    
#     # 2. Call the method on the object 'mark'
#     mark.calculate_cgpa()
    
#     print("Output is Successful!")
    
#     # 3. Save to file
#     # Use raw string r"" or forward slashes to avoid path errors on Windows
#     file_path = r"D:\pratic\python\CGPA-CALCULATOR\data.txt"
#     with open(file_path, "a+") as f:
#         f.write(mark.display("\n"))

# while True:
#     print("\n1. Calculate CGPA")
#     print("2. Exit")
#     choice = input("Enter Your choice: ")
    
#     if choice == '1':
#         calculate()
#     elif choice == '2':
#         break
#     else:
#         print("Invalid Choice")
#         print()

from flask import Flask, render_template, request
from collectdata import mark_view

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    cgpa = None
    name = ""

    if request.method == "POST":
        name = request.form["name"]
        sgpa = float(request.form["sgpa"])
        semester = int(request.form["semester"])

        mark = mark_view(name, semester, sgpa)
        cgpa = mark.calculate_cgpa()

        with open("CGPA-CALCULATOR-P\data.txt", "a+") as f:
            f.write(f"Name: {name}, Semester: {semester},Sgpa:{sgpa} CGPA: {cgpa}\n")

    return render_template("index.html", cgpa=cgpa, name=name)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=7860)
