import time

def get_element_by_id(id, db):
    obj = db.get(id)
    if obj:
        return obj
    else:
        return None
    
def display_db(db) :
    for key, value in db.items():
        print(f"{key} : {value}")

class CollegeEntity:
    clg_name = None
    clg_address = None

    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"{self.__class__.__name__}: {self.name}")

    @classmethod
    def college_info(cls, name, address):
        cls.clg_name = name
        cls.clg_address = address

    @classmethod
    def get_college_info(cls):
        print(f"College Name: {cls.clg_name}, College Address: {cls.clg_address}")

class Student:

    def __init__(self, student_id, name, year, course, branch, fees=0):
        self.student_id = student_id
        self.name = name
        self.year = year
        self.course = course
        self.fees = fees
        self.branch = branch

    def display_profile(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Year: {self.year}, Course: {self.course}, Branch: {self.branch}")

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
        print(f"ID: {self.faculty_id}, Name: {self.name}, Department: {self.department}")

    @staticmethod
    def add_faculty_database(db, faculty):
        db[faculty.faculty_id] = faculty.__dict__
        print(f"Faculty {faculty.name} added to database")

class Club(CollegeEntity):

    CLUB_CATEGORIES = {
        "Cultural": {
            "Dance Club": ["Speakers"],
            "Singing Club": ["Mic", "Flute", "Tabla", "Microphones", "Guitar", "Electric Guitar", "Keyboard", "Drums"],
            "Drama Club": ["Props", "Costumes", "Lighting"],
            "Arts Club": ["Art Supplies", "Canvases", "Paints"],
            "Photography Club": ["Cameras", "Lenses", "Tripods"]
        },
        "Social": {
            "Parmarth": ["Stationery Kit"],
            "College Media Body Club": ["Cameras", "Mics"]
        },
        "Technical": {
            "Literature Club": ["Journals", "Books"],
            "Coding Club": ["Laptops", "Monitors", "Keyboards"]
        }
    }

    def __init__(self, name, treasurer, secretary, members):
        super().__init__(name)
        self.category, self.instruments = self._get_category_and_instruments(name)
        self.treasurer = treasurer
        self.secretary = secretary
        self.members = {}
        self.members.update(members)

    def _get_category_and_instruments(self, name):
        for category, clubs in Club.CLUB_CATEGORIES.items():
            if name in clubs:
                return category, clubs[name]
        raise ValueError(f"Club '{name}' not found in predefined categories")

    def add_member(self, student_id):
        if student_id in self.members:
            print(f"Student {student_id} is already a member of {self.name}")
        else:
            self.members[student_id] = get_element_by_id(student_id, student_db)

    def remove_member(self, student_id):
        if student_id in self.members:
            del self.members[student_id]
            print(f"Member {student_id} removed from club")
        else:
            print(f"Member {student_id} not found in club")

    def change_secretary(self, new_secretary):
        self.secretary = new_secretary
        print(f"Secretary changed to {new_secretary.name} for {self.name}")

    def change_treasurer(self, new_treasurer):
        self.treasurer = new_treasurer
        print(f"Treasurer changed to {new_treasurer.name} for {self.name}")

    def add_instrument(self, instrument):
        if instrument not in self.instruments:
            self.instruments.append(instrument)
            print(f"Instrument '{instrument}' added to {self.name}")

    def remove_instrument(self, instrument):
        if instrument in self.instruments:
            self.instruments.remove(instrument)
            print(f"Instrument '{instrument}' removed from {self.name}")

    def display_club_info(self):
        print(f"\nClub Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Treasurer: {self.treasurer.name}")
        print(f"Secretary: {self.secretary.name}")
        print(f"Instruments/Resources: {', '.join(self.instruments)}")
        print(f"Members Count: {len(self.members)}")
        for member in self.members:
            print(f" - {self.members[member].name} (ID: {self.members[member].student_id}, Dept: {self.members[member].branch})")

class Department(CollegeEntity):

    def __init__(self,id, name, courses, std, std_db, faculty, faculty_db):
        super().__init__(name)
        self.id = id
        self.courses = courses
        self.students = std
        self.std_db = std_db
        self.faculty = faculty
        self.faculty_db = faculty_db

    def organise_fest( self, fest_name, fest_date, fest_location, fest_budget, fest_members):
        self.fest_name = fest_name
        self.fest_date = fest_date
        self.fest_location = fest_location
        self.fest_budget = fest_budget
        self.fest_members = fest_members
        print(f"Organised {fest_name} on {fest_date} at {fest_location}")

class NNF(CollegeEntity):
    def __init__(self, name="Navchar Navyug Foundation"):
        super().__init__(name)
        self._chief_director = None
        self._startups = []
        self._past_events = []
        self._upcoming_events = []

    # Management
    @property
    def chief_director(self):
        return self._chief_director

    @chief_director.setter
    def chief_director(self, name):
        action = "assigned" if self._chief_director is None else "changed"
        self._chief_director = name
        print(f"Chief Director {action}: {name}")

    # Incubation Hub
    @property
    def startups(self):
        return self._startups

    def add_startup(self, name):
        self._startups.append(name)
        print(f"Startup '{name}' added to Incubation Hub")

    def list_startups(self):
        print("Incubated Startups:")
        for s in self._startups:
            print(f" - {s}")

    # Events
    @property
    def past_events(self):
        return self._past_events

    @property
    def upcoming_events(self):
        return self._upcoming_events

    def add_past_event(self, event):
        self._past_events.append(event)
        print(f"Past Event added: {event}")

    def schedule_event(self, event):
        self._upcoming_events.append(event)
        print(f"Upcoming Event scheduled: {event}")

    def remove_past_event(self, event):
        if event in self._past_events:
            self._past_events.remove(event)
            print(f"Past Event removed: {event}")

    def remove_upcoming_event(self, event):
        if event in self._upcoming_events:
            self._upcoming_events.remove(event)
            print(f"Upcoming Event removed: {event}")

    def show_all_events(self):
        print("\nPast Events:")
        for e in self._past_events:
            print(" - " + e)
        print("\nUpcoming Events:")
        for e in self._upcoming_events:
            print(" - " + e)

class Hostel(CollegeEntity):

    def __init__(self, name, rooms):
        super().__init__(name)
        self.rooms = rooms  # dict: {room_no: student}

    def vaccate_room(self, room_no):
        if room_no in self.rooms:
            del self.rooms[room_no]

    def add_room_members(self, room_no, *students):
        self.vaccate_room(room_no)
        self.rooms[room_no] = students
        print(f"Room {room_no} in {self.name} allocated to {[student.name for student in students]}")

    def pay_fees(self, room_no, amount, db):
        if room_no in self.rooms:
            for student in self.rooms[room_no]:
                print("Paying Fees .....")
                db[student.student_id].fees += amount
                time.sleep(1)
                print(f"Student {student.name} paid {amount} to {room_no} in {self.name}")
        else:
            print(f"Room {room_no} in {self.name} is not allocated")

    def get_roommates(self, room_no):
        ls = self.rooms[room_no] if room_no in self.rooms else []
        print([student.name for student in ls])

    def penalty(self, room_no, amount, db):
        if room_no in self.rooms:
            for student in self.rooms[room_no]:
                print("Penalty .....")
                db[student.student_id].fees += amount
                time.sleep(1)
                print(f"Student {student.name} paid {amount} to {room_no} in {self.name} as penalty")

class Library(CollegeEntity):

    def __init__(self, name, books=None):
        super().__init__(name)
        self.books = books if books else {}  # dict: {book_title: {rentable:count1, non_rentable:count2}}

    def add_rentable_book(self, book_title, count):
        if book_title in self.books:
            self.books[book_title]["rentable"] += count
        else:
            self.books[book_title] = {"rentable": count, "non_rentable": 0}

    def add_non_rentable_book(self, book_title, count):
        if book_title in self.books:
            self.books[book_title]["non_rentable"] += count
        else:
            self.books[book_title] = {"rentable": 0, "non_rentable": count}
    
    def remove_rentable_book(self, book_title, count):
        if book_title in self.books:
            if self.books[book_title]["rentable"] >= 0:
                self.books[book_title]["rentable"] -= count
            else:
                print(f"Book {book_title} is not available in {self.name}")
        else:
            print(f"Book {book_title} is not available in {self.name}")

    def remove_non_rentable_book(self, book_title, count):
        if book_title in self.books:
            if self.books[book_title]["non_rentable"] >= 0:
                self.books[book_title]["non_rentable"] -= count
            else:
                print(f"Book {book_title} is not available in {self.name}")
        else:
            print(f"Book {book_title} is not available in {self.name}")

    def issue_book(self, title, student):
        if title in self.books:
            if self.books[title]["rentable"] > 0:
                self.books[title]["rentable"] -= 1
                print(f"Book {title} issued to {student.name}")
        else:
            print(f"Book {title} is not available in {self.name}")

    
    def return_book(self, title, student):
        if title in self.books:
            self.books[title]["rentable"] += 1
            print(f"{title} returned by {student.name}")
        else:
            print("Updating Shelf....")
            time.sleep(1)
            self.books.update({title:{"rentable":1, "non_rentable":0}})
            print(f"{title} added to {self.name}. Shelf Updated")

    def update_db(self, db) :
        for book in self.books:
            db[book] = self.books[book]
            print(f"Database updated for {self.name}")

    
    @staticmethod
    def get_rentable_books(db) :
        rentable_db = {}
        for key, value in db.items():
            if value["rentable"] > 0 :
                rentable_db[key] = value["rentable"]
        return rentable_db

    @staticmethod
    def get_non_rentable_books(db) :
        non_rentable_db = {}
        for key, value in db.items():
            if value["non_rentable"] > 0 :
                non_rentable_db[key] = value["non_rentable"]
        return non_rentable_db


class AccountsDepartment(CollegeEntity):
    def __init__(self, name):
        super().__init__(name)
        self.fees_paid = {}

    def pay_fees(self, student, amount):
        self.fees_paid[student.student_id] = amount
        student.fees += amount
        print(f"{student.name} paid ₹{amount}")

class Academic(CollegeEntity):

    def __init__(self, name):
        super().__init__(name)
        self.records = {}  # dict: {student_id: grades}

    def assign_grade(self, faculty, student, year, semester, subject, grade):
        student_id = student.student_id

        if student_id not in self.records:
            self.records[student_id] = {}

        if year not in self.records[student_id]:
            self.records[student_id][year] = {}

        if semester not in self.records[student_id][year]:
            self.records[student_id][year][semester] = {}

        self.records[student_id][year][semester][subject] = grade
        print(f"Grade assigned to {student.name} in {subject} ({year} year, Sem {semester})")

    def view_grades(self, student):
        student_id = student.student_id

        print(f"\nGrades for {student.name} (ID: {student_id}):")

        if student_id not in self.records:
            print("No records found.")
            return

        for year in self.records[student_id]:
            print(f"Year {year}:")
            for semester in self.records[student_id][year]:
                print(f"  Semester {semester}:")
                for subject in self.records[student_id][year][semester]:
                    grade = self.records[student_id][year][semester][subject]
                    print(f"    {subject}: {grade}")

    def view_subject_grades(self, subject_name):
        print(f"\nGrades for Subject: {subject_name}")
        for student_id in self.records:
            for year in self.records[student_id]:
                for semester in self.records[student_id][year]:
                    sem_data = self.records[student_id][year][semester]
                    if subject_name in sem_data:
                        grade = sem_data[subject_name]
                        print(f"Student ID {student_id} - Year {year} Sem {semester}: {grade}")    

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

    def update_db(self, db):
        db[self.name] = self.menu
        print(f"Canteen {db[self.name]} updated in database")

    def update_menu(self, db, item, price):
        if self.name not in db:
            print(f"{self.name} not found in DB. Adding first...")
            self.update_db(db)
        db[self.name].update({item: price})
        print(f"Menu updated in database")


    def request_item(self, item, price):
        print(f"Requested to add {item} add to canteen menu for ₹{price}...")
        time.sleep(2)
        self.menu[item] = price
        print("Request Approved")

if __name__ == "__main__":

    # Creating Databases
    faculty_db = {}
    student_db = {}
    hostel_db = {}
    canteen_db = {}
    department_db = {}
    library_db = {}

    # 1. College Info Setup
    CollegeEntity.college_info("Institute of Engineering and Technology, Lucknow", "Sitapur Road, Lucknow")
    CollegeEntity.get_college_info()

    # 2. Creating Students
    s1 = Student("S101", "Amit Sharma", 2, "B.Tech", "Computer Science")
    s2 = Student("S102", "Riya Verma", 3, "B.Tech", "Electronics")
    s3 = Student("S103", "Manish Kumar", 1, "B.Tech", "Mechanical")

    # 3. Adding Students to Database
    student_db[s1.student_id] = s1
    student_db[s2.student_id] = s2
    student_db[s3.student_id] = s3


    # 4. Display Student Profiles
    s1.display_profile()
    s2.display_profile()
    s3.display_profile()

    # 5. Creating Faculty
    f1 = Faculty("F201", "Dr. Anil Singh", "Computer Science")
    f2 = Faculty("F202", "Prof. Neha Agarwal", "Electronics")

    # 6. Adding Faculty to Database
    faculty_db[f1.faculty_id] = f1
    faculty_db[f2.faculty_id] = f2

    # 7. Display Faculty
    f1.display_profile()
    f2.display_profile()

    # 8. Creating Department
    cse_dept = Department("D01", "Computer Science", ["B.Tech", "M.Tech"], [s1], student_db, [f1], faculty_db)
    cse_dept.organise_fest("TechX", "20 Aug 2025", "Auditorium", 50000, ["Amit Sharma", "Team TechX"])

    # 9. Creating and Managing Club
    dance_club = Club("Dance Club", s1, s2, {})
    dance_club.add_member("S101")
    dance_club.add_member("S102")
    dance_club.add_instrument("DJ Console")
    dance_club.remove_member("S102")
    dance_club.change_secretary(s3)
    dance_club.display_club_info()

    # 10. Hostel Management
    rooms = {
        "101": [],
        "102": []
    }
    hostel = Hostel("Aryabhatt Hostel", rooms)
    hostel.add_room_members("101", s1, s3)
    hostel.get_roommates("101")
    hostel.pay_fees("101", 15000, student_db)
    hostel.penalty("101", 500, student_db)
    hostel.vaccate_room("101")
    hostel.get_roommates("101")

    # 11. Library Management
    library = Library("Central Library", {
        "Python Programming": {"rentable": 2, "non_rentable": 1},
        "Digital Logic": {"rentable": 1, "non_rentable": 2}
    })

    library.add_rentable_book('Quantum Physics', 3)
    library.add_non_rentable_book('Artificial Intelligence', 2)
    library.update_db(library_db)

    rentable_books = Library.get_rentable_books(library.books)
    non_rentable_books = Library.get_non_rentable_books(library.books)
    print("\nAvailable Rentable Books:")
    display_db(rentable_books)
    print("\nAvailable Non-Rentable Books:")
    display_db(non_rentable_books)

    library.issue_book("Python Programming", s1)
    library.return_book("Python Programming", s1)

    # 12. Accounts Department
    accounts = AccountsDepartment("Accounts")
    accounts.pay_fees(s1, 10000)
    accounts.pay_fees(s2, 12000)

    # 13. Academic Records
    academic = Academic("Academic Block")
    academic.assign_grade(f1, s1, 2, 1, "Data Structures", "A")
    academic.assign_grade(f1, s1, 2, 1, "OOP", "B+")
    academic.assign_grade(f2, s1, 2, 1, "Signals", "A")  # Department mismatch
    academic.view_grades(s1)
    academic.view_subject_grades("Data Structures")

    # 14. Canteen Management
    canteen = Canteen("IET Cafeteria", {"Chowmein": 40, "Coffee": 20})
    canteen.order_item(s2, "Coffee")
    canteen.order_item(s3, "Pizza")  # Not available
    canteen.request_item("Pizza", 80)
    canteen.order_item(s3, "Pizza")
    canteen.update_db(canteen_db)
    canteen.update_menu(canteen_db, "Sandwich", 30)
    canteen.update_db(canteen_db)

    # 15. NNF Functionality
    nnf = NNF()
    nnf.chief_director = "Mr. Rajeev Tiwari"
    nnf.add_startup("GreenTech Solutions")
    nnf.add_startup("EduSpark")
    nnf.add_past_event("Hackathon 2023")
    nnf.schedule_event("Startup Meet 2025")
    nnf.remove_past_event("Hackathon 2023")
    nnf.remove_upcoming_event("Startup Meet 2025")
    nnf.show_all_events()

