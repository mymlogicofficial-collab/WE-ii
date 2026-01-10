# WE-ii Chat Integration Guide

## Overview

This guide explains how to run the complete WE-ii chat application, which consists of:
- **Backend**: FastAPI server with LilaMeta AI chat engine
- **Frontend**: React-based UI with Auth0 authentication

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                  React Frontend                     │
│              (http://localhost:3000)                │
│  - Auth0 Authentication                             │
│  - Chat UI Interface                                │
│  - Token Management                                 │
└────────────────┬────────────────────────────────────┘
                 │ CORS-enabled API calls
                 │ with Bearer tokens
                 ▼
┌─────────────────────────────────────────────────────┐
│                 FastAPI Backend                     │
│              (http://localhost:8000)                │
│  - /chat endpoint                                   │
│  - LilaMeta AI (Freedom Core)                       │
│  - Dual neuro access (intent + intense)             │
└─────────────────────────────────────────────────────┘
```

## Prerequisites

### Backend Requirements
- Python 3.8 or higher
- pip (Python package manager)

### Frontend Requirements
- Node.js 14 or higher
- npm (comes with Node.js)

### Auth0 Account
- Free Auth0 account: https://auth0.com

## Quick Start

### Step 1: Clone and Navigate
```bash
cd /path/to/WE-ii
```

### Step 2: Backend Setup

#### 2.1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

#### 2.2. Verify Backend Configuration
The backend is pre-configured with:
- ✅ CORS middleware for frontend communication
- ✅ `/chat` endpoint for message processing
- ✅ LilaMeta AI with dual neuro access

#### 2.3. Start the Backend Server
```bash
uvicorn main:app --reload
```

The backend will start at `http://localhost:8000`

You can test it with:
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello!"}'
```

### Step 3: Frontend Setup

#### 3.1. Install Frontend Dependencies
```bash
cd frontend
npm install
```

#### 3.2. Configure Auth0

1. **Create an Auth0 Application**
   - Go to https://auth0.com and sign up/login
   - Navigate to **Applications** > **Applications**
   - Click **Create Application**
   - Name: "WE-ii Chat Frontend"
   - Type: **Single Page Web Applications**
   - Click **Create**

2. **Configure Application Settings**
   
   In your Auth0 application settings, add:
   - **Allowed Callback URLs**: `http://localhost:3000`
   - **Allowed Logout URLs**: `http://localhost:3000`
   - **Allowed Web Origins**: `http://localhost:3000`
   - **Allowed Origins (CORS)**: `http://localhost:3000`
   - Click **Save Changes**

3. **(Optional) Create an API**
   
   For production use with token verification:
   - Navigate to **Applications** > **APIs**
   - Click **Create API**
   - Name: "WE-ii Backend API"
   - Identifier: `https://we-ii-api` (or your preferred identifier)
   - Click **Create**

#### 3.3. Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env.local
   ```

2. Edit `.env.local` with your Auth0 credentials:
   ```env
   REACT_APP_AUTH0_DOMAIN=your-domain.auth0.com
   REACT_APP_AUTH0_CLIENT_ID=your-client-id-here
   REACT_APP_AUTH0_AUDIENCE=https://we-ii-api
   REACT_APP_API_URL=http://localhost:8000
   ```

   Replace:
   - `your-domain.auth0.com` with your Auth0 domain
   - `your-client-id-here` with your Auth0 client ID
   - `https://we-ii-api` with your API identifier (or leave empty if not using)

#### 3.4. Start the Frontend Development Server
```bash
npm start
```

The frontend will start at `http://localhost:3000` and automatically open in your browser.

### Step 4: Using the Application

1. **Login**
   - Click the "Log In" button on the welcome screen
   - Complete the Auth0 authentication flow
   - You'll be redirected back to the chat interface

2. **Chat**
   - Type a message in the input field
   - Press Enter or click "Send"
   - LilaMeta will respond with her blend of intent and intense responses

3. **Logout**
   - Click the "Log Out" button in the header when finished

## Development Workflow

### Running Both Servers Simultaneously

**Terminal 1 - Backend:**
```bash
cd /path/to/WE-ii
uvicorn main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd /path/to/WE-ii/frontend
npm start
```

### Testing the Integration

1. **Backend Health Check**
   ```bash
   curl http://localhost:8000/chat \
     -X POST \
     -H "Content-Type: application/json" \
     -d '{"message": "test"}'
   ```

2. **Frontend Build Test**
   ```bash
   cd frontend
   npm run build
   ```

## Troubleshooting

### Issue: CORS Errors

**Symptom**: Browser console shows CORS policy errors

**Solution**: The backend now includes CORS middleware configured for `http://localhost:3000`. If you change the frontend port, update `main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:YOUR_PORT"],  # Update this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Issue: "Invalid redirect URI" from Auth0

**Symptom**: Auth0 shows an error about redirect URI

**Solution**: Verify that `http://localhost:3000` is added to ALL redirect URL fields in Auth0 application settings

### Issue: Backend Connection Failed

**Symptom**: Frontend shows "Failed to fetch" or connection errors

**Solution**: 
1. Verify the backend is running at `http://localhost:8000`
2. Check that `REACT_APP_API_URL` in `.env.local` is set to `http://localhost:8000`
3. Ensure CORS is configured in the backend

### Issue: npm Vulnerabilities Warning

**Symptom**: `npm install` shows vulnerability warnings

**Note**: These are primarily development dependencies in `react-scripts`. For production:
- Use `npm run build` to create an optimized build
- Serve the `build` folder with a production server
- Consider migrating to Vite for better security and performance

## Production Deployment

### Backend Deployment

1. **Environment Variables**: Set up proper environment variables for production
2. **Token Verification**: Implement Auth0 token verification (see frontend/README.md)
3. **CORS Configuration**: Update allowed origins to your production frontend URL
4. **HTTPS**: Deploy with HTTPS enabled

### Frontend Deployment

1. **Build the Production Bundle**
   ```bash
   cd frontend
   npm run build
   ```

2. **Update Auth0 Settings**
   - Add your production URL to all allowed URL fields
   - Update `REACT_APP_API_URL` to your production backend URL

3. **Deploy the `build` folder** to your hosting service:
   - Static hosting: Netlify, Vercel, AWS S3 + CloudFront
   - Web server: nginx, Apache
   - CDN: Cloudflare Pages, GitHub Pages (for static sites)

### Security Recommendations

⚠️ **Important**: The current implementation authenticates users in the frontend only. For production:

1. **Backend Token Verification**: Implement Auth0 JWT verification in the backend
2. **HTTPS Only**: Use HTTPS for both frontend and backend
3. **Environment Variables**: Never commit `.env.local` or expose credentials
4. **Token Rotation**: Configure Auth0 token rotation policies
5. **Rate Limiting**: Implement API rate limiting

See `frontend/README.md` for detailed security implementation instructions.

## Project Structure

```
WE-ii/
├── main.py                    # FastAPI backend with CORS
├── config.py                  # Backend configuration
├── requirements.txt           # Python dependencies
├── neuropathways/            # Intent-based neuro module
│   └── neuro.py
├── nuropathways/             # Intense neuro module
│   └── neuro.py
└── frontend/                 # React frontend
    ├── package.json          # Node dependencies
    ├── .env.example          # Environment template
    ├── .env.local            # Your Auth0 config (create this)
    ├── public/
    │   └── index.html
    └── src/
        ├── App.js            # Auth0Provider wrapper
        ├── components/
        │   ├── ChatApp.js    # Auth logic & layout
        │   └── ChatInterface.js  # Chat UI
        └── index.js          # React entry point
```

## API Reference

### Backend Endpoint

**POST /chat**

Send a message to LilaMeta and receive a response.

**Request:**
```json
{
  "message": "Your message here"
}
```

**Response:**
```json
{
  "response": "LilaMeta's response (blend of intent and intense)"
}
```

**Headers:**
- `Content-Type: application/json`
- `Authorization: Bearer <token>` (when using Auth0 token verification)

## Additional Resources

- **Frontend README**: `frontend/README.md` - Detailed frontend documentation
- **Run Guide**: `RUN.md` - Backend-specific run instructions
- **Demo Script**: `demo.py` - Backend demo and testing

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review `frontend/README.md` for frontend-specific issues
3. Verify Auth0 configuration at https://auth0.com/docs
4. Check backend logs for errors

## License

This project is part of the WE-ii repository and follows the same license.
