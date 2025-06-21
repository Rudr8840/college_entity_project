# 🎓 College Entity Management System (Python CLI Project)

This Python-based CLI project simulates a complete **college ecosystem**, providing functionalities for managing:

- Students & Faculty
- Departments & Events
- Clubs (Cultural, Social, Technical)
- Hostel Allocation & Fee Management
- Library Book Management
- Canteen Menu and Order System
- Academic Records (Grades)
- Accounts Department (Fee Records)
- Incubation Cell (NNF)
- And more...

---

## 🔧 Features

### 🧑‍🎓 Students & Faculty
- Add and display student & faculty profiles
- Maintain centralized databases
- Assign branches, courses, and departments

### 🏢 Departments
- Organize fests and academic activities
- Manage faculty and student associations

### 🎭 Clubs
- Auto-detect category & resources based on club name
- Add/Remove members
- Change Treasurer/Secretary
- Add/Remove instruments/resources

### 🏠 Hostels
- Assign rooms to multiple students
- Collect fees and apply penalties
- Manage room vacancies

### 📚 Library
- Track rentable and non-rentable books
- Issue and return books
- Auto-update shelf when new books are returned
- Display rentable and non-rentable inventory

### 🧾 Accounts Department
- Track and update fee payments per student

### 🎓 Academic Block
- Assign grades by semester, subject, and year
- View complete student-wise and subject-wise report cards

### 🍽️ Canteen
- Handle food orders
- Update menu and manage inventory
- Request new food items

### 🚀 Navchar Navyug Foundation (NNF)
- Manage Chief Director
- Incubate startups
- Record past and upcoming events

---

## 🖥️ Sample CLI Output

