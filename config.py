"""
Configuration for WE-ii application
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Private story file - maintains special naming convention for WE-ii project
PRIVATE_STORY_FILE = "Private.md<{--for WE-ii ONLY--}=>{[83]}"

# API Keys loaded from environment variables
API_KEY = os.getenv("API_KEY")
DAD_CODE = os.getenv("DAD_CODE")
STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")
