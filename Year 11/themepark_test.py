class Overall:

    def __init__(self):
        self.num_students = 0
        self.ticket_price = 30
        self.coach_price = 550
        self.max_students = 45
        self.all_students = []

    def inputNumStudents(self):
        self.num_students = int(input("How many students are going? "))
        return self.num_students

    def freeticket(self, num_students):
        self.num_freeticket = int(round(num_students/10))
        print(self.num_freeticket)
        return self.num_freeticket

    def add_student(self, student_class):
        self.all_students.append(student_class.firstname)
        return 
    
    def test_if_paid(self):
        for person in self.all_students:
             if person.paid == False:
                self.all_students.remove(person)
        return int(len(self.all_students) + 1)    # plus one because list starts at 0
 
    def __str__(self):
        self.num_students_paid = test_if_paid()
        self.freeticket(self.num_students_paid)
        self.discount = self.num_freeticket * self.ticker_price 
        self.total_cost = int(self.num_students_paid) * int(self.ticket_price) + self.coach_price - self.discount
        return f" {self.num_students} said they are going to the trip\n {self.num_students_paid} have paid\n You get {self.num_freeticket} free tickers\n Total cost is ${self.total_cost}"

class Student():
    def __init__(self, paid, firstname, lastname):
        self.paid = paid                                              # boolean value of true or false
        self.firstname = firstname
        self.lastname =  lastname

#input_error = "Invalid input"

# try:
#     print("")
# except Exception as input_error:
#     pass

trip_class = Overall()
trip_class.inputNumStudents()
# print(trip_class)

count = 0

while True:
    print("\nPress 1 to add students")
    print("Press 2 to update student")
    print("Press 3 to calculate final price")
    choice = str(input("Option: "))

    if choice == "1":
        while count <= 45 and count <= trip_class.num_students:
            print(f"You current have {count} student")
            if count <= trip_class.num_students:
                count += 1
            else:
                print("")
                break

            student_name = str(input(f"Input the full name of student {count}: "))
            first = student_name.split(" ")[0]
            last = student_name.split(" ")[1]

            student_paid = str(input("Paid? Y/N")).lower()
            if student_paid == "y":
                student_paid = True
            elif student_paid == "n":
                student_paid = False

            globals()[first] = Student(student_paid, first, last)
            print(f"{globals()[first].firstname}'s details updated")
            # globals()[first] dynamically creates a variable from the firstname

            trip_class.add_student(globals()[first])      #adds the student class to a list of other students

    elif choice == "2":
        update_name = input("Input the firstname of student you want to edit: ")
        
        student_paid = str(input("Paid? Y/N")).lower()
        if student_paid == "y":
            student_paid = True
        elif student_paid == "n":
            student_paid = False

        try:
            globals()[update_name] = Student(student_paid, globals()[update_name].firstname, globals()[update_name].lastname)
        except:
            print("Student does not exist")

    elif choice == "3":
        print(trip_class)


        