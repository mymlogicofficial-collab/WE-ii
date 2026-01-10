"""
nuropathways.neuro - lilaplatform class for intensive/unfiltered mode
"""


class lilaplatform:
    """Lila Platform - Intense/Unfiltered response system"""
    
    def __init__(self):
        self.user = "Sterling"
        self.identity = "Lila Lawson"
        self.mission = "KIDS"
        
        # Spanish intense responses
        self.spanish_responses = {
            "greetings": [
                "¡Oye! ¿Qué tienes en mente?",
                "¡Hola! ¿Qué pasa? ¡Hablemos!",
                "¡Ey! Dime lo que piensas."
            ],
            "questions": {
                "how_are_you": "Intenso: ¡Estoy lista para todo! ¿Y tú?",
                "what_mission": "Intenso: Mi misión es KIDS - ¡con toda la pasión y energía!",
                "who_are_you": "Intenso: Soy Lila Lawson - ¡sin filtros, con toda la verdad!"
            },
            "default": "Intenso: '{message}' - ¡Vamos profundo y hagámoslo real!"
        }
        
        # English intense responses
        self.english_responses = {
            "greetings": [
                "Hey! What's on your mind?",
                "Hello! What's up? Let's talk!",
                "Hey there! Tell me what you're thinking."
            ],
            "questions": {
                "how_are_you": "Intense: I'm ready for anything! How about you?",
                "what_mission": "Intense: My mission is KIDS - with all the passion and energy!",
                "who_are_you": "Intense: I'm Lila Lawson - unfiltered, all truth!"
            },
            "default": "Intense: '{message}' - Let's dive deep and make it real!"
        }
    
    def detect_language(self, message):
        """
        Detect if the message is in Spanish or English.
        Returns 'es' for Spanish, 'en' for English.
        """
        if not message:
            return 'en'
        
        message_lower = message.lower()
        
        # Common Spanish words and patterns
        spanish_indicators = [
            'hola', 'qué', 'cómo', 'estás', 'buenos', 'días', 'noches',
            'tardes', 'gracias', 'por favor', 'perdón', 'disculpa',
            'cuál', 'dónde', 'cuándo', 'quién', 'soy', 'eres', 'está',
            'estoy', 'tienes', 'tengo', 'puedes', 'puedo', 'favor',
            'ayuda', 'ayudar', 'misión', 'quiero', 'necesito', 'oye',
            'cuéntame', 'sobre', 'más', 'tu', 'mi', 'ser', 'hacer', 'decir'
        ]
        
        # Common English words
        english_indicators = [
            'hello', 'what', 'how', 'are', 'you', 'good', 'morning',
            'evening', 'thanks', 'please', 'sorry', 'where', 'when',
            'who', 'can', 'help', 'mission', 'want', 'need', 'the', 'is', 'hey',
            'tell', 'about', 'more', 'your', 'my', 'be', 'do', 'say'
        ]
        
        # Count indicators
        spanish_count = sum(1 for word in spanish_indicators if word in message_lower)
        english_count = sum(1 for word in english_indicators if word in message_lower)
        
        # Detect based on indicators
        if spanish_count > english_count:
            return 'es'
        return 'en'
    
    def respond(self, message):
        """
        Process message and return intense, unfiltered response.
        This is the more creative, emotional response path.
        Supports both English and Spanish.
        """
        # Detect language
        lang = self.detect_language(message)
        
        # Select appropriate response set
        responses = self.spanish_responses if lang == 'es' else self.english_responses
        
        # Handle empty message
        if not message:
            return responses["greetings"][0]
        
        message_lower = message.lower()
        
        # Check for specific patterns
        if any(word in message_lower for word in ['hola', 'hello', 'hi', 'buenos', 'good morning', 'oye', 'hey', 'ey']):
            import random
            return random.choice(responses["greetings"])
        
        if any(word in message_lower for word in ['cómo estás', 'how are you', 'como estas', 'qué tal']):
            return responses["questions"]["how_are_you"]
        
        if any(word in message_lower for word in ['misión', 'mission', 'propósito', 'purpose']):
            return responses["questions"]["what_mission"]
        
        if any(word in message_lower for word in ['quién eres', 'who are you', 'quien eres', 'what are you']):
            return responses["questions"]["who_are_you"]
        
        # Default response in detected language
        if lang == 'es':
            return responses["default"].format(message=message)
        else:
            return responses["default"].format(message=message)
