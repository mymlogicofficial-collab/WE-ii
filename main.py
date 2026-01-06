from fastapi import FastAPI, Request
from nuropathways import your_ai_function  # Replace with your actual function/class

app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")
    ai_response = your_ai_function(user_message)  # Update to fit your function
    return {"response": ai_response}
