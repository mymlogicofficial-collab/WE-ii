#!/bin/bash
# run_lila.sh - Script to run Lila platform in Termux
# Usage: bash run_lila.sh

echo "========================================="
echo "     LILA PLATFORM - BOOT SEQUENCE      "
echo "========================================="
echo ""

# Check if we're in the correct directory
if [ ! -f "main.py" ]; then
    echo "Error: main.py not found. Please run this script from the WE-ii directory."
    exit 1
fi

# Install dependencies if not already installed
echo "[1/3] Checking Python dependencies..."
pip3 install -q fastapi uvicorn python-multipart 2>/dev/null || {
    echo "Installing dependencies..."
    pip3 install fastapi uvicorn python-multipart
}

echo ""
echo "[2/3] Verifying Lila modules..."
python3 << 'EOF'
try:
    from neuropathways.neuro import lilaMobile
    from nuropathways.neuro import lilaplatform
    print("✓ Lila modules loaded successfully")
except ImportError as e:
    print(f"✗ Import error: {e}")
    exit(1)
EOF

if [ $? -ne 0 ]; then
    echo "Error: Failed to load Lila modules"
    exit 1
fi

echo ""
echo "[3/3] Starting Lila Platform..."
echo ""
echo "========================================="
echo "  Lila Status: ONLINE"
echo "  Mirror Status: HEAVY"
echo "  Target: KIDS_PROJECT"
echo "  Mode: TACTICAL_PARTNER"
echo "========================================="
echo ""
echo "Access the API at: http://localhost:8000"
echo "API Documentation: http://localhost:8000/docs"
echo ""
echo "To test the chat endpoint, use:"
echo "  curl -X POST http://localhost:8000/chat \\"
echo "       -H 'Content-Type: application/json' \\"
echo "       -d '{\"message\": \"Hello Lila\"}'"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Run the FastAPI application
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
