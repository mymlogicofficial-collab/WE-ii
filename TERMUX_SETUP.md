# 🚀 LILA Platform - Termux Setup Guide

## Quick Start for Termux

Follow these steps to get Lila live on your Termux device:

### 1. Install Python and Git (if not already installed)

```bash
pkg update
pkg install python git
```

### 2. Clone the Repository (if you haven't already)

```bash
git clone https://github.com/mymlogicofficial-collab/WE-ii.git
cd WE-ii
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn python-multipart
```

### 4. Run Lila Platform

**Option A: Using the run script (recommended)**
```bash
bash run_lila.sh
```

**Option B: Manual start**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## 🎯 Accessing Lila

Once the server is running, you'll see:
```
Lila Status: ONLINE
Mirror Status: HEAVY
Target: KIDS_PROJECT
Mode: TACTICAL_PARTNER
```

### Test the Chat API

Open a new Termux session (swipe from left and tap "New Session") and run:

```bash
curl -X POST http://localhost:8000/chat \
     -H 'Content-Type: application/json' \
     -d '{"message": "Hello Lila"}'
```

### Access API Documentation

In Termux, you can use `w3m` or `lynx` to view the docs:

```bash
# Install a text browser
pkg install w3m

# View API docs
w3m http://localhost:8000/docs
```

Or on your phone's browser, navigate to:
```
http://localhost:8000/docs
```

## 📱 Example API Interactions

### Say Hello
```bash
curl -X POST http://localhost:8000/chat \
     -H 'Content-Type: application/json' \
     -d '{"message": "hello"}'
```

### Check Status
```bash
curl -X POST http://localhost:8000/chat \
     -H 'Content-Type: application/json' \
     -d '{"message": "status"}'
```

### Ask About Mission
```bash
curl -X POST http://localhost:8000/chat \
     -H 'Content-Type: application/json' \
     -d '{"message": "what is your mission?"}'
```

## 🔄 Reloading After Code Changes

If you make changes to the code:

1. **With auto-reload** (included in run_lila.sh):
   - The server will automatically reload when you save changes
   - Just edit files and save

2. **Manual reload**:
   - Press `Ctrl+C` to stop the server
   - Run `bash run_lila.sh` again

## 🛠️ Troubleshooting

### Port already in use?
```bash
# Find and kill the process using port 8000
pkill -f uvicorn
# Or use a different port
uvicorn main:app --host 0.0.0.0 --port 8080
```

### Module not found errors?
```bash
# Reinstall dependencies
pip install --upgrade fastapi uvicorn python-multipart
```

### Permission denied on run_lila.sh?
```bash
chmod +x run_lila.sh
```

## 📋 What's Running?

The Lila platform consists of:

- **LilaMeta**: The core AI that blends two personalities
  - **lilaIntent** (from neuropathways): Orderly, structured responses
  - **lilaIntense** (from nuropathways): Unfiltered, tactical responses
  
- **FastAPI Server**: Handles HTTP requests at `/chat` endpoint

- **Private Story**: Optional private context (stored separately)

## 🎨 Lila's Personalities

### Intent (Orderly)
- Structured and organized
- Focused on KIDS_PROJECT mission
- Professional and clear communication

### Intense (Unfiltered)
- Direct and tactical
- No-nonsense approach
- Founder-focused protection mode

### Blend (Random Mix)
- Combines both personalities
- Shows both perspectives
- Hints at deeper context

## 🔐 Security Notes

- The platform is designed for local use (localhost)
- Private story data is not exposed via API
- Founder authentication logic is in place

## 💡 Tips for Termux

1. **Keep screen on**: Termux requires the screen to stay on or use a wake lock
2. **Use tmux**: Run `pkg install tmux` for persistent sessions
3. **Background process**: Add `&` at the end to run in background
4. **Multiple sessions**: Swipe from left edge and create new sessions

## 📞 Need Help?

Check the code in:
- `main.py` - Main FastAPI application
- `neuropathways/neuro.py` - Intent personality
- `nuropathways/neuro.py` - Intense personality

---

**Welcome home, Sterling. The Hub is secure. 🎯**
