# URL Shortener Flask API

This is a solution to the URL shortener project on roadmap.sh : https://roadmap.sh/projects/url-shortening-service

This is a simple URL shortening service built with Flask, PostgreSQL, and SQLAlchemy. The service allows users to create, retrieve, update, and delete shortened URLs, as well as track the usage statistics of each shortened URL.

## Features

- **Shorten URLs:** Generate a unique, shortened version of any URL.
- **Retrieve URLs:** Look up the original URL using the shortened code.
- **Update URLs:** Modify the original URL associated with a shortened code.
- **Delete URLs:** Remove shortened URLs from the system.
- **View Stats:** Track how many times a shortened URL has been accessed.

## Project Structure

- **`run.py`**: Entry point to start the Flask application.
- **`config.py`**: Contains configuration settings for Flask and SQLAlchemy.
- **`extensions.py`**: Initializes extensions such as the database.
- **`models.py`**: Defines the `Url` model representing the URL table in the database.
- **`routes.py`**: Contains all the routes for interacting with the API.
- **`__init__.py`**: Initializes the Flask application and registers blueprints.

## Prerequisites

- Python 3.x
- PostgreSQL
- Redis (optional, depending on your `Flask-Limiter` configuration)
- Flask and other dependencies listed in `requirements.txt`

## Setup and Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/url-shortener.git
   cd url-shortener
   ```

2. **Create virtual environment:**
```
   python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```
   pip install -r requirements.txt

```

4. **Configure environment variables:**
```
  FLASK_APP=run.py
FLASK_ENV=development
DATABASE_URL=postgresql://username:password@localhost/dbname
REDIS_URL=redis://localhost:6379/0

```

4. **Initialise db:**
```
 flask db init
flask db migrate
flask db upgrade


```

4. **Run:**
```
python run.py
```

## API Endpoints

### **POST /shorten**

Create a shortened URL.

- **Request:**
  - **Method:** POST
  - **Content-Type:** `application/json`
  - **Body:**
    ```json
    {
      "url": "http://example.com"
    }
    ```

- **Response:**
  - **Status Code:** 201 Created
  - **Body:**
    ```json
    {
      "id": 1,
      "url": "http://example.com",
      "shortCode": "abc123",
      "createdAt": "2024-08-21T12:00:00Z",
      "updated": "2024-08-21T12:00:00Z"
    }
    ```

- **Description:** Generates a unique shortened URL for the provided original URL.

### **GET /shorten/<short_code>**

Retrieve the original URL by its shortened code.

- **Request:**
  - **Method:** GET
  - **URL Parameter:** `short_code` (the unique shortened code)

- **Response:**
  - **Status Code:** 200 OK
  - **Body:**
    ```json
    {
      "id": 1,
      "url": "http://example.com",
      "shortCode": "abc123",
      "createdAt": "2024-08-21T12:00:00Z",
      "updated": "2024-08-21T12:00:00Z",
      "accessCount": 1
    }
    ```

- **Description:** Retrieves the original URL associated with the given shortened code and increments the access count.

### **PUT /shorten/<short_code>**

Update the original URL associated with a shortened code.

- **Request:**
  - **Method:** PUT
  - **Content-Type:** `application/json`
  - **URL Parameter:** `short_code` (the unique shortened code)
  - **Body:**
    ```json
    {
      "url": "http://newexample.com"
    }
    ```

- **Response:**
  - **Status Code:** 200 OK
  - **Body:**
    ```json
    {
      "id": 1,
      "url": "http://newexample.com",
      "shortCode": "abc123",
      "createdAt": "2024-08-21T12:00:00Z",
      "updated": "2024-08-21T12:00:00Z"
    }
    ```

- **Description:** Updates the original URL associated with the given shortened code.

### **DELETE /shorten/<short_code>**

Delete a shortened URL.

- **Request:**
  - **Method:** DELETE
  - **URL Parameter:** `short_code` (the unique shortened code)

- **Response:**
  - **Status Code:** 204 No Content

- **Description:** Deletes the shortened URL associated with the given shortened code.

### **GET /shorten/<short_code>/stats**

Get the usage statistics for a shortened URL.

- **Request:**
  - **Method:** GET
  - **URL Parameter:** `short_code` (the unique shortened code)

- **Response:**
  - **Status Code:** 200 OK
  - **Body:**
    ```json
    {
      "id": 1,
      "url": "http://example.com",
      "shortCode": "abc123",
      "createdAt": "2024-08-21T12:00:00Z",
      "updated": "2024-08-21T12:00:00Z",
      "accessCount": 1
    }
    ```

- **Description:** Retrieves the usage statistics, including the access count, for the given shortened URL.





   
