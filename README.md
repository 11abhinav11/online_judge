# Online Judge Competitive Programming Website

This repository contains the source code for an Online Judge Competitive Programming Website built using Django and Docker. The online judge system allows users to participate in coding competitions, submit their code solutions, and receive immediate feedback on their submissions.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Running Tests](#running-tests)
6. [Contributing](#contributing)
7. [License](#license)

## Features

- User authentication (signup, login, logout)
- Problem listing and details
- Code submission and evaluation
- Real-time feedback on submissions
- Leaderboard and user rankings
- Admin panel for managing problems and users

## Requirements

- Docker
- Docker Compose

## Installation

Follow these steps to get the project up and running on your local machine:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/online-judge.git
    cd online-judge
    ```

2. **Build and start the Docker containers:**
    ```bash
    docker-compose up --build
    ```

3. **Apply the database migrations:**
    ```bash
    docker-compose exec web python manage.py migrate
    ```

4. **Create a superuser for accessing the Django admin panel:**
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

5. **Collect static files:**
    ```bash
    docker-compose exec web python manage.py collectstatic --noinput
    ```

The application should now be running at `http://localhost:8000`.

## Usage

1. **Access the application:**
   Open your web browser and navigate to `http://localhost:8000`.

2. **Register or log in:**
   Create a new account or log in with an existing one.

3. **Browse and submit problems:**
   Explore the available problems, submit your solutions, and receive immediate feedback.

4. **Admin panel:**
   Access the admin panel at `http://localhost:8000/admin` using the superuser credentials created during the installation process. Here you can manage problems, users, and other aspects of the site.

## Running Tests

To run the tests for the Django application, use the following command:

```bash
docker-compose exec web python manage.py test
