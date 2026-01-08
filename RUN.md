# Running WE-ii Main Application

## Prerequisites

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the FastAPI Server

```bash
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`

## API Endpoint

### POST /chat

Send a JSON request with a message:

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello!"}'
```

Response format:
```json
{
  "response": "Intent: Understood 'Hello!' - Processing with compassion and clarity."
}
```

## Architecture

- **lilaMobile** (from `neuropathways.neuro`): Intent-based, orderly response system
- **lilaplatform** (from `nuropathways.neuro`): Intense, unfiltered response system
- **LilaMeta**: Blends both response types with creative logic
- **Private Story**: Loaded from `Private.md<{--for WE-ii ONLY--}=>{[83]}` for context

## Testing

Test the core logic without running the server:

```python
from neuropathways.neuro import lilaMobile
from nuropathways.neuro import lilaplatform

intent = lilaMobile()
intense = lilaplatform()

print(intent.respond("Test message"))
print(intense.respond("Test message"))
```
