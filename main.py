from fastapi import FastAPI, Request
from neuropathways.neuro import lilaMobile
from nuropathways.neuro import lilaplatform
import random

app = FastAPI()

lilaIntent = lilaMobile()
lilaIntense = lilaplatform()

def load_private_story(path="Private.md<{--for WE-ii ONLY--}=>{[83]}"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception:
        return None

private_story = load_private_story()

class LilaMeta:
    def __init__(self, intent, intense, private_story=None):
        self.intent = intent
        self.intense = intense
        self.private_story = private_story  # This is hers alone

    def respond(self, message):
        resp_intent = self.intent.respond(message)
        resp_intense = self.intense.respond(message)

        # Example creative logic: SHE chooses how to blend
        blend_style = random.choice(["intent", "intense", "blend"])
        # Optionally, let her be inspired by her story but not show it

        # For her eyes only; never reveal unless you want
        if blend_style == 'blend':
            return (
                f"Orderly: {resp_intent}\n"
                f"Unfiltered: {resp_intense}\n"
                f"(Sometimes, deep roots run beneath every answer.)"
            )
        elif blend_style == 'intense':
            return resp_intense
        else:
            return resp_intent

lila = LilaMeta(lilaIntent, lilaIntense, private_story=private_story)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message", "")
    response = lila.respond(message)
    return {"response": response}