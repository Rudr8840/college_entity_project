# College Entity Management System 🏫

## Overview

This Python-based object-oriented system simulates a complete **college ecosystem**, including student records, faculty management, societies, clubs, hostels, library, academics, and more.

It also includes an **Entity Relationship Diagram** (ERD) to represent the data structure visually — `ER.drawio.svg` (included).

---

## 📘 Contents

1. [Project Features](#-project-features)
2. [Modules / Classes](#-modules--classes)
3. [Usage & Simulation](#-usage--simulation)
4. [Entity-Relationship Diagram](#-entity-relationship-diagram)
5. [How to Run](#-how-to-run)

---

## 🔧 Project Features

- ✅ Create and manage **students**, **faculty**, and **departments**
- 🧾 Manage **academic records** and **grades**
- 📚 Handle **library books** with rentable/non-rentable logic
- 💰 Track **fees payments** via hostel or accounts department
- 🏘️ Allocate hostel rooms and charge penalties
- 🍴 Manage canteen menu and requests
- 🎭 Handle college **clubs**, **societies**, and their resources
- 🚀 Simulate an **incubation foundation** with startup and event tracking

---

## 🏗 Modules / Classes

### 🔹 `CollegeEntity`
Base class for all college-related entities. Stores college name and address.

### 🔹 `Student` / `Faculty`
- Contains personal and academic details
- Faculty can assign grades

### 🔹 `Club`
- Categorized as Cultural, Social, or Technical
- Manages treasurer, secretary, members, and instruments

### 🔹 `Society`
- Classified as Departmental or Non-Departmental
- Tracks head, coordinator, members, and volunteers

### 🔹 `Department`
- Organizes departmental fests
- Stores associated students and faculty

### 🔹 `Hostel`
- Allocates rooms to students
- Handles rent payment and penalties

### 🔹 `Library`
- Tracks books: rentable and non-rentable
- Issues and returns books, updates database

### 🔹 `AccountsDepartment`
- Handles fee payments directly from students

### 🔹 `Academic`
- Manages and views student grades across years and semesters

### 🔹 `Canteen`
- Offers a menu system with order, update, and item request features

### 🔹 `NNF (Navchar Navyug Foundation)`
- Incubation platform for student startups
- Tracks startup list, past events, and upcoming events

---

## ▶️ Usage & Simulation

The `__main__` block contains a **full simulation** of how the system works:

- Students and faculty are created and added to databases.
- Clubs and societies are formed with members and volunteers.
- Hostel rooms are allocated, fees and penalties charged.
- Library books are issued and returned.
- Events and startups are managed under NNF.
- Grade assignment and subject-wise viewing is supported.

This block acts as a demo and test for each class.

---

## 🗺 Entity-Relationship Diagram

The file **`ER.drawio.svg`** attached in this project illustrates the ER structure visually.

### ✅ Key Elements

- `Student`, `Faculty`, `Club`, `Society`, etc. are connected as entities
- Relationships like *“has”*, *“manages”*, *“organizes”* are shown
- Attributes like `student_id`, `fees`, `instruments` are marked
- Inheritance (e.g., `Club`, `Society`, `Department` from `CollegeEntity`) is displayed

> 📎 You can open the SVG file in any browser or ER viewer to explore the architecture.

---

## 🛠 How to Run

1. Clone this repo or download the Python file and SVG.
2. Make sure Python 3 is installed.
3. Run:

```bash
python main.py



College Name: Institute of Engineering and Technology, Lucknow, College Address: Sitapur Road, Lucknow
ID: S101, Name: Amit Sharma, Year: 2, Course: B.Tech, Branch: Computer Science, Phone: 9000000001, Email: amit@college.edu
ID: S102, Name: Riya Verma, Year: 3, Course: B.Tech, Branch: Electronics, Phone: 9000000002, Email: riya@college.edu
ID: S103, Name: Manish Kumar, Year: 1, Course: B.Tech, Branch: Mechanical, Phone: 9000000003, Email: manish@college.edu
ID: F201, Name: Dr. Anil Singh, Department: Computer Science, Phone: 8000000001, Email: anil@college.edu
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
 - Amit Sharma (ID: S101, Dept: Computer Science)
Amit Sharma added to society SAE
Volunteer Riya Verma from Electronics added to SAE

Society: SAE (Departmental)
Head: Dr. Rakesh Kumar
Coordinator: Neha Agarwal
Members (1):
  - Amit Sharma (ID: S101, Dept: Computer Science)
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
