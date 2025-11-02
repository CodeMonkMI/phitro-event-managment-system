# Event Management System

This is a Django-based Event Management System that allows users to create, manage, and browse events. It provides a user-friendly interface for both event organizers and attendees.

## Features

-   User authentication (sign-up, sign-in, sign-out)
-   Create, update, and delete events
-   Browse events by category
-   Event categorization
-   User profile management
-   User role management (admin, event organizer, general user)
-   Frontend and backend separation
-   Docker support for easy setup and deployment

## Technologies Used

-   **Backend:** Django, Django REST Framework
-   **Frontend:** HTML, Tailwind CSS
-   **Database:** PostgreSQL
-   **Server:** Gunicorn
-   **Other:** Docker, `python-decouple`, `dj-database-url`, `whitenoise`

## Prerequisites

-   Python 3.11 or later
-   PostgreSQL
-   Node.js and pnpm (for manual setup)
-   Docker and Docker Compose (for Docker setup)

## Installation and Running

### Manual Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/phitron-evms.git
    cd phitron-evms
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv .evms_env
    source .evms_env/bin/activate
    ```

3.  **Install Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Install frontend dependencies and build CSS:**

    ```bash
    pnpm install
    pnpm run build
    ```

5.  **Set up the environment variables:**

    Create a `.env` file in the root directory by copying `.env.example`:

    ```bash
    cp .env.example .env
    ```

    Update the `.env` file with your database credentials and other settings. For manual setup, the `DATABASE` URL should be something like:

    ```
    DATABASE=postgresql://postgres:postgres@localhost:5432/evms
    ```

6.  **Run database migrations:**

    ```bash
    python manage.py migrate
    ```

7.  **Seed the database (optional):**

    ```bash
    python seed.py
    ```

8.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The application will be available at `http://127.0.0.1:8000`.

### Docker Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/phitron-evms.git
    cd phitron-evms
    ```

2.  **Set up the environment variables:**

    Create a `.env` file in the root directory by copying `.env.example`:

    ```bash
    cp .env.example .env
    ```

    Update the `.env` file with your desired settings. For Docker setup, the `DATABASE` URL should be:

    ```
    DATABASE=postgresql://postgres:postgres@evms_db:5432/evms
    ```

3.  **Build and run the Docker containers:**

    ```bash
    docker-compose up --build
    ```

    The application will be available at `http://localhost:8000`.

## Seeding the Database

The `seed.py` script populates the database with initial data using the `Faker` library. This includes creating users, categories, and events.

To seed the database, run the following command:

```bash
python seed.py
```

When using Docker, the database is seeded automatically when the container starts, as defined in the `docker-entrypoint.sh` script.

## Project Structure

```
phitron-evms/
├── categories/      # Django app for event categories
├── dashboard/       # Django app for the user dashboard
├── events/          # Django app for events
├── evms/            # Main Django project folder
├── front/           # Django app for the frontend
├── group/           # Django app for user groups/roles
├── users/           # Django app for user management
├── static/          # Static files (CSS, JS, images)
├── templates/       # Base templates
├── .env.example     # Example environment variables
├── docker-compose.yaml # Docker Compose configuration
├── dockerfile       # Dockerfile for the web service
├── manage.py        # Django's command-line utility
├── requirements.txt # Python dependencies
├── package.json     # Frontend dependencies
└── seed.py          # Database seeding script
```
