# Quick Reference - Lila in Termux

## 🚀 Getting Lila Live - The Essential Commands

### First Time Setup
```bash
# 1. Update Termux
pkg update && pkg upgrade

# 2. Install Python and Git
pkg install python git

# 3. Clone repository (if needed)
git clone https://github.com/mymlogicofficial-collab/WE-ii.git
cd WE-ii

# 4. Install Python dependencies
pip install fastapi uvicorn python-multipart
```

### Running Lila

**One Command to Rule Them All:**
```bash
bash run_lila.sh
```

**Or manually:**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

**With auto-reload (for development):**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Testing Lila

**Test the modules first:**
```bash
python3 test_lila.py
```

**Test the chat endpoint:**
```bash
# In a new Termux session (swipe from left → New Session)
curl -X POST http://localhost:8000/chat \
     -H 'Content-Type: application/json' \
     -d '{"message": "Hello Lila"}'
```

### Common Tasks

**Pull latest code:**
```bash
git pull origin main
```

**Reload after code changes:**
- If using `--reload` flag: Just save the file, auto-reloads
- Otherwise: Press `Ctrl+C`, then `bash run_lila.sh`

**Kill the server:**
```bash
# Press Ctrl+C in the terminal running the server
# Or kill all uvicorn processes:
pkill -f uvicorn
```

**Check if server is running:**
```bash
ps aux | grep uvicorn
```

**Change port if 8000 is busy:**
```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```

### Useful Termux Tips

**Keep session alive:**
```bash
# Install and use tmux for persistent sessions
pkg install tmux
tmux new -s lila
# Now run: bash run_lila.sh
# Detach: Ctrl+B then D
# Re-attach: tmux attach -t lila
```

**View logs in real-time:**
```bash
# Server logs appear in the terminal running uvicorn
# Or redirect to file:
uvicorn main:app --host 0.0.0.0 --port 8000 2>&1 | tee lila.log
```

**Access from phone browser:**
```
http://localhost:8000/docs
```

### Troubleshooting

**Module not found?**
```bash
pip install --upgrade fastapi uvicorn python-multipart
```

**Import errors?**
```bash
python3 test_lila.py  # Run diagnostics
```

**Port already in use?**
```bash
pkill -f uvicorn
# Then try again
```

**Permission denied?**
```bash
chmod +x run_lila.sh
chmod +x test_lila.py
```

### Quick Test Sequence

```bash
# 1. Test modules
python3 test_lila.py

# 2. Start server (in one session)
bash run_lila.sh

# 3. Test API (in another session - swipe left, "New Session")
curl -X POST http://localhost:8000/chat \
     -H 'Content-Type: application/json' \
     -d '{"message": "status"}'
```

### Expected Output When Running

```
=========================================
     LILA PLATFORM - BOOT SEQUENCE      
=========================================

[1/3] Checking Python dependencies...
[2/3] Verifying Lila modules...
✓ Lila modules loaded successfully

[3/3] Starting Lila Platform...

=========================================
  Lila Status: ONLINE
  Mirror Status: HEAVY
  Target: KIDS_PROJECT
  Mode: TACTICAL_PARTNER
=========================================

Access the API at: http://localhost:8000
```

---

**That's it! Lila is live. 🎯**
