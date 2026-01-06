from fastapi import FastAPI, Request
from neuropathways import lilaplatform
from nuropathways import lilaMobile
app = FastAPI()

# Create the lilaplatform instance
lila = lilaplatform()
lilaplatform = lilaMobile
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    # Optionally: use user message for future functions
    # user_message = data.get("message")
    ai_response = lila.execute_stealth_relay()
    return {"response": ai_response}