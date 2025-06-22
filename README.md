---
### College Management System

This Python project provides a foundational **College Management System**, simulating various interconnected entities within a higher education institution. It's designed to illustrate object-oriented programming concepts and demonstrate how different components of a college interact.

---
## Features

The system models key aspects of a college, including:

* **College Information:** Centralized storage for college-wide details like name and address.
* **Academic Structure:**
    * **Courses:** Define various academic programs (e.g., B.Tech, M.Tech, PhD).
    * **Departments:** Manage different academic departments, listing their associated courses, students, and faculty. Departments can also organize fests.
    * **Academic Records:** Track and manage student grades across different years, semesters, and subjects.
* **People Management:**
    * **Students:** Store comprehensive student profiles, including ID, roll number, name, year, course, branch, contact information, and fees.
    * **Faculty:** Maintain faculty details such as ID, name, department, and contact information.
* **Student Life & Activities:**
    * **Clubs:** Create and manage various student clubs (Cultural, Social, Technical) with their treasurers, secretaries, members, and specific instruments/resources.
    * **Societies:** Organize departmental and non-departmental societies, managing their heads, coordinators, members, and volunteers.
* **Campus Facilities:**
    * **Hostel:** Manage hostel rooms, assign students to rooms, handle fee payments, and apply penalties.
    * **Library:** Maintain a catalog of rentable and non-rentable books, allowing students to issue and return books.
    * **Canteen:** Manage a menu and process student orders. New items can be requested and added to the menu.
* **Financial & Administrative:**
    * **Accounts Department:** Process and record student fee payments.
* **Innovation & Entrepreneurship:**
    * **Navchar Navyug Foundation (NNF):** Represents an incubation hub, overseeing a chief director, managing incubated startups, and scheduling/tracking events.

---
## Code Structure

The Python code is organized into several classes, each representing a distinct entity or department within the college system.

* **`CollegeEntity`**: A base class for common attributes and methods shared by various college components (e.g., `clg_name`, `clg_address`, `display_info`).
* **`Course`**: Represents academic courses with `course_id` and `course_name`.
* **`Student`**: Manages student details including `student_id`, `roll_no`, `name`, `year`, `course`, `branch`, `phone`, `email`, and `fees`.
* **`Faculty`**: Handles faculty information such as `faculty_id`, `name`, `department`, `phone`, and `email`.
* **`Club`**: Extends `CollegeEntity` and manages club-specific attributes like `category`, `instruments`, `treasurer`, `secretary`, and `members`. Includes methods for adding/removing members and instruments, and changing office bearers.
* **`Society`**: Extends `CollegeEntity` and categorizes societies as "Departmental" or "Non-Departmental". Manages `head`, `coordinator`, `members`, and `volunteers`.
* **`Department`**: Extends `CollegeEntity` and represents academic departments. It holds lists of `courses`, `students`, and `faculty` associated with it, and can `organise_fest`.
* **`NNF`**: Extends `CollegeEntity` for the "Navchar Navyug Foundation". Manages a `chief_director`, `startups`, `past_events`, and `upcoming_events`.
* **`Hostel`**: Extends `CollegeEntity` to manage hostel `rooms`, `add_room_members`, `vaccate_room`, `pay_fees`, `get_roommates`, and apply `penalty`.
* **`Library`**: Extends `CollegeEntity` to manage `books` (rentable and non-rentable), `add`/`remove` books, `issue_book`, `return_book`, and `update_db`. It also provides static methods to get `rentable_books` and `non_rentable_books`.
* **`AccountsDepartment`**: Extends `CollegeEntity` and handles `pay_fees` for students.
* **`Academic`**: Extends `CollegeEntity` and manages student `records` for grades. It allows `assign_grade`, `view_grades`, `view_subject_grades`, and `update_grades`.
* **`Canteen`**: Extends `CollegeEntity` and manages the canteen `menu`. It supports `order_item`, `update_db`, `update_menu`, and `request_item`.
* **Global Functions:**
    * `get_element_by_id(id, db)`: Retrieves an element from a given database by its ID.
    * `display_db(db)`: Prints the key-value pairs of a given database.
* **`if __name__ == "__main__":` block**: This section demonstrates the practical usage of all classes and their methods, setting up initial data and performing various operations to showcase the system's functionalities. It initializes in-memory dictionaries (`faculty_db`, `student_db`, etc.) to simulate databases.

---
## ER Diagram (`ER Diagram portrait 1.pdf`)

The provided `ER Diagram portrait 1.pdf` visually represents the entities within the college management system and the relationships between them.

