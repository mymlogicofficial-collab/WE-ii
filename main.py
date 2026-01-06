from fastapi import FastAPI, Request
from nuropathways import #LilaMobile

app = FastAPI()

from nuropathways import Lila_Kinetic

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")
    # Example: call a method on Lila_Kinetic (pick the right method)
    ai_response = Lila_Kinetic.execute_stealth_relay()
    return {"response": ai_response}