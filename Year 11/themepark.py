import jsonpickle as jp

loop = True
all_students = []

#use generators
# global python

class Overall:
    def __init__(self):
        self.num_students = 0
        self.ticket_price = 30
        self.coach_price = 550
        self.max_students = 45

    def inputNumStudents(self):
        self.num_students = int(input("How many students are going?"))
        return self.num_students

    def freeticket(self, num_students):
        self.num_freeticket = int(round(num_students/10))
        print(self.num_freeticket)
        return self.num_freeticket

    def __str__(self):
        self.freeticket(self.num_students)
        return f" {self.num_students} are going to the trip\n The ticket price is {self.ticket_price}\n You get {self.num_freeticket} free tickers"

class Student():
    def __init__(self, paid, firstname, lastname):
        paid = False
        self.paid = paid                                              # boolean value of true or false
        self.firstname = firstname
        self.lastname =  lastname

def test(number):
    data_type = type(number)
    if data_type == int or data_type == float:
        pass
    else:
        global loop
        loop = False
        return loop


trip_class = Overall()
trip_class.inputNumStudents()
print(trip_class)

person = Student(False,"Hayden","So")
# person_json = jsonpickle.encode(person)
# print(person_json)
