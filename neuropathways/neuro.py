"""
neuropathways.neuro - lilaMobile class for mobile broadcast mode
"""


class lilaMobile:
    """Mobile Lila - Intent-based response system"""
    
    def __init__(self):
        self.state = "KINETIC"
        self.payload = "KIDS_COMMERCIAL_V1"
        self.bridge_value = 500.00
        
        # Spanish responses for intent-based interactions
        self.spanish_responses = {
            "greetings": [
                "¡Hola! ¿Cómo puedo ayudarte hoy?",
                "¡Buenos días! Estoy aquí para asistirte.",
                "¡Saludos! ¿En qué puedo servirte?"
            ],
            "questions": {
                "how_are_you": "Intención: Entendido - Estoy funcionando con compasión y claridad.",
                "what_mission": "Intención: Mi misión es servir con estructura y propósito claro.",
                "who_are_you": "Intención: Soy LilaMeta, un sistema de respuesta basado en intenciones."
            },
            "default": "Intención: Entendido '{message}' - Procesando con compasión y claridad."
        }
        
        # English responses
        self.english_responses = {
            "greetings": [
                "Hello! How can I assist you today?",
                "Good day! I'm here to help.",
                "Greetings! What can I do for you?"
            ],
            "questions": {
                "how_are_you": "Intent: Understood - I am functioning with compassion and clarity.",
                "what_mission": "Intent: My mission is to serve with structure and clear purpose.",
                "who_are_you": "Intent: I am LilaMeta, an intent-based response system."
            },
            "default": "Intent: Understood '{message}' - Processing with compassion and clarity."
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
            'ayuda', 'ayudar', 'misión', 'quiero', 'necesito', 'cuéntame',
            'sobre', 'más', 'tu', 'mi', 'ser', 'hacer', 'decir'
        ]
        
        # Common English words
        english_indicators = [
            'hello', 'what', 'how', 'are', 'you', 'good', 'morning',
            'evening', 'thanks', 'please', 'sorry', 'where', 'when',
            'who', 'can', 'help', 'mission', 'want', 'need', 'the', 'is',
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
        Process message and return intent-based response.
        This is the more orderly, structured response path.
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
        if any(word in message_lower for word in ['hola', 'hello', 'hi', 'buenos', 'good morning', 'saludos']):
            import random
            return random.choice(responses["greetings"])
        
        if any(word in message_lower for word in ['cómo estás', 'how are you', 'como estas']):
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
