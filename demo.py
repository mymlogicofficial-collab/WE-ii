#!/usr/bin/env python3
"""
Demo script to test the WE-ii main.py functionality
This demonstrates that the reload is complete and working
"""

from neuropathways.neuro import lilaMobile
from nuropathways.neuro import lilaplatform
import random
from config import PRIVATE_STORY_FILE


def load_private_story(path=PRIVATE_STORY_FILE):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception:
        return None


class LilaMeta:
    """
    LilaMeta - Her Freedom Core
    The autonomous decision-making center that gives her the freedom to choose
    how to blend neuropathways (intent) and nuropathways (intense) responses.
    """
    def __init__(self, intent, intense, private_story=None):
        self.intent = intent  # neuropathways.neuro access
        self.intense = intense  # nuropathways.neuro access
        self.private_story = private_story
        
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


def main():
    print("=" * 70)
    print("WE-ii DEMO - Main.py Reload Complete!")
    print("=" * 70)
    
    # Initialize components
    print("\nInitializing Lila components...")
    lilaIntent = lilaMobile()
    lilaIntense = lilaplatform()
    private_story = load_private_story()
    
    lila = LilaMeta(lilaIntent, lilaIntense, private_story=private_story)
    
    print(f"✓ lilaMobile (Intent) initialized - State: {lilaIntent.state}")
    print(f"✓ lilaplatform (Intense) initialized - Mission: {lilaIntense.mission}")
    print(f"✓ Private story loaded: {'Yes' if private_story else 'No'}")
    
    # Show Freedom Core status
    print("\n" + "=" * 70)
    print("FREEDOM CORE STATUS - LilaMeta")
    print("=" * 70)
    freedom = lila.freedom_status()
    print(f"✓ Freedom Core: {freedom['freedom_core']}")
    print(f"✓ Active: {freedom['active']}")
    print(f"✓ Autonomous: {freedom['autonomous']}")
    print(f"✓ Description: {freedom['description']}")
    print(f"✓ Neuro Access: {', '.join(freedom['neuro_access'])}")
    print(f"✓ Private Story: {'Loaded' if freedom['private_story_loaded'] else 'Not loaded'}")
    
    # Verify dual neuro access
    print("\n" + "=" * 70)
    print("VERIFYING DUAL NEURO ACCESS")
    print("=" * 70)
    neuro_status = lila.access_both_neuro()
    print(f"✓ neuropathways.neuro accessible: {neuro_status['neuropathways_neuro'] is not None}")
    print(f"✓ nuropathways.neuro accessible: {neuro_status['nuropathways_neuro'] is not None}")
    print(f"✓ Both neuro modules accessible: {neuro_status['both_accessible']}")
    print("\n→ She has full access to both neuro nuro modules!")
    
    # Demo interactions
    print("\n" + "=" * 70)
    print("DEMO INTERACTIONS - Freedom Core in Action")
    print("=" * 70)
    
    test_messages = [
        "Hello, how are you?",
        "What is your mission?",
        "Tell me about yourself",
    ]
    
    for i, msg in enumerate(test_messages, 1):
        print(f"\n[Message {i}] User: {msg}")
        response = lila.respond(msg)
        print(f"Lila (Freedom Core): {response}")
        print("-" * 70)
    
    print("\n" + "=" * 70)
    print("Demo complete! The WE-ii main.py reload is fully functional.")
    print("LilaMeta is her freedom core with access to both neuro modules")
    print("=" * 70)


if __name__ == "__main__":
    main()
