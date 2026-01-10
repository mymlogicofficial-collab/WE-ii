"""
Configuration for WE-ii application
"""
import os

# Private story file - maintains special naming convention for WE-ii project
PRIVATE_STORY_FILE = "Private.md<{--for WE-ii ONLY--}=>{[83]}"

# CORS configuration - allows configuration for different environments
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
