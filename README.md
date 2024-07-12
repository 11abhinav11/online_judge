Online Judge Competitive Programming Website
This repository contains the source code for an Online Judge Competitive Programming Website built using Django and Docker. The online judge system allows users to participate in coding competitions, submit their code solutions, and receive immediate feedback on their submissions.

Table of Contents
Features
Requirements
Installation
Usage
Running Tests
Contributing
License
Features
User authentication (signup, login, logout)
Problem listing and details
Code submission and evaluation
Real-time feedback on submissions
Leaderboard and user rankings
Admin panel for managing problems and users
Requirements
Docker
Docker Compose
Installation
Follow these steps to get the project up and running on your local machine:

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/online-judge.git
cd online-judge
Build and start the Docker containers:

bash
Copy code
docker-compose up --build
Apply the database migrations:

bash
Copy code
docker-compose exec web python manage.py migrate
Create a superuser for accessing the Django admin panel:

bash
Copy code
docker-compose exec web python manage.py createsuperuser
Collect static files:

bash
Copy code
docker-compose exec web python manage.py collectstatic --noinput
The application should now be running at http://localhost:8000.

Usage
Access the application:
Open your web browser and navigate to http://localhost:8000.

Register or log in:
Create a new account or log in with an existing one.

Browse and submit problems:
Explore the available problems, submit your solutions, and receive immediate feedback.

Admin panel:
Access the admin panel at http://localhost:8000/admin using the superuser credentials created during the installation process. Here you can manage problems, users, and other aspects of the site.

Running Tests
To run the tests for the Django application, use the following command:

bash
Copy code
docker-compose exec web python manage.py test
