import time

class CollegeEntity:
    clg_name = None
    clg_address = None

    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"{self.__class__.__name__}: {self.name}")

    @classmethod
    def college_info(cls, name, address) :
        cls.clg_name = name
        cls.clg_address = address
    
    @classmethod
    def get_college_info(cls) :
        print(f"College Name: {cls.clg_name}, College Address: {cls.clg_address}")
    


class Student:

    def __init__(self, student_id, name, course, year, expenses=0):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.year = year
        self.expenses = expenses

    def display_profile(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Course: {self.course}, Year: {self.year}")
    
    @staticmethod
    def add_student_database(db, student):
        db[student.student_id] = student.__dict__
        print(f"Student {student.name} added to database")

class Faculty:

    def __init__(self, faculty_id, name, department):
        self.faculty_id = faculty_id
        self.name = name
        self.department = department


    def display_profile(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Course: {self.course}, Year: {self.year}")
    
    @staticmethod
    def add_student_database(db, student):
        db[student.student_id] = student.__dict__
        print(f"Student {student.name} added to database")



class Club(CollegeEntity):
    def __init__(self, name, members=None):
        super().__init__(name)
        self.members = members if members else []

    def add_member(self, student):
        self.members.append(student)
        print(f"{student.name} added to club {self.name}")


class Department(CollegeEntity):
    def __init__(self, name):
        super().__init__(name)
    

class NNF(CollegeEntity):
    def __init__(self, name="Navchar Navyug Foundation"):
        super().__init__(name)
    


class Hostel(CollegeEntity):

    def __init__(self, name, rooms):
        super().__init__(name)
        self.rooms = rooms  # dict: {room_no: student}

    def vaccate_room(self, room_no):
        self.rooms[room_no] = []
    
    def add_room_members(self, room_no, *students):
        self.vaccate_room()
        self.rooms[room_no].extend(students)
        print(f"Room {room_no} in {self.name} allocated to {students}")
    
    def pay_fees(self, room_no, amount, db):
        if room_no in self.rooms:
            for student in self.rooms[room_no]:
                print("Paying Fees .....")
                db[student.student_id].expenses += amount
                time.sleep(1)
                print(f"Student {student.name} paid {amount} to {room_no} in {self.name}")
        else:
            print(f"Room {room_no} in {self.name} is not allocated")
    
    def get_roommates(self, room_no):
        ls = self.rooms[room_no] if room_no in self.rooms else []
        print(ls)

    def penalty(self, room_no, amount, db):
        if room_no in self.rooms:
            for student in self.rooms[room_no]:
                print("Penalty .....")
                db[student.student_id].expenses += amount
                time.sleep(1)
                print(f"Student {student.name} paid {amount} to {room_no} in {self.name} as penalty")


class Library(CollegeEntity):
    def __init__(self, name, books=None):
        super().__init__(name)
        self.books = books if books else {}  # dict: {book_title: count}

    def issue_book(self, title, student):
        if self.books.get(title, 0) > 0:
            self.books[title] -= 1
            print(f"{title} issued to {student.name}")
        else:
            print(f"{title} not available")
    


class AccountsDepartment(CollegeEntity):
    def __init__(self, name):
        super().__init__(name)
        self.fees_paid = {}

    def pay_fees(self, student, amount):
        self.fees_paid[student.student_id] = amount
        print(f"{student.name} paid ₹{amount}")
    



class Academic(CollegeEntity):
    def __init__(self, name):
        super().__init__(name)
        self.records = {}  # dict: {student_id: grades}

    def update_grades(self, student, grades):
        self.records[student.student_id] = grades
        print(f"{student.name}'s grades updated")


class Canteen(CollegeEntity):

    def __init__(self, name, menu):
        super().__init__(name)
        self.menu = menu  # dict: {item: price}

    def order_item(self, student, item):
        if item in self.menu:
            print(f"{student.name} ordered {item} for ₹{self.menu[item]}")
        else:
            print(f"{item} not available in canteen")

    def update_db(self, db) :
        db[self.name] = self.menu
        print(f"Canteen {db[self.name]} updated in database")
    
    def update_menu(self, db, item, price) :
        db[self.name].update({item:price})
        print(f"Menu updated in database")
        
    
    def request_item(self, item, price):
        print(f"Requested to add {item} add to canteen menu for ₹{price}...")
        time.sleep(2)
        self.menu[item] = price
        print("Request Approved")
    

if __name__ == "__main__":

    #Creating Databases
    student_db = {}
    hostel_db = {}
    canteen_db = {}