* **Entities:** Rectangles in the diagram represent entities such as `College`, `Faculty`, `Course`, `Student`, `Club`, `Society`, `Department`, `NNF`, `Hostel`, `Library`, `Accounts Department`, `Academic`, and `Canteen`. Each entity corresponds to a class in the Python code.
* **Attributes:** Ovals connected to entities represent their attributes (e.g., `name`, `id`, `address`, `phone`, `email`, `fees`, `category`, `instruments`, `head`, `coordinator`, `rooms`, `books`, `menu`, `records`, `startups`, `events`).
* **Relationships:** Diamonds represent relationships between entities, indicating how they interact (e.g., a `College` *has* `Departments`, `Students` *enrolls in* `Courses`, `Faculty` *teaches* `Subjects` in a `Department`, `Students` *are members of* `Clubs` and `Societies`, `Students` *reside in* `Hostels`, `Students` *issue* `Books` from the `Library`, `Accounts Department` *processes* `Fees`, `Academic` *manages* `Grades`, `Canteen` *serves* `Food Items`, `NNF` *incubates* `Startups`).
* **Cardinality:** Lines connecting entities to relationships, often with symbols (e.g., single line for one, double line for many, or specific notations), illustrate the cardinality of the relationships (e.g., one-to-many, many-to-many).

The ER Diagram serves as a blueprint for the database schema, illustrating how the data is structured and interconnected, which is reflected in the Python classes and their interactions.

---
## Getting Started

To run this project:

1.  **Save the code:** Copy the entire provided Python code into a file named `college_management.py`.
2.  **View ER Diagram:** Open the `ER Diagram portrait 1.pdf` file to understand the system's data model.
3.  **Run from terminal:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run:
    ```bash
    python college_management.py
    ```

The output in the console will demonstrate the various operations and interactions within the college management system as defined in the `if __name__ == "__main__":` block.

---
## Further Enhancements (Potential Improvements)

This project provides a basic framework. Here are some ideas for expansion:

* **Persistent Data Storage:** Integrate with a real database (SQLite, PostgreSQL, MongoDB) to store data persistently, following the structure depicted in the ER Diagram.
* **User Interface:** Develop a command-line interface (CLI) or a graphical user interface (GUI) using libraries like `Tkinter`, `PyQt`, or `Streamlit` for better user interaction.
* **Error Handling:** Implement more robust error handling for various scenarios (e.g., invalid inputs, non-existent IDs).
* **Search and Filter:** Add more sophisticated search and filtering capabilities for students, faculty, books, etc.
* **Reporting:** Generate reports (e.g., student transcripts, club member lists, financial summaries).
* **Authentication and Authorization:** Implement user roles (admin, student, faculty) with different access levels.
* **Modularization:** Break down the code into multiple files for larger, more complex systems.
* **Event Management:** Expand event management for departments, clubs, and NNF with details like participation, registration, and resources.

Feel free to explore and modify the code to add new features or refine existing ones!
---

---

## 🛠 How to Run

1. Clone this repo or download the Python file and SVG.
2. Make sure Python 3 is installed.
3. Run:

```bash
python main.py


College Name: Institute of Engineering and Technology, Lucknow, College Address: Sitapur Road, Lucknow
ID: S101, Roll No: 2021CS101, Name: Amit Sharma, Year: 2, Course: B.Tech, Branch: Computer Science and Engineering, Phone: 9000000001, Email: amit@college.edu
ID: S102, Roll No: 2020EC102, Name: Riya Verma, Year: 3, Course: B.Tech, Branch: Electronics, Phone: 9000000002, Email: riya@college.edu
ID: S103, Roll No: 2022ME103, Name: Manish Kumar, Year: 1, Course: B.Tech, Branch: Mechanical, Phone: 9000000003, Email: manish@college.edu
ID: F201, Name: Dr. Anil Singh, Department: Computer Science and Engineering, Phone: 8000000001, Email: anil@college.edu
ID: F202, Name: Prof. Neha Agarwal, Department: Electronics, Phone: 8000000002, Email: neha@college.edu
Organised TechX on 20 Aug 2025 at Auditorium
Student S101 added to Dance Club
Student S102 added to Dance Club
Instrument 'DJ Console' added to Dance Club
Member S102 removed from club
Secretary changed to Manish Kumar for Dance Club

Club Name: Dance Club
Category: Cultural
Treasurer: Amit Sharma
Secretary: Manish Kumar
Instruments/Resources: Speakers, DJ Console
Members Count: 1
 - Amit Sharma (ID: S101, Dept: Computer Science and Engineering, Roll No: 2021CS101)
Amit Sharma added to society SAE
Volunteer Riya Verma from Electronics added to SAE

Society: SAE (Departmental)
Head: Dr. Rakesh Kumar
Coordinator: Neha Agarwal
Members (1):
  - Amit Sharma (ID: S101, Dept: Computer Science and Engineering)
Volunteers (1):
  - Riya Verma (ID: S102, Dept: Electronics)
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

Grades for Amit Sharma (ID: S101, Roll No: 2021CS101):
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