```bash

College Name: Institute of Engineering and Technology, Lucknow, College Address: Sitapur Road, Lucknow
ID: S101, Name: Amit Sharma, Year: 2, Course: B.Tech, Branch: Computer Science
ID: S102, Name: Riya Verma, Year: 3, Course: B.Tech, Branch: Electronics
ID: S103, Name: Manish Kumar, Year: 1, Course: B.Tech, Branch: Mechanical
ID: F201, Name: Dr. Anil Singh, Department: Computer Science
ID: F202, Name: Prof. Neha Agarwal, Department: Electronics
Organised TechX on 20 Aug 2025 at Auditorium
Instrument 'DJ Console' added to Dance Club
Member S102 removed from club
Secretary changed to Manish Kumar for Dance Club

Club Name: Dance Club
Category: Cultural
Treasurer: Amit Sharma
Secretary: Manish Kumar
Instruments/Resources: Speakers, DJ Console
Members Count: 1
 - Amit Sharma (ID: S101, Dept: Computer Science)
Room 101 in Aryabhatt Hostel allocated to ['Amit Sharma', 'Manish Kumar']
(<__main__.Student object at 0x000001EB07783B60>, <__main__.Student object at 0x000001EB07783BC0>)
Paying Fees .....
Student Amit Sharma paid 15000 to 101 in Aryabhatt Hostel
Paying Fees .....
Student Manish Kumar paid 15000 to 101 in Aryabhatt Hostel
Penalty .....
Student Amit Sharma paid 500 to 101 in Aryabhatt Hostel as penalty
Penalty .....
Student Manish Kumar paid 500 to 101 in Aryabhatt Hostel as penalty
[]
Database updated for Central Library
Database updated for Central Library
Database updated for Central Library
Database updated for Central Library

Available Rentable Books:
Python Programming : 2
Digital Logic : 1
Quantum Physics : 3

Available Non-Rentable Books:
Python Programming : 1
Digital Logic : 2
Artificial Intelligence : 2
Book Python Programming issued to Amit Sharma
Python Programming returned by Amit Sharma
Amit Sharma paid ₹10000
Riya Verma paid ₹12000
Grade assigned to Amit Sharma in Data Structures (2 year, Sem 1)
Grade assigned to Amit Sharma in OOP (2 year, Sem 1)
Grade assigned to Amit Sharma in Signals (2 year, Sem 1)

Grades for Amit Sharma (ID: S101):
Year 2:
  Semester 1:
    Data Structures: A
    OOP: B+
    Signals: A

Grades for Subject: Data Structures
Student ID S101 - Year 2 Sem 1: A
Riya Verma ordered Coffee for ₹20
Pizza not available in canteen
Requested to add Pizza add to canteen menu for ₹80...
Request Approved
Manish Kumar ordered Pizza for ₹80
Canteen {'Chowmein': 40, 'Coffee': 20, 'Pizza': 80} updated in database
Menu updated in database
Canteen {'Chowmein': 40, 'Coffee': 20, 'Pizza': 80, 'Sandwich': 30} updated in database
Chief Director assigned: Mr. Rajeev Tiwari
Startup 'GreenTech Solutions' added to Incubation Hub
Startup 'EduSpark' added to Incubation Hub
Past Event added: Hackathon 2023
Upcoming Event scheduled: Startup Meet 2025
Past Event removed: Hackathon 2023
Upcoming Event removed: Startup Meet 2025

Past Events:

Upcoming Events:
PS C:\Users\stddu\Downloads\VRACKS> python -u "c:\Users\stddu\Downloads\VRACKS\College_Entity_Project\main.py"
College Name: Institute of Engineering and Technology, Lucknow, College Address: Sitapur Road, Lucknow
ID: S101, Name: Amit Sharma, Year: 2, Course: B.Tech, Branch: Computer Science
ID: S102, Name: Riya Verma, Year: 3, Course: B.Tech, Branch: Electronics
ID: S103, Name: Manish Kumar, Year: 1, Course: B.Tech, Branch: Mechanical
ID: F201, Name: Dr. Anil Singh, Department: Computer Science
ID: F202, Name: Prof. Neha Agarwal, Department: Electronics
Organised TechX on 20 Aug 2025 at Auditorium
Instrument 'DJ Console' added to Dance Club
Member S102 removed from club
Secretary changed to Manish Kumar for Dance Club

Club Name: Dance Club
Category: Cultural
Treasurer: Amit Sharma
Secretary: Manish Kumar
Instruments/Resources: Speakers, DJ Console
Members Count: 1
 - Amit Sharma (ID: S101, Dept: Computer Science)
Room 101 in Aryabhatt Hostel allocated to ['Amit Sharma', 'Manish Kumar']
Traceback (most recent call last):
  File "c:\Users\stddu\Downloads\VRACKS\College_Entity_Project\main.py", line 497, in <module>
    hostel.get_roommates("101")
  File "c:\Users\stddu\Downloads\VRACKS\College_Entity_Project\main.py", line 255, in get_roommates
    print({[student.name for student in ls]})
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'list'
PS C:\Users\stddu\Downloads\VRACKS> python -u "c:\Users\stddu\Downloads\VRACKS\College_Entity_Project\main.py"
College Name: Institute of Engineering and Technology, Lucknow, College Address: Sitapur Road, Lucknow
ID: S101, Name: Amit Sharma, Year: 2, Course: B.Tech, Branch: Computer Science
ID: S102, Name: Riya Verma, Year: 3, Course: B.Tech, Branch: Electronics
ID: S103, Name: Manish Kumar, Year: 1, Course: B.Tech, Branch: Mechanical
ID: F201, Name: Dr. Anil Singh, Department: Computer Science
ID: F202, Name: Prof. Neha Agarwal, Department: Electronics
Organised TechX on 20 Aug 2025 at Auditorium
Instrument 'DJ Console' added to Dance Club
Member S102 removed from club
Secretary changed to Manish Kumar for Dance Club

Club Name: Dance Club
Category: Cultural
Treasurer: Amit Sharma
Secretary: Manish Kumar
Instruments/Resources: Speakers, DJ Console
Members Count: 1
 - Amit Sharma (ID: S101, Dept: Computer Science)
Room 101 in Aryabhatt Hostel allocated to ['Amit Sharma', 'Manish Kumar']
['Amit Sharma', 'Manish Kumar']
Paying Fees .....
Student Amit Sharma paid 15000 to 101 in Aryabhatt Hostel
Paying Fees .....
Student Manish Kumar paid 15000 to 101 in Aryabhatt Hostel
Penalty .....
Student Amit Sharma paid 500 to 101 in Aryabhatt Hostel as penalty
Penalty .....
Student Manish Kumar paid 500 to 101 in Aryabhatt Hostel as penalty
[]
Database updated for Central Library
Database updated for Central Library
Database updated for Central Library
Database updated for Central Library

Available Rentable Books:
Python Programming : 2
Digital Logic : 1
Quantum Physics : 3

Available Non-Rentable Books:
Python Programming : 1
Digital Logic : 2
Artificial Intelligence : 2
Book Python Programming issued to Amit Sharma
Python Programming returned by Amit Sharma
Amit Sharma paid ₹10000
Riya Verma paid ₹12000
Grade assigned to Amit Sharma in Data Structures (2 year, Sem 1)
Grade assigned to Amit Sharma in OOP (2 year, Sem 1)
Grade assigned to Amit Sharma in Signals (2 year, Sem 1)

Grades for Amit Sharma (ID: S101):
Year 2:
  Semester 1:
    Data Structures: A
    OOP: B+
    Signals: A

Grades for Subject: Data Structures
Student ID S101 - Year 2 Sem 1: A
Riya Verma ordered Coffee for ₹20
Pizza not available in canteen
Requested to add Pizza add to canteen menu for ₹80...
Request Approved
Manish Kumar ordered Pizza for ₹80
Canteen {'Chowmein': 40, 'Coffee': 20, 'Pizza': 80} updated in database
Menu updated in database
Canteen {'Chowmein': 40, 'Coffee': 20, 'Pizza': 80, 'Sandwich': 30} updated in database
Chief Director assigned: Mr. Rajeev Tiwari
Startup 'GreenTech Solutions' added to Incubation Hub
Startup 'EduSpark' added to Incubation Hub
Past Event added: Hackathon 2023
Upcoming Event scheduled: Startup Meet 2025
Past Event removed: Hackathon 2023
Upcoming Event removed: Startup Meet 2025

Past Events:

Upcoming Events:
