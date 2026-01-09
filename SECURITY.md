# Security Best Practices

## Environment Variables

This project uses environment variables to manage sensitive configuration data. **NEVER** commit actual secrets to the repository.

### Setup

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Fill in your actual values in `.env`:
   - `STRIPE_API_KEY`: Your Stripe secret key (get from https://dashboard.stripe.com/apikeys)
   - `EMAIL_*`: Your email service configuration
   - `FOUNDER_KEY`: A secure authentication key you choose
   - `TARGET_IDENTIFIER`: Your target identifier

3. The `.env` file is already included in `.gitignore` and will not be committed

### Using Environment Variables in Code

```python
import os

# Read from environment variables
api_key = os.getenv("STRIPE_API_KEY", "")
founder_key = os.getenv("FOUNDER_KEY", "")
```

## What Was Removed

The following sensitive data has been removed from the codebase:

1. **Hardcoded API keys** - Stripe test/live keys
2. **Personal identifiers** - Names, addresses, financial information
3. **Authentication secrets** - Hardcoded founder keys and passwords
4. **Email addresses** - Personal and business email addresses
5. **Chat logs and documentation** - Removed extensive commented code containing sensitive examples

## Security Checklist

- [x] All API keys moved to environment variables
- [x] Personal information removed from code
- [x] Authentication keys use environment variables
- [x] `.env.example` template created
- [x] `.gitignore` properly configured
- [x] CodeQL security scan passed with 0 alerts

## Production Deployment

When deploying to production:

1. Set all environment variables on your hosting platform
2. Use production API keys (not test keys)
3. Never expose `.env` files publicly
4. Rotate keys regularly
5. Monitor for security alerts

## Reporting Security Issues

If you discover a security vulnerability, please email the project maintainer directly rather than opening a public issue.
