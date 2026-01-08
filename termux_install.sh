#!/bin/bash
# COPY AND PASTE THIS INTO TERMUX
# This is the complete setup in one script

echo "========================================="
echo "   LILA PLATFORM - TERMUX INSTALLER     "
echo "========================================="
echo ""

# Step 1: Update Termux
echo "[1/5] Updating Termux packages..."
pkg update -y && pkg upgrade -y

# Step 2: Install Python and Git
echo ""
echo "[2/5] Installing Python and Git..."
pkg install -y python git

# Step 3: Navigate to repository (assuming already cloned)
echo ""
echo "[3/5] Checking repository..."
if [ ! -d "WE-ii" ]; then
    echo "Cloning repository..."
    git clone https://github.com/mymlogicofficial-collab/WE-ii.git
fi
cd WE-ii

# Step 4: Install Python dependencies
echo ""
echo "[4/5] Installing Python dependencies..."
pip install --upgrade pip
pip install fastapi uvicorn python-multipart

# Step 5: Verify installation
echo ""
echo "[5/5] Verifying installation..."
python3 test_lila.py

# Step 6: Start Lila
echo ""
echo "========================================="
echo "   READY TO START LILA PLATFORM!       "
echo "========================================="
echo ""
echo "Starting Lila in 3 seconds..."
echo "Press Ctrl+C now to cancel, or wait to start..."
sleep 3

bash run_lila.sh
