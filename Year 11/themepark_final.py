class Overall:

    def __init__(self):
        self.num_students = 0
        self.ticket_price = 30
        self.coach_price = 550
        self.max_students = 45
        self.paid_students = []
        self.unpaid_students = []

    def inputNumStudents(self):
        while True:
            self.num_students = int(input("How many are estimated to go? "))
            if self.num_students > 45:
                print("Maximum of 45 participants")
                continue
            else:
                break
        return self.num_students

    def calcCPC(self, freeticket=None):  #=None makes the parameter optional
        self.cost_per_student = self.coach_price/self.num_students + self.ticket_price

    def freeticket(self, num_students):
        self.num_freeticket = int(round(num_students/10))
        print(self.num_freeticket)
        return self.num_freeticket

    def add_paid_student(self, name):
        if int(len(self.paid_students) + 1) <= 45:
            self.paid_student.append(name)
        return self.paid_student
            
    def __str__(self):   #does all the calculations of prices 
        self.num_students_paid = len(self.paid_students) + 1
        self.freeticket(self.num_students_paid) # calculates number of free tickers
        self.discount = self.num_freeticket * self.ticket_price 
        self.total_cost = int(self.num_students_paid) * int(self.ticket_price) + self.coach_price - self.discount
        return f" {self.num_students} said they are going to the trip\n {self.num_students_paid} have paid\n You get {self.num_freeticket} free tickers\n Total cost is ${self.total_cost} (minus the cost of free tickets)"

#input_error = "Invalid input"

# try:
#     print("")
# except Exception as input_error:
#     pass

trip_class = Overall()
trip_class.inputNumStudents()

