# StudDash (Assessment Management System)

The StudDash is a web application that allows administrators, teachers, and students to manage assessments, track results, and perform various assessment-related tasks. This system provides a user-friendly interface for creating assessments, viewing individual and class reports, and conducting assessments online.

## Technology Specifications

The StudDash (Assessment Management System) is built using the following technologies:

- Python: Programming language used for the backend development.
- Flask: Web framework used to build the application.
- MongoDB: NoSQL database used to store assessment data.
- HTML/CSS: Frontend development languages for creating the user interface.
- JavaScript: Programming language used to add interactivity to the application.
- Jinja2: Templating engine used for rendering dynamic content.

## Temporary Login Details

To access the Assessment Management System, you can use the following temporary login details:

- Admin:
  - Username: owner
  - Password: adminLog

- Teacher:
  - Username: teacher1
  - Password: teacherLog

- Student:
  - Username: student1
  - Password: studentLog

Please note that these are temporary login credentials provided for testing purposes.

## screenshots

Below are the screenshots of different parts of the Assessment Management System:

1. Login Page:
   [![Login Page](static/screenshots/home.png)](static/screenshots/home.png)

2. Admin/Teacher Dashboard:
   [![Admin Dashboard](static/screenshots/od1.png)](static/screenshots/od1.png)
   [![Admin Dashboard](static/screenshots/od2.png)](static/screenshots/od2.png)

   Student Dashboard:
   [![Student Dashboard](static/screenshots/sd.png)](static/screenshots/sd.png)

3. Create Assessment (Admin & Teacher):
   [![Create Assessment](static/screenshots/ca.png)](static/screenshots/ca.png)

4. Individual Reports (Admin & Teacher):
   [![Individual Reports](static/screenshots/ir.png)](static/screenshots/ir.png)

5. Class Reports (Admin & Teacher):
   [![Class Reports](static/screenshots/cp.png)](static/screenshots/cp.png)

6. View Assessment (Admin & Teacher):
   [![View Assessment](static/screenshots/va.png)](static/screenshots/va.png)

7. View Results:
   [![View Results](static/screenshots/vr.png)](static/screenshots/vr.png)

8. Add User (Admin Only):
   [![Add User](static/screenshots/au.png)](static/screenshots/au.png)

9. Take Assessment (Student):
   [![Take Assessment](static/screenshots/ta.png)](static/screenshots/ta.png)

Please click on the respective screenshot links to view them in full size.

## How to Run the Application

To run the Assessment Management System on your local machine, follow the steps below:

1. Make sure you have Python and MongoDB installed on your system.
2. Clone this repository: `git clone https://github.com/your-username/assessment-management-system.git`
3. Navigate to the project directory: `cd assessment-management-system`
4. Install the required dependencies: `pip install -r requirements.txt`
5. Set up the MongoDB connection by creating a database with required collections on mongoDB Atlas.
6. Run the application: `python app.py`
7. Open your web browser and access the application at: `http://localhost:5000`

Make sure to replace `your-username` with your actual GitHub username in step 2.

That's it! You should now be able to access and use the StudDash on your local machine.

