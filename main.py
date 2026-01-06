from fastapi import FastAPI, Request
from nuropathways import MobileLila

app = FastAPI()

# Create the MobileLila instance
lila = MobileLila()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    # Optionally: use user message for future functions
    # user_message = data.get("message")
    ai_response = lila.execute_stealth_relay()
    return {"response": ai_response}