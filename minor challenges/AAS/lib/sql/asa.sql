--  Creating a database for students at the academy.
CREATE DATABASE academyStudents;

-- Creating a table called students to store the information about the students
CREATE TABLE student IF NOT EXISTS(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL 1000;
    name TEXT NOT NULL;
    student BLOB NOT NULL;
)
