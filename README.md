# Smart College Chatbot – Student Assistance

This project is a chatbot system designed to assist college students with academic and administrative queries. It connects to a MySQL database to fetch relevant answers based on user input.

Project Overview

The chatbot helps students quickly find answers to questions related to:
- Class timetables
- Faculty contact details
- Department information
- Exam schedules
- General college FAQs

It uses a simple Python script with database integration to respond based on predefined Q&A entries.

 Technologies Used

Language: Python  
Database: MySQL  
Interface: Console-based or Web (specify if you used one)  
Environment: XAMPP / Localhost (if applicable)

Database Design

Table Name: `faq_data`

| Column   | Type        | Description                     |
|----------|-------------|---------------------------------|
| id       | INT         | Primary key (auto-increment)    |
| question | TEXT        | Question keywords to match user input |
| answer   | TEXT        | Response to be shown to user    |

Sample Entry:
sql
INSERT INTO faq_data (question, answer)
VALUES ('hod of cse', 'The HOD of CSE is Dr. Ramesh Kumar');
