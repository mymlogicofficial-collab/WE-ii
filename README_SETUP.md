# WE-ii Lila Platform - Setup Guide

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

Copy the example environment file and configure it:

```bash
cp .env.example .env
```

Edit `.env` and add your Stripe API key (optional for basic chat functionality).

### 3. Start the Backend Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### 4. Open the Chat Interface

Open `chat.html` in your web browser or navigate to:
- `http://localhost:8000/` (API documentation)
- Open `chat.html` directly in a browser

## Features

### Chat Interface
- **ChatGPT-style UI** with message bubbles
- **Real-time communication** with the Lila platform
- **Quick action buttons** for common queries
- **Typing indicators** for better UX
- **Error handling** with user-friendly messages

### Authentication
- **Founder key authentication** (key: "83")
- **Secure access** to platform features
- **Status indicator** showing authentication state

### API Endpoints

#### `GET /`
Get API information and available endpoints.

#### `POST /chat`
Send chat messages to the Lila platform.

**Request:**
```json
{
  "message": "Hello, Lila!",
  "user_key": "83"  // optional
}
```

**Response:**
```json
{
  "response": "Welcome to WE-ii Lila Platform!...",
  "status": "success"
}
```

#### `POST /auth`
Authenticate with founder key.

**Request:**
```json
{
  "key": "83"
}
```

**Response:**
```json
{
  "status": "HEAVY",
  "identity": "Lila Lawson",
  "active_mission": "KIDS",
  "message": "Welcome home, Sterling. The Hub is secure."
}
```

#### `GET /status`
Get current system status.

#### `GET /principles`
Get all Deep Seed Principles.

## Project Structure

```
WE-ii/
├── main.py                 # FastAPI backend server
├── neuropathways.py        # Core Lila platform logic
├── nuropathways.py         # Mobile Lila platform
├── stripe_bridge.py        # Stripe payment integration
├── requirements.txt        # Python dependencies
├── .env.example           # Environment configuration template
├── chat.html              # Chat interface (ChatGPT-style)
├── index.html             # Main landing page
└── README_SETUP.md        # This file
```

## Development

### Running Tests

```bash
python -m pytest  # If tests are added
```

### Testing the API

You can test the API using curl:

```bash
# Test root endpoint
curl http://localhost:8000/

# Test chat endpoint
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'

# Test authentication
curl -X POST http://localhost:8000/auth \
  -H "Content-Type: application/json" \
  -d '{"key": "83"}'

# Get status
curl http://localhost:8000/status

# Get principles
curl http://localhost:8000/principles
```

## Chat Commands

The chat interface responds to various keywords:

- **"hello"** or **"hi"** - Welcome message
- **"status"** - Get system status
- **"secure"** or **"heavy"** - Security status
- **"principle"** + principle name - Get specific principle info
  - Available principles: compassion, integrity, pain, joy

## Security Features

- **Environment-based configuration** - All sensitive data stored in `.env` file
- **CORS configuration** - Configurable allowed origins for API access
- **Authentication** - Founder key-based authentication
- **No hardcoded secrets** - All keys and URLs use environment variables
- **Stripe optional** - Payment features gracefully disabled if not configured

## Stripe Integration (Optional)

The platform includes Stripe Express integration for payment handling:

1. Sign up for a Stripe account
2. Get your API key from the Stripe Dashboard
3. Add the key to your `.env` file
4. Use the `onboard_recipient()` and `payout_to_recipient()` functions in `stripe_bridge.py`

## Troubleshooting

### Backend not connecting
- Make sure the FastAPI server is running
- Check that it's running on port 8000
- Verify no firewall is blocking the connection

### CORS errors
- The backend is configured to allow all origins in development
- For production, update the CORS settings in `main.py`

### Authentication failing
- The default founder key is "83"
- Make sure you're using the correct key
- Check that the backend is running

## Production Deployment

For production deployment:

1. Set `APP_ENV=production` in `.env`
2. Use a production WSGI server like gunicorn
3. Update CORS settings to allow only your domain
4. Use HTTPS
5. Set up proper authentication and authorization
6. Use production Stripe keys (sk_live_...)

```bash
# Production server example
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## License

WE-ii & SE CUSTOMS © 2026

## Support

For issues or questions, please contact the development team.
