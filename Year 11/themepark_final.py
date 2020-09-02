import math

def test_int(n):
    try:
        int(n)
        pass
        return int(n)
    except (ValueError, SyntaxError):
        raise Exception("Invalid input")

class Overall:
    #TASK 1
    def __init__(self):
        self.num_students = 0
        self.ticket_price = 30
        self.coach_price = 550
        self.max_students = 45
        self.paid_students = []
        self.unpaid_students = []
        self.num_freeticket = 0

    #TASK 1
    def inputNumStudents(self):
        while True:
            try:
                self.num_students = int(input("How many are estimated to go? "))
                test_int(self.num_students)
                if self.num_students > 45:
                    print("Maximum of 45 participants")
                    continue
                else:
                    break
            except Exception:
                print("Invalid input")
                continue
        return self.num_students

    #TASK 1
    def calcCPC(self):  #CPC = Cost Per Student
        self.freeticket(self.num_students)
        self.cost_per_student = math.ceil((self.coach_price + ((self.num_students - self.num_freeticket) * self.ticket_price)) / self.num_students) #math.ceil to round up all the time
        print(f"The current cost per student is ${self.cost_per_student}")
        return self.cost_per_student

    #TASK 1
    def freeticket(self, n):
        try:
            self.num_freeticket = round(n/10)
            return self.num_freeticket
        except:
            print("No free tickets")  #returns the default value of 0

    #TASK 2
    def add_student(self, name, list_name):
        if int(len(list_name) + 1) <= 45:
            list_name.append(name)
        else:
            print("Maximum number of students")
        return list_name

    #TASK 3
    def calc_price(self):
        self.num_paid = len(self.paid_students) 
        self.freeticket(self.num_paid) # calculates number of free tickets
        self.discount = self.num_freeticket * self.ticket_price 
        self.total_cost = int(self.num_paid) * int(self.ticket_price) + self.coach_price - self.discount
        return self.total_cost

    #TASK 3  
    def __str__(self):   #does all the calculations of prices   
        self.calc_price()
        return f" {self.num_students} said they are going to the trip\n {self.num_paid} have paid\n You get {self.num_freeticket} free ticket\n Total cost is ${self.total_cost} (minus the cost of free tickets)"


trip_class = Overall()
trip_class.inputNumStudents()

trip_class.add_student("John", trip_class.paid_students)
trip_class.add_student("Hayden", trip_class.paid_students)
trip_class.add_student("Hayden", trip_class.paid_students)
trip_class.add_student("Hayden", trip_class.paid_students)
trip_class.add_student("Hayden", trip_class.paid_students)
trip_class.add_student("Hayden", trip_class.paid_students)
trip_class.add_student("Hayden", trip_class.paid_students)
trip_class.add_student("Hayden", trip_class.paid_students)
trip_class.add_student("Hayden", trip_class.paid_students)
trip_class.add_student("Hayden", trip_class.paid_students)
trip_class.add_student("Hayden", trip_class.paid_students)

trip_class.add_student("Kiran", trip_class.unpaid_students)

trip_class.calcCPC()
print(trip_class)
