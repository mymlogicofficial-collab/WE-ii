#!/usr/bin/env python3
"""
Interactive bilingual demo for LilaMeta
Run this to chat with LilaMeta in English or Spanish!
"""

from neuropathways.neuro import lilaMobile
from nuropathways.neuro import lilaplatform
import random


class LilaMeta:
    """
    LilaMeta - Her Freedom Core with Bilingual Support
    """
    def __init__(self, intent, intense):
        self.intent = intent
        self.intense = intense
        self.freedom_core_active = True
        self.autonomous = True
    
    def respond(self, message):
        """Freedom Core Response: Blends responses autonomously"""
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


def print_banner():
    print("\n" + "═" * 70)
    print("║" + " " * 15 + "🌟 LilaMeta Bilingual Demo 🌟" + " " * 21 + "║")
    print("║" + " " * 10 + "Chat with me in English or Spanish!" + " " * 18 + "║")
    print("═" * 70)
    print("\nType 'exit', 'quit', or 'salir' to end the conversation.")
    print("Type 'help' or 'ayuda' for tips on what to ask.\n")


def show_help():
    print("\n" + "─" * 70)
    print("💡 Try asking me:")
    print("  English: 'Hello!', 'How are you?', 'What is your mission?'")
    print("  Spanish: '¡Hola!', '¿Cómo estás?', '¿Cuál es tu misión?'")
    print("\nI can understand both languages and will respond accordingly!")
    print("─" * 70 + "\n")


def main():
    # Initialize LilaMeta
    intent = lilaMobile()
    intense = lilaplatform()
    lila = LilaMeta(intent, intense)
    
    print_banner()
    
    # Interactive loop
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            # Check for exit commands
            if user_input.lower() in ['exit', 'quit', 'salir', 'adiós', 'adios', 'bye']:
                print("\nLilaMeta: Goodbye! ¡Hasta luego! 👋\n")
                break
            
            # Check for help commands
            if user_input.lower() in ['help', 'ayuda', '?']:
                show_help()
                continue
            
            # Get response from LilaMeta
            response = lila.respond(user_input)
            print(f"\nLilaMeta: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\nLilaMeta: Goodbye! ¡Hasta luego! 👋\n")
            break
        except Exception as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    main()
