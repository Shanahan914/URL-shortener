# URL Shortener Flask API

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
