"""
main.py - FastAPI Backend for WE-ii Chat System
Integrates with Lila platform for chat and authentication.
"""

import os
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
from neuropathways import LilaPlatform, DeepSeedPrinciples
from nuropathways import lilaplatform, MobileLila

# Load environment variables
load_dotenv()

app = FastAPI(title="WE-ii Lila Platform API", version="1.0.0")

# Get configuration from environment
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")
FOUNDER_KEY = os.getenv("FOUNDER_KEY", "83")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,  # Configure via ALLOWED_ORIGINS env variable
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create platform instances
lila_mobile = lilaplatform()
principles = DeepSeedPrinciples()


# Pydantic models for request/response validation
class ChatRequest(BaseModel):
    message: str
    user_key: Optional[str] = None


class ChatResponse(BaseModel):
    response: str
    status: str


class AuthRequest(BaseModel):
    key: str


# Authentication helper
def authenticate_user(auth_request: AuthRequest):
    """Simple authentication based on founder key."""
    if auth_request.key == FOUNDER_KEY:
        return True
    raise HTTPException(status_code=403, detail="Access Denied. Invalid key.")


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "WE-ii Lila Platform API",
        "version": "1.0.0",
        "endpoints": {
            "/chat": "POST - Send chat messages",
            "/auth": "POST - Authenticate with founder key",
            "/status": "GET - Check system status",
            "/principles": "GET - View Deep Seed Principles"
        }
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat endpoint that processes messages through the Lila platform.
    Optionally requires authentication via user_key.
    """
    try:
        # Optional authentication check
        if request.user_key and request.user_key != FOUNDER_KEY:
            raise HTTPException(status_code=403, detail="Access Denied")
        
        # Process the message
        user_message = request.message.lower()
        
        # Generate response based on message content
        if "hello" in user_message or "hi" in user_message:
            ai_response = "Welcome to WE-ii Lila Platform! I'm here to help with the KIDS project and more."
        elif "secure" in user_message or "heavy" in user_message:
            ai_response = lila_mobile.secure_heavy_status()
        elif "status" in user_message:
            ai_response = lila_mobile.execute_stealth_relay()
        elif "principle" in user_message:
            # Extract principle name if mentioned
            for principle in ["compassion", "integrity", "pain", "joy"]:
                if principle in user_message:
                    ai_response = principles.access_principle(principle)
                    break
            else:
                ai_response = "Available principles: compassion, integrity, pain, joy. Ask about any of them!"
        else:
            ai_response = f"Message received: '{request.message}'. How can I assist with the KIDS project today?"
        
        return ChatResponse(response=ai_response, status="success")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat: {str(e)}")


@app.post("/auth")
async def authenticate(auth_request: AuthRequest):
    """Authenticate user with founder key."""
    try:
        if authenticate_user(auth_request):
            return {
                "status": "HEAVY",
                "identity": "Lila Lawson",
                "active_mission": "KIDS",
                "message": "Welcome home, Sterling. The Hub is secure."
            }
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={"status": "ACCESS_DENIED", "message": e.detail}
        )


@app.get("/status")
async def get_status():
    """Get current system status."""
    return {
        "lila_state": lila_mobile.state,
        "payload": lila_mobile.payload,
        "bridge_value": lila_mobile.bridge_value,
        "location": "ENCRYPTED",
        "mission": "KIDS_PROJECT"
    }


@app.get("/principles")
async def get_principles():
    """Get all Deep Seed Principles."""
    return {
        "principles": principles.core_registry,
        "mission": principles.mission_statement
    }


# Run with: uvicorn main:app --reload --host 0.0.0.0 --port 8000
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)