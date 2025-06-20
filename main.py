import time

class CollegeEntity:
    clg_name = None
    clg_address = None
    std_db = {}

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

    def __init__(self, student_id, name, course, year):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.year = year

    def display_profile(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Course: {self.course}, Year: {self.year}")
    
    @staticmethod
    def add_student_database(clg, student):
        clg.std_db[student.student_id] = student.__dict__
        print(f"Student {student.name} added to database")



class Club(CollegeEntity):
    def __init__(self, name, members=None):
        super().__init__(name)
        self.members = members if members else []

    def add_member(self, student):
        self.members.append(student)
        print(f"{student.name} added to club {self.name}")


class Society(CollegeEntity):
    def __init__(self, name, activities=None):
        super().__init__(name)
        self.activities = activities if activities else []

    def add_activity(self, activity):
        self.activities.append(activity)


class Hostel(CollegeEntity):
    def __init__(self, name, rooms):
        super().__init__(name)
        self.rooms = rooms  # dict: {room_no: student}

    def pay_fees(self, student_id, *amount):
        if student_id in self.rooms:
            self.student = std_db.get(student_id)

    def vaccate_room(self, room_no):
        self.rooms[room_no] = []
    
    def add_roommates(self, room_no, *students):
        self.vaccate_room()
        self.rooms[room_no].extend(students)
        print(f"Room {room_no} in {self.name} allocated to {students}")
    
    def deduct_HMC
    


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
    
    def withdraw_name()


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
    
    def request_item(self, item, price):
        print(f"Requested to add {item} add to canteen menu for ₹{price}...")
        time.sleep(2)
        self.menu[item] = price
        print("Request Approved")
    



    


if __name__ == "__main__":

    #Declaring College
    college = College_Entity()
    # Creating student
    s1 = Student("S101", "Rudresh Dubey", "CSE", 1)
    s1.add_student_database()
    # Initializing systems
    lib = Library("Central Library", {"Python Book": 5})
    hostel = Hostel("Aryabhatt Hostel", {})
    canteen = Canteen("Main Canteen", {"Samosa": 10, "Chai": 5})
    accounts = AccountsDepartment("Accounts Office")
    academic = Academic("Academic Section")
    club = Club("Coding Club")
    society = Society("Drama Society")

    # Operations
    lib.issue_book("Python Book", s1)
    hostel.allocate_room("A-101", s1)
    canteen.order_item(s1, "Samosa")
    accounts.pay_fees(s1, 45000)
    academic.update_grades(s1, {"Math": "A", "Physics": "B+"})
    club.add_member(s1)
    society.add_activity("Stage Play")
    CollegeEntity.display_info()
