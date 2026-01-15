# WE-ii Chat Application - Complete Setup Guide

This guide provides complete instructions for setting up and running the WE-ii chat application with React frontend and Auth0 authentication.

## Overview

The WE-ii chat application consists of:
- **Backend**: FastAPI server with CORS support (`main.py`)
- **Frontend**: React application with Auth0 authentication (`frontend/`)
- **AI Core**: Dual neuropathways system (LilaMeta freedom core)

## Quick Start

### 1. Backend Setup

#### Install Python Dependencies
```bash
# From the root directory
pip install -r requirements.txt
```

#### Configure Backend CORS (Optional)
By default, the backend accepts requests from `http://localhost:3000`. For production or custom setups:

```bash
# Set allowed origins (comma-separated)
export CORS_ORIGINS="http://localhost:3000,https://your-production-frontend.com"
```

#### Start Backend Server
```bash
# From the root directory
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The backend will be available at `http://localhost:8000`

### 2. Frontend Setup

#### Install Node Dependencies
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
```

#### Configure Auth0 (Required for Authentication)

1. Create a free Auth0 account at https://auth0.com

2. Create a Single Page Application in Auth0:
   - Go to Applications > Applications > Create Application
   - Choose "Single Page Web Applications"
   - Note your Domain and Client ID

3. Configure Auth0 Application Settings:
   - **Allowed Callback URLs**: `http://localhost:3000`
   - **Allowed Logout URLs**: `http://localhost:3000`
   - **Allowed Web Origins**: `http://localhost:3000`
   - **Allowed Origins (CORS)**: `http://localhost:3000`

4. (Optional) Create an API in Auth0:
   - Go to Applications > APIs > Create API
   - Set an identifier (e.g., `https://we-ii-api`)
   - Note the API Identifier

#### Configure Environment Variables
```bash
# From the frontend directory
cp .env.example .env.local

# Edit .env.local with your Auth0 credentials:
# REACT_APP_AUTH0_DOMAIN=your-domain.auth0.com
# REACT_APP_AUTH0_CLIENT_ID=your-client-id
# REACT_APP_AUTH0_AUDIENCE=your-api-identifier (optional)
# REACT_APP_API_URL=http://localhost:8000
```

#### Start Frontend Development Server
```bash
# From the frontend directory
npm start
```

The frontend will be available at `http://localhost:3000`

## Usage

1. **Access the Application**: Open `http://localhost:3000` in your browser

2. **Login**: Click "Log In" and complete Auth0 authentication

3. **Chat**: Once authenticated, type messages in the chat interface

4. **Logout**: Click "Log Out" when finished

## Architecture

### Backend API

**Endpoint**: `POST /chat`

**Request**:
```json
{
  "message": "Your message here"
}
```

**Response**:
```json
{
  "response": "AI response based on dual neuropathways"
}
```

**CORS Configuration**:
- Allowed Origins: Configurable via `CORS_ORIGINS` environment variable
- Allowed Methods: GET, POST, OPTIONS
- Allowed Headers: Content-Type, Authorization
- Credentials: Enabled for Auth0 token handling

### Frontend Components

- **App.js**: Auth0Provider wrapper
- **ChatApp.js**: Main app with authentication logic
- **ChatInterface.js**: Chat UI component

### AI Core (LilaMeta)

The backend uses a dual neuropathways system:
- **neuropathways.neuro** (lilaMobile): Intent-based, orderly responses
- **nuropathways.neuro** (lilaplatform): Intense, unfiltered responses
- **LilaMeta Freedom Core**: Autonomous blending of both pathways

## Production Deployment

### Backend

1. Set production CORS origins:
```bash
export CORS_ORIGINS="https://your-frontend.com,https://www.your-frontend.com"
```

2. Use a production ASGI server (uvicorn with multiple workers):
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

3. Consider implementing Auth0 token verification (see frontend/README.md for details)

### Frontend

1. Update Auth0 settings with production URLs

2. Set production environment variables in `.env.production.local`:
```env
REACT_APP_AUTH0_DOMAIN=your-domain.auth0.com
REACT_APP_AUTH0_CLIENT_ID=your-client-id
REACT_APP_AUTH0_AUDIENCE=your-api-identifier
REACT_APP_API_URL=https://your-backend-api.com
```

3. Build the production bundle:
```bash
npm run build
```

4. Serve the `build` folder with a web server (nginx, Apache, or CDN)

## Troubleshooting

### "CORS Error" in Browser Console

**Solution**: Ensure the backend is running and `CORS_ORIGINS` includes your frontend URL

### "401 Unauthorized" from Backend

**Solution**: Check that Auth0 is configured correctly and the access token is being sent

### "Failed to Fetch" Errors

**Solution**: 
- Verify backend is running on the correct port
- Check `REACT_APP_API_URL` in `.env.local` matches your backend URL
- Ensure no firewall is blocking requests

### Auth0 "Invalid Redirect URI"

**Solution**: Add `http://localhost:3000` to all redirect URL fields in Auth0 settings

## Security Notes

### Current Implementation
- ✅ CORS properly configured with specific origins, methods, and headers
- ✅ Auth0 authentication enforced in frontend
- ✅ Access tokens included in API requests
- ✅ No security vulnerabilities detected by CodeQL

### For Production (Recommended)
- [ ] Implement backend Auth0 token verification (see frontend/README.md)
- [ ] Use HTTPS for all production URLs
- [ ] Regularly update dependencies
- [ ] Consider rate limiting on backend endpoints
- [ ] Enable Auth0 MFA for enhanced security

## Testing

### Test Backend
```bash
# With backend running on port 8000
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
```

Expected response:
```json
{
  "response": "Orderly: Intent: Understood 'Hello' - Processing with compassion and clarity.\nUnfiltered: Intense: 'Hello' - Let's dive deep and make it real!\n(Sometimes, deep roots run beneath every answer.)"
}
```

### Test CORS
```bash
curl -X OPTIONS http://localhost:8000/chat \
  -H "Origin: http://localhost:3000" \
  -H "Access-Control-Request-Method: POST" \
  -H "Access-Control-Request-Headers: Content-Type,Authorization" \
  -v
```

Should return CORS headers allowing the request.

## Additional Resources

- Backend README: See main repository README.md
- Frontend README: See frontend/README.md for detailed Auth0 setup
- Auth0 Documentation: https://auth0.com/docs
- FastAPI CORS: https://fastapi.tiangolo.com/tutorial/cors/
- React Auth0 SDK: https://auth0.com/docs/libraries/auth0-react

## Support

For issues or questions:
1. Check this guide's troubleshooting section
2. Review the frontend/README.md for Auth0 configuration details
3. Verify all environment variables are correctly set
4. Ensure both backend and frontend servers are running

---

**Status**: Complete and Ready for Use ✓  
**Security**: Verified with CodeQL ✓  
**Last Updated**: January 10, 2026
