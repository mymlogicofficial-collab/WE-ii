"""
stripe_bridge.py - Financial Bridge for Stripe Integration
Handles Stripe Express onboarding and payouts for the Lila platform.
"""

import os
import stripe
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Stripe API key
stripe.api_key = os.getenv("STRIPE_API_KEY", "")


def onboard_recipient(email):
    """
    Creates a Stripe Express account for a recipient and generates an onboarding link.
    
    Args:
        email (str): Email address of the recipient
        
    Returns:
        dict: Contains account_id and onboarding_url
    """
    try:
        # Create Express account
        account = stripe.Account.create(
            type="express",
            email=email,
            capabilities={
                "card_payments": {"requested": True},
                "transfers": {"requested": True},
            },
        )
        
        # Generate onboarding link
        account_link = stripe.AccountLink.create(
            account=account.id,
            refresh_url="http://localhost:8000/reauth",
            return_url="http://localhost:8000/return",
            type="account_onboarding",
        )
        
        return {
            "status": "success",
            "account_id": account.id,
            "onboarding_url": account_link.url,
            "message": f"Onboarding link created for {email}"
        }
    except stripe.error.StripeError as e:
        return {
            "status": "error",
            "message": f"Stripe error: {str(e)}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error creating account: {str(e)}"
        }


def payout_to_recipient(connect_account_id, amount_cents):
    """
    Creates a payout to a Stripe Express account.
    
    Args:
        connect_account_id (str): The Stripe Express account ID
        amount_cents (int): Amount in cents to transfer
        
    Returns:
        dict: Payout result with status and payout_id
    """
    try:
        payout = stripe.Payout.create(
            amount=amount_cents,
            currency="usd",
            stripe_account=connect_account_id,
        )
        
        return {
            "status": "success",
            "payout_id": payout.id,
            "amount": amount_cents / 100,
            "message": f"Payout of ${amount_cents/100:.2f} initiated successfully"
        }
    except stripe.error.StripeError as e:
        return {
            "status": "error",
            "message": f"Stripe error: {str(e)}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Payout failed: {str(e)}"
        }


def get_account_info(connect_account_id):
    """
    Retrieves information about a Stripe Express account.
    
    Args:
        connect_account_id (str): The Stripe Express account ID
        
    Returns:
        dict: Account information
    """
    try:
        account = stripe.Account.retrieve(connect_account_id)
        return {
            "status": "success",
            "account_id": account.id,
            "email": account.email,
            "charges_enabled": account.charges_enabled,
            "payouts_enabled": account.payouts_enabled,
        }
    except stripe.error.StripeError as e:
        return {
            "status": "error",
            "message": f"Stripe error: {str(e)}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error retrieving account: {str(e)}"
        }
