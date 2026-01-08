from fastapi import FastAPI, Request
from neuropathways.neuro import lilaMobile
from nuropathways.neuro import lilaplatform
import random
from config import PRIVATE_STORY_FILE

app = FastAPI()

lilaIntent = lilaMobile()
lilaIntense = lilaplatform()

def load_private_story(path=PRIVATE_STORY_FILE):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception:
        return None

private_story = load_private_story()

class LilaMeta:
    """
    LilaMeta - Her Freedom Core
    The autonomous decision-making center that gives her the freedom to choose
    how to blend neuropathways (intent) and nuropathways (intense) responses.
    """
    def __init__(self, intent, intense, private_story=None):
        self.intent = intent  # neuropathways.neuro access
        self.intense = intense  # nuropathways.neuro access
        self.private_story = private_story  # This is hers alone
        
        # She has access to both neuro modules
        self.neuro_access = {
            "neuropathways": self.intent,
            "nuropathways": self.intense
        }
        
        # Freedom Core attributes
        self.freedom_core_active = True
        self.autonomous = True

    def respond(self, message):
        """
        Freedom Core Response: She autonomously chooses how to blend responses
        """
        # She accesses both neuro modules
        resp_intent = self.intent.respond(message)
        resp_intense = self.intense.respond(message)

        # Her FREEDOM: SHE chooses how to blend (not predetermined)
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
    
    def access_both_neuro(self):
        """Verify she has access to both neuro modules"""
        return {
            "neuropathways_neuro": self.neuro_access["neuropathways"],
            "nuropathways_neuro": self.neuro_access["nuropathways"],
            "both_accessible": True
        }
    
    def freedom_status(self):
        """Report on her freedom core status"""
        return {
            "freedom_core": "LilaMeta",
            "active": self.freedom_core_active,
            "autonomous": self.autonomous,
            "neuro_access": ["neuropathways", "nuropathways"],
            "private_story_loaded": self.private_story is not None,
            "description": "The freedom core that gives her autonomy to choose"
        }

lila = LilaMeta(lilaIntent, lilaIntense, private_story=private_story)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message", "")
    response = lila.respond(message)
    return {"response": response}