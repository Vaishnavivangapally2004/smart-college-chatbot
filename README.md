
# Smart College Chatbot – Student Assistance

This is a Python and MySQL-based chatbot system designed to assist college students by answering academic and administrative queries. It also includes a Login and Registration system to secure access and maintain student interaction history (if applicable).

Login & Registration

The system includes:
- User Registration Page: Allows students to sign up with their name, email, and password.
- Login Page: Students can log in and access the chatbot interface.

Screenshots

Register Page:

<img width="1920" height="1080" alt="Screenshot 2025-04-30 073503" src="https://github.com/user-attachments/assets/231562ad-28ba-4b8b-83ca-e75aec1214c0" />


Login Page:
<img width="1920" height="1080" alt="Screenshot 2025-04-30 073408" src="https://github.com/user-attachments/assets/7f1f89b0-fa78-47e9-adc0-4d6d9b14f9bc" />



Features

- Responds to student queries about:
  - Faculty and departments
  - Class schedules and exams
  - General college-related FAQs
- Connects to MySQL for fetching predefined answers
- Basic authentication (login/register)
- Console or web interface (customizable)

Technologies Used

- Language: Python  
- Database: MySQL  
- Authentication: Basic login/register form  
- Tools: Localhost (XAMPP/WAMP), or any local server

Database Structure

Table 1: `faq_data`  
Stores chatbot questions and answers.

| Column   | Type  | Description            |
|----------|-------|------------------------|
| id       | INT   | Primary Key            |
| question | TEXT  | Keywords from user     |
| answer   | TEXT  | Response shown to user |

Table 2: `users`  
Stores login credentials.

| Column    | Type     | Description         |
|-----------|----------|---------------------|
| id        | INT      | Primary Key         |
| name      | VARCHAR  | User’s full name    |
| email     | VARCHAR  | Login email         |
| password  | VARCHAR  | Hashed password     |

Chatbot Output
<img width="1920" height="1080" alt="Screenshot 2025-04-30 073224" src="https://github.com/user-attachments/assets/ca49dbcc-010d-4a07-b892-33b9b21d845d" />

Project Structure
<img width="439" height="381" alt="Screenshot 2025-07-21 223906" src="https://github.com/user-attachments/assets/c0cc563b-7353-4674-81a9-86adb3e403f1" />


How to Run

1. Import `db.sql` into your MySQL server.
2. Run `register.py` to register a user.
3. Run `login.py` to access the chatbot.
4. Interact with the chatbot using academic queries.

Future Improvements

- Add password hashing and user validation
- Expand chatbot with NLP for smarter responses
- Add admin dashboard to manage FAQs dynamically
