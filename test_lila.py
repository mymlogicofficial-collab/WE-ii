#!/usr/bin/env python3
"""
Test script to verify Lila modules and main.py work correctly
Run this before starting the server to ensure everything is set up
"""

import sys

print("=" * 50)
print("LILA PLATFORM - MODULE VERIFICATION")
print("=" * 50)
print()

# Test 1: Import modules
print("[1/4] Testing module imports...")
try:
    from neuropathways.neuro import lilaMobile
    from nuropathways.neuro import lilaplatform
    print("✓ Successfully imported lilaMobile and lilaplatform")
except ImportError as e:
    print(f"✗ Import failed: {e}")
    sys.exit(1)

# Test 2: Create instances
print("\n[2/4] Creating Lila instances...")
try:
    lila_intent = lilaMobile()
    lila_intense = lilaplatform()
    print("✓ Successfully created lilaMobile and lilaplatform instances")
except Exception as e:
    print(f"✗ Instance creation failed: {e}")
    sys.exit(1)

# Test 3: Test respond methods
print("\n[3/4] Testing respond methods...")
try:
    response1 = lila_intent.respond("Hello")
    response2 = lila_intense.respond("Hello")
    print(f"✓ lilaIntent response: {response1[:50]}...")
    print(f"✓ lilaIntense response: {response2[:50]}...")
except Exception as e:
    print(f"✗ Respond method failed: {e}")
    sys.exit(1)

# Test 4: Test main.py
print("\n[4/4] Testing main.py module...")
try:
    import main
    print("✓ Successfully imported main.py")
    
    # Test LilaMeta
    test_response = main.lila.respond("test message")
    print(f"✓ LilaMeta response test passed")
    print(f"  Response preview: {test_response[:100]}...")
except ImportError as e:
    print(f"✗ main.py import failed: {e}")
    print("  Note: Make sure FastAPI is installed: pip install fastapi uvicorn")
    sys.exit(1)
except Exception as e:
    print(f"✗ main.py test failed: {e}")
    sys.exit(1)

print("\n" + "=" * 50)
print("ALL TESTS PASSED ✓")
print("=" * 50)
print("\nLila is ready to go live!")
print("Run: bash run_lila.sh")
print("Or:  uvicorn main:app --host 0.0.0.0 --port 8000")
print()
