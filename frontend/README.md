# WE-ii Chat Frontend

A React-based chat interface for the WE-ii application with Auth0 authentication. This frontend provides a secure, authenticated chat experience that connects to the FastAPI backend.

## Features

- **Secure Authentication**: Auth0-based login and logout
- **Protected Routes**: Chat interface accessible only to authenticated users
- **Real-time Chat**: Send messages and receive responses from the WE-ii backend
- **Token Management**: Automatically includes Auth0 access tokens in API requests
- **Simple UI**: Clean, responsive interface with basic CSS styling

## Prerequisites

- Node.js (v14 or higher recommended)
- npm or yarn
- Auth0 account (free tier available at https://auth0.com)
- Running WE-ii FastAPI backend (see main repository README)

## Setup Instructions

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Configure Auth0

#### Step 2.1: Create an Auth0 Application

1. Go to https://auth0.com and create a free account or log in
2. Navigate to **Applications** > **Applications** in the Auth0 Dashboard
3. Click **Create Application**
4. Choose a name (e.g., "WE-ii Chat Frontend")
5. Select **Single Page Web Applications**
6. Click **Create**

#### Step 2.2: Configure Application Settings

In your Auth0 application settings:

1. **Allowed Callback URLs**: Add `http://localhost:3000`
2. **Allowed Logout URLs**: Add `http://localhost:3000`
3. **Allowed Web Origins**: Add `http://localhost:3000`
4. **Allowed Origins (CORS)**: Add `http://localhost:3000`
5. Click **Save Changes**

#### Step 2.3: Create an API (Optional but Recommended)

To enable access tokens with custom audiences:

1. Navigate to **Applications** > **APIs** in the Auth0 Dashboard
2. Click **Create API**
3. Give it a name (e.g., "WE-ii Backend API")
4. Set an identifier (e.g., `https://we-ii-api`)
5. Click **Create**

#### Step 2.4: Get Your Auth0 Credentials

From your Auth0 application settings page, note:
- **Domain** (e.g., `dev-xxxxx.us.auth0.com`)
- **Client ID** (e.g., `abc123...`)
- **API Identifier/Audience** (if you created an API)

### 3. Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env.local
   ```

2. Edit `.env.local` with your Auth0 credentials:
   ```env
   REACT_APP_AUTH0_DOMAIN=your-domain.auth0.com
   REACT_APP_AUTH0_CLIENT_ID=your-client-id
   REACT_APP_AUTH0_AUDIENCE=your-api-identifier
   REACT_APP_API_URL=http://localhost:8000
   ```

   - Replace `your-domain.auth0.com` with your Auth0 domain
   - Replace `your-client-id` with your Auth0 client ID
   - Replace `your-api-identifier` with your API identifier (or leave empty if not using)
   - Update `REACT_APP_API_URL` if your backend runs on a different port

### 4. Start the Development Server

```bash
npm start
```

The application will open at `http://localhost:3000`.

## Usage

1. **Login**: Click the "Log In" button on the welcome screen
2. **Authenticate**: Complete the Auth0 authentication flow
3. **Chat**: Once authenticated, use the chat interface to send messages
4. **Logout**: Click the "Log Out" button in the header when done

## Project Structure

```
frontend/
├── public/
│   ├── index.html          # HTML template
│   └── robots.txt          # Robots configuration
├── src/
│   ├── components/
│   │   ├── ChatApp.js      # Main app component with auth logic
│   │   ├── ChatInterface.js    # Chat UI component
│   │   └── ChatInterface.css   # Chat styling
│   ├── App.js              # Auth0Provider wrapper
│   ├── App.css             # Main app styling
│   ├── index.js            # React entry point
│   └── index.css           # Global styles
├── .env.example            # Environment variables template
├── package.json            # Dependencies and scripts
└── README.md              # This file
```

## API Integration

The frontend communicates with the backend through the `/chat` endpoint:

- **Endpoint**: `POST /chat`
- **Headers**:
  - `Content-Type: application/json`
  - `Authorization: Bearer <access_token>`
- **Request Body**: `{ "message": "user message here" }`
- **Response**: `{ "response": "bot response here" }`

## Authentication Flow

1. User clicks "Log In"
2. Redirected to Auth0 for authentication
3. After successful login, redirected back to the app
4. Auth0 SDK stores tokens securely
5. When sending messages, `getAccessTokenSilently()` retrieves the access token
6. Access token is included in the `Authorization` header for API requests

## Security Notes

### Frontend Authentication Enforcement

The current implementation enforces authentication **in the frontend only**:
- Unauthenticated users cannot access the chat UI
- All API requests include the Auth0 access token
- The token is obtained through Auth0's secure flow

### Backend Token Verification (Future Enhancement)

**For production use**, the backend should verify the Auth0 access tokens. Here's how to implement this:

#### 1. Install Required Python Packages

```bash
pip install python-jose[cryptography] requests
```

#### 2. Add Token Verification to Backend

Add this middleware to `main.py`:

```python
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
import requests

# Auth0 Configuration
AUTH0_DOMAIN = "your-domain.auth0.com"
AUTH0_AUDIENCE = "your-api-identifier"
ALGORITHMS = ["RS256"]

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    
    try:
        # Get Auth0 public key
        jwks_url = f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
        jwks = requests.get(jwks_url).json()
        
        # Decode and verify token
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
        
        if rsa_key:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=AUTH0_AUDIENCE,
                issuer=f"https://{AUTH0_DOMAIN}/"
            )
            return payload
        
        raise HTTPException(status_code=401, detail="Unable to find appropriate key")
        
    except JWTError as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {str(e)}")

# Update the /chat endpoint
@app.post("/chat")
async def chat(request: Request, token_payload: dict = Security(verify_token)):
    data = await request.json()
    message = data.get("message", "")
    response = lila.respond(message)
    return {"response": response}
```

#### 3. Configure CORS

The backend now has CORS configured. For production deployments, you can set the `CORS_ORIGINS` environment variable:

```bash
# Development (default)
CORS_ORIGINS=http://localhost:3000

# Production (multiple origins)
CORS_ORIGINS=https://your-frontend.com,https://www.your-frontend.com
```

The CORS configuration in `main.py`:

```python
from fastapi.middleware.cors import CORSMiddleware
from config import CORS_ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,  # Configured via environment variable
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)
```

## Development

### Available Scripts

- `npm start` - Start development server (http://localhost:3000)
- `npm build` - Create production build
- `npm test` - Run tests (if configured)
- `npm eject` - Eject from Create React App (irreversible)

### Running with Backend

1. Start the FastAPI backend:
   ```bash
   # In the root directory
   uvicorn main:app --reload
   ```

2. In a separate terminal, start the frontend:
   ```bash
   # In the frontend directory
   npm start
   ```

### Troubleshooting

**Issue**: "Invalid redirect URI" error from Auth0
- **Solution**: Verify that `http://localhost:3000` is added to all redirect URL fields in Auth0 settings

**Issue**: CORS errors when calling the backend
- **Solution**: Add CORS middleware to the backend (see Security Notes section)

**Issue**: 401 Unauthorized responses from backend
- **Solution**: Ensure the backend is configured to accept requests without token verification, or implement token verification as described above

**Issue**: "Failed to fetch" or network errors
- **Solution**: Verify the backend is running and `REACT_APP_API_URL` in `.env.local` is correct

## Security Vulnerabilities Notice

This project uses `react-scripts` which has some known vulnerabilities in its dependencies. These are primarily development dependencies and do not affect the production build security. For a production deployment:

1. Use `npm run build` to create an optimized production build
2. Serve the build folder with a production server (not `react-scripts`)
3. **Recommended**: Consider migrating to Vite or another modern build tool for better security and performance

### Migration to Vite (Recommended for Production)

For enhanced security and better performance, consider migrating from Create React App to Vite:

```bash
# Install Vite and required dependencies
npm install --save-dev vite @vitejs/plugin-react

# Update package.json scripts to use Vite
# Then migrate your code following the Vite migration guide
```

Vite offers:
- Faster development server
- Better build performance
- No known security vulnerabilities
- Modern ESM-based architecture

## Production Deployment

For production deployment:

1. Build the application:
   ```bash
   npm run build
   ```

2. Update Auth0 settings with your production URLs

3. Set production environment variables

4. Serve the `build` folder with a web server (nginx, Apache, or CDN)

5. **Implement backend token verification** (see Security Notes above)

## License

This frontend is part of the WE-ii project and follows the same license as the main repository.

## Support

For issues or questions:
- Check Auth0 documentation: https://auth0.com/docs
- Review FastAPI backend setup in the main repository README
- Ensure all environment variables are correctly configured
