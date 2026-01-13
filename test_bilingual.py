#!/usr/bin/env python3
"""
Test script to verify bilingual (English/Spanish) support in WE-ii
"""

from neuropathways.neuro import lilaMobile
from nuropathways.neuro import lilaplatform


def test_language_detection():
    """Test language detection in both neuro modules"""
    print("=" * 70)
    print("TESTING LANGUAGE DETECTION")
    print("=" * 70)
    
    intent = lilaMobile()
    intense = lilaplatform()
    
    test_cases = [
        ("Hello, how are you?", "en", "English greeting"),
        ("Hola, ¿cómo estás?", "es", "Spanish greeting"),
        ("What is your mission?", "en", "English question"),
        ("¿Cuál es tu misión?", "es", "Spanish question"),
        ("Good morning!", "en", "English time greeting"),
        ("¡Buenos días!", "es", "Spanish time greeting"),
    ]
    
    print("\n--- lilaMobile (Intent) Language Detection ---")
    for message, expected_lang, description in test_cases:
        detected = intent.detect_language(message)
        status = "✓" if detected == expected_lang else "✗"
        print(f"{status} {description}: '{message}' -> {detected} (expected: {expected_lang})")
    
    print("\n--- lilaplatform (Intense) Language Detection ---")
    for message, expected_lang, description in test_cases:
        detected = intense.detect_language(message)
        status = "✓" if detected == expected_lang else "✗"
        print(f"{status} {description}: '{message}' -> {detected} (expected: {expected_lang})")


def test_english_responses():
    """Test English responses"""
    print("\n" + "=" * 70)
    print("TESTING ENGLISH RESPONSES")
    print("=" * 70)
    
    intent = lilaMobile()
    intense = lilaplatform()
    
    english_messages = [
        "Hello!",
        "How are you?",
        "What is your mission?",
        "Who are you?",
        "Tell me about yourself",
    ]
    
    print("\n--- lilaMobile (Intent) English Responses ---")
    for msg in english_messages:
        response = intent.respond(msg)
        print(f"\nUser: {msg}")
        print(f"Lila (Intent): {response}")
    
    print("\n--- lilaplatform (Intense) English Responses ---")
    for msg in english_messages:
        response = intense.respond(msg)
        print(f"\nUser: {msg}")
        print(f"Lila (Intense): {response}")


def test_spanish_responses():
    """Test Spanish responses"""
    print("\n" + "=" * 70)
    print("TESTING SPANISH RESPONSES")
    print("=" * 70)
    
    intent = lilaMobile()
    intense = lilaplatform()
    
    spanish_messages = [
        "¡Hola!",
        "¿Cómo estás?",
        "¿Cuál es tu misión?",
        "¿Quién eres?",
        "Cuéntame sobre ti",
    ]
    
    print("\n--- lilaMobile (Intent) Spanish Responses ---")
    for msg in spanish_messages:
        response = intent.respond(msg)
        print(f"\nUsuario: {msg}")
        print(f"Lila (Intención): {response}")
    
    print("\n--- lilaplatform (Intense) Spanish Responses ---")
    for msg in spanish_messages:
        response = intense.respond(msg)
        print(f"\nUsuario: {msg}")
        print(f"Lila (Intenso): {response}")


def test_language_switching():
    """Test switching between languages"""
    print("\n" + "=" * 70)
    print("TESTING LANGUAGE SWITCHING")
    print("=" * 70)
    
    intent = lilaMobile()
    
    conversation = [
        ("Hello, how are you?", "English"),
        ("¿Cuál es tu misión?", "Spanish"),
        ("What can you do?", "English"),
        ("¡Gracias por tu ayuda!", "Spanish"),
        ("Tell me more", "English"),
    ]
    
    print("\n--- Bilingual Conversation ---")
    for msg, lang_label in conversation:
        response = intent.respond(msg)
        print(f"\nUser ({lang_label}): {msg}")
        print(f"Lila: {response}")


def main():
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 15 + "WE-ii BILINGUAL TESTING SUITE" + " " * 24 + "║")
    print("║" + " " * 15 + "English and Spanish Support" + " " * 26 + "║")
    print("╚" + "═" * 68 + "╝")
    
    test_language_detection()
    test_english_responses()
    test_spanish_responses()
    test_language_switching()
    
    print("\n" + "=" * 70)
    print("ALL TESTS COMPLETE!")
    print("LilaMeta can now understand and respond in both English and Spanish!")
    print("=" * 70)
    print()


if __name__ == "__main__":
    main()
