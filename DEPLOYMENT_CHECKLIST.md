# WE-ii Deployment Checklist

Use this checklist to ensure proper deployment of the WE-ii chat application.

## Development Setup ✓

- [x] Backend CORS middleware configured
- [x] Frontend React app with Auth0 authentication
- [x] CORS environment variable support added
- [x] Security-focused CORS configuration (specific methods and headers)
- [x] Documentation updated
- [x] CodeQL security scan passed (0 vulnerabilities)
- [x] Integration tests completed

## Before Going to Production

### Backend Configuration

- [ ] Set `CORS_ORIGINS` environment variable with production frontend URLs
  ```bash
  export CORS_ORIGINS="https://yourapp.com,https://www.yourapp.com"
  ```

- [ ] Implement Auth0 token verification (optional but recommended)
  - See `frontend/README.md` for implementation details
  - Install dependencies: `pip install python-jose[cryptography] requests`

- [ ] Configure production ASGI server
  ```bash
  uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
  ```

- [ ] Enable HTTPS/SSL for backend API

- [ ] Set up rate limiting for API endpoints

- [ ] Configure logging and monitoring

- [ ] Set up database if needed (currently in-memory only)

### Frontend Configuration

- [ ] Create production Auth0 application

- [ ] Update Auth0 settings with production URLs:
  - Allowed Callback URLs
  - Allowed Logout URLs
  - Allowed Web Origins
  - Allowed Origins (CORS)

- [ ] Create `.env.production.local` with production values:
  ```env
  REACT_APP_AUTH0_DOMAIN=your-domain.auth0.com
  REACT_APP_AUTH0_CLIENT_ID=your-production-client-id
  REACT_APP_AUTH0_AUDIENCE=your-api-identifier
  REACT_APP_API_URL=https://your-backend-api.com
  ```

- [ ] Build production bundle: `npm run build`

- [ ] Test production build locally before deploying

- [ ] Configure web server (nginx/Apache) or CDN to serve build folder

- [ ] Enable HTTPS/SSL for frontend

### Security

- [ ] Review and update CORS origins for production
- [ ] Enable Auth0 MFA for enhanced security
- [ ] Implement backend token verification
- [ ] Set up security headers (CSP, HSTS, etc.)
- [ ] Regular dependency updates scheduled
- [ ] Security monitoring and alerts configured
- [ ] Backup strategy for any persistent data

### Testing

- [ ] End-to-end testing in production-like environment
- [ ] Auth0 login/logout flow tested
- [ ] Chat functionality tested
- [ ] CORS tested from production frontend URL
- [ ] Error handling tested
- [ ] Mobile responsiveness tested
- [ ] Load testing completed

### Monitoring & Maintenance

- [ ] Application logging configured
- [ ] Error tracking set up (e.g., Sentry)
- [ ] Performance monitoring enabled
- [ ] Uptime monitoring configured
- [ ] Backup and recovery procedures documented
- [ ] Incident response plan created

## Development Environment Verification

Quick checks to verify development setup is working:

```bash
# Backend health check
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "test"}'

# CORS check
curl -X OPTIONS http://localhost:8000/chat \
  -H "Origin: http://localhost:3000" \
  -H "Access-Control-Request-Method: POST" \
  -v | grep -i access-control

# Frontend build check
cd frontend && npm run build
```

All should succeed without errors.

## Quick Reference

### Start Development Servers

**Backend** (Terminal 1):
```bash
cd /path/to/WE-ii
uvicorn main:app --reload
```

**Frontend** (Terminal 2):
```bash
cd /path/to/WE-ii/frontend
npm start
```

### Environment Variables

**Backend**:
- `CORS_ORIGINS`: Comma-separated list of allowed origins (default: `http://localhost:3000`)

**Frontend** (`.env.local`):
- `REACT_APP_AUTH0_DOMAIN`: Your Auth0 domain
- `REACT_APP_AUTH0_CLIENT_ID`: Your Auth0 client ID
- `REACT_APP_AUTH0_AUDIENCE`: Your Auth0 API identifier (optional)
- `REACT_APP_API_URL`: Backend API URL (default: `http://localhost:8000`)

---

**Created**: January 10, 2026  
**Status**: Development Complete - Ready for Production Planning
