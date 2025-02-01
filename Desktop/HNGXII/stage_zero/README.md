OUTLINES

Project Title & Description
Features
Tech Stack
Installation Steps
Usage Guide
API Documentation
Contributing Guide
License
Contact Information/ Backlink


# Django REST API for User Information

A simple Django REST API that returns user email and Current_time in ISO 8601 format.

## Features
- Returns user email and timestamp in ISO 8601 format
- Uses Django REST Framework (DRF)
- Supports JSON responses

## Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL (or SQLite by default)
- **Authentication:** Django Authentication (optional)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-user-api.git
   cd django-user-api

2. Create a virtual environment:
   virtualenv venv NB: (Venv) can be any name you choose
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run migrations:
   python manage.py migrate

5. Create a superuser (optional):
   python manage.py createsuperuser

6. Run the server:
   python manage.py runserver



   API Endpoints

Method	Endpoint	Description
GET	/api/userinfo/	Fetch user email & current_time & github_url

Example Response
{
    "email": "user@example.com",
    "current_time": "2024-01-31T14:30:15.123456Z"
    "github_url": 'http://github.com/kingsleyabonyi
}


Contributing

    Fork the repository.
    Create a new branch (feature/your-feature).
    Commit your changes (git commit -m "Added a new feature").
    Push to the branch (git push origin feature/your-feature).
    Create a Pull Request.


License

This project is licensed under the MIT License.

Contact Information/ Backlink

 https://hng.tech/hire/python-developers