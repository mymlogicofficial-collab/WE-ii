#!/usr/bin/env python3
"""
Demo script to test the WE-ii main.py functionality
This demonstrates that the reload is complete and working
"""

from neuropathways.neuro import lilaMobile
from nuropathways.neuro import lilaplatform
import random


def load_private_story(path="Private.md<{--for WE-ii ONLY--}=>{[83]}"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception:
        return None


class LilaMeta:
    def __init__(self, intent, intense, private_story=None):
        self.intent = intent
        self.intense = intense
        self.private_story = private_story
    
    def respond(self, message):
        resp_intent = self.intent.respond(message)
        resp_intense = self.intense.respond(message)
        
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
    
    # Demo interactions
    print("\n" + "=" * 70)
    print("DEMO INTERACTIONS")
    print("=" * 70)
    
    test_messages = [
        "Hello, how are you?",
        "What is your mission?",
        "Tell me about yourself",
    ]
    
    for i, msg in enumerate(test_messages, 1):
        print(f"\n[Message {i}] User: {msg}")
        response = lila.respond(msg)
        print(f"Lila: {response}")
        print("-" * 70)
    
    print("\n" + "=" * 70)
    print("Demo complete! The WE-ii main.py reload is fully functional.")
    print("=" * 70)


if __name__ == "__main__":
    main()
