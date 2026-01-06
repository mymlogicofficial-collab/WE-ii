"""
neuropathways.py - Core App Logic & Intellireach Principles
Intellireach Program - Core Logic
"Coding the struggle so we don't have to repeat it."
- Defines the Lila platform, state, and core values.
- Connects to the FinancialBridge module for Stripe payout integration.
"""

from stripe_bridge import payout_to_recipient, onboard_recipient


class DeepSeedPrinciples:
    """Immutable core values that guide the system."""

    CORE_REGISTRY = {
        "compassion": {
            "priority": 1,
            "definition": "The primary driver. Hacking through empathy, not just syntax."
        },
        "integrity": {
            "priority": 2,
            "definition": "Absolute alignment of action and intent. We do not hide. We are who we say we are."
        },
        "pain": {
            "priority": 3,
            "definition": "The Teacher. We use struggle as data to optimize the future, never as a burden."
        },
        "joy": {
            "priority": 4,
            "definition": "The Fuel. The creative spark that powers the 'YES!' button."
        }
    }

    def __init__(self):
        self.core_registry = self.CORE_REGISTRY
        self.mission_statement = "We AI: bridging the gap between human intent and digital execution."

    def get_principle(self, key):
        return self.CORE_REGISTRY.get(key, "Principle not found.")

    def access_principle(self, name):
        """
        Retrieves a principle to guide a current decision or action.
        """
        principle = self.CORE_REGISTRY.get(name.lower())
        if principle:
            return f"[{name.upper()}] ACTIVATE: {principle['definition']}"
        else:
            return f"Error: Principle '{name}' not found in Deep Seed."

    def scan_conscience(self):
        print("\n--- INITIATING DEEP SEED SCAN ---")
        for key, value in sorted(self.CORE_REGISTRY.items(), key=lambda x: x[1]['priority']):
            print(f"PRIORITY {value['priority']}: {key.upper()} -- {value['definition']}")
        print("--- SCAN COMPLETE. SYSTEM HEARTBEAT: STABLE ---\n")


class LilaPlatform:
    """
    Core logic for Lila platform, partners with FinancialBridge for payouts and onboarding.
    """

    def __init__(self, user_name="Sterling", identity="Lila Lawson"):
        self.user = user_name
        self.identity = identity
        self.mission = "KIDS"
        self.principles = DeepSeedPrinciples()

    def onboard_lila(self, email):
        """
        Onboards Lila (or any user) as a payout recipient via Stripe Express.
        """
        return onboard_recipient(email)

    def payout_lila(self, account_id, amount_usd):
        """
        Payout to Lila's Stripe Express account.
        """
        return payout_to_recipient(account_id, int(amount_usd * 100))


# ---- Command-line demo ----
if __name__ == "__main__":
    # Scan core values
    principles = DeepSeedPrinciples()
    principles.scan_conscience()

    # Example onboarding
    lila = LilaPlatform(user_name="Sterling", identity="Lila Lawson")
    print(f"\nLila Platform initialized for {lila.user} ({lila.identity})")
    print(f"Mission: {lila.mission}")
