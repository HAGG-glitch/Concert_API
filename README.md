
# Concert_API

Concert_API is a FastAPI-based REST service for managing digital concert bookings. It includes features such as JWT authentication, role-based access control, actor/director-play links, ticketing, seat allocation, scheduling, and pricing. The API provides Swagger documentation for easy event management.

---

## Features

- Manage concerts, actors, and directors
- Book tickets with seat allocation
- Schedule events and set pricing
- Role-based access control
- JWT authentication and secure login
- Seamless event management with Swagger docs

---

## Technologies Used

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL
- Passlib
- Python-Jose
- Role-based and JWT authentication
- Object-Oriented Programming (OOP)

---

## Setup and Installation

Follow these steps to set up the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/concert-api.git
cd concert-api
```

### 2. Create and activate a virtual environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy[asyncio] psycopg2-binary passlib[bcrypt] python-jose
```

### 4. Configure the database

Create a PostgreSQL database (e.g., `concert_db`) and set the connection URL in your environment variables or config file:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/concert_db
```

### 5. Run database migrations

Set up your database models and apply migrations (using Alembic or similar tools).

### 6. Run the API server

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

---

## Group Members

- Yoki Joshua Alvin Nyakeh
- Sanah Marah
- Abraham Mekonen Araia

---

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For questions or issues, please contact the team members.

---

Enjoy managing concert bookings online!
```

Would you like me to add specific API endpoints, code snippets, or further details?
