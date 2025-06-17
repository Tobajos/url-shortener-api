# URL Shortener API

A minimal Django REST Framework project that shortens URLs.

## Endpoints

- `POST /api/shorten/` – create a short URL  
- `GET /api/expand/<short_code>/` – expand back to the original URL

## Example

### POST  
`http://localhost:8000/api/shorten/`  
**Request Body:**
```json
{
  "original_url": "https://example.com/very/long/url"
}
```
**Response:**
```json
{
  "short_url": "http://localhost:8000/api/expand/XyZ123/"
}
```

### GET  
`http://localhost:8000/api/expand/XyZ123/`  
**Response:**
```json
{
  "original_url": "https://example.com/very/long/url"
}
```

## How to run locally

```bash
# Create virtual environment
python -m venv venv

# Activate environment (Windows)
venv\Scripts\activate

# Activate environment (Linux/macOS)
source venv/bin/activate

# Install dependencies
pip install django djangorestframework

# Apply migrations
python manage.py migrate

# Run the server
python manage.py runserver
```
