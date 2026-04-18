# Ara Personal Finance

Single-agent example from the [Ara Hackathon Tour 2026](https://github.com/cyu60/ara-ai-computer) — a chat-based personal finance tracker running on the [Ara](https://ara.so) agentic operating system.

**Links:** [Ara docs](https://docs.ara.so/introduction) · [Ara Hackathon Tour](https://github.com/cyu60/ara-ai-computer) · [DayDreamers](https://daydreamers.live)

Part of the **Aragrams** — reference projects built by [DayDreamers](https://daydreamers.live) to show what's possible with agent-first development.

## What it does

Log expenses via chat in natural language ("coffee $4.50", "uber to airport $35"). The agent:

- Auto-categorizes every expense (food, transport, subscriptions, etc.)
- Persists the ledger as JSON on the sandbox filesystem
- Tracks spending against monthly budget targets
- Answers questions like "how much did I spend on food this week?"
- Sends a weekly spending summary every Sunday at 6 PM UTC

No apps to open, no categories to tap — text the agent like a friend who's good with money.

## Architecture

```
Browser (index.html)
   ↓
/api/run (Vercel serverless function)
   ↓
Ara API (api.ara.so) — Bearer ARA_RUNTIME_KEY
   ↓
finance-tracker subagent running in a sandboxed Python runtime
```

## Local dev

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install ara-sdk
export ARA_ACCESS_TOKEN=<your_token>

python3 app.py setup                           # registers the app → returns APP_ID
python3 app.py deploy --on-existing update     # pushes the agent definition
python3 app.py run --workflow finance-tracker --message "coffee $4.50"
```

## Deploy

This repo is wired to Vercel. On push to `main`:

1. Vercel builds the static frontend + `api/run.js` edge function.
2. The function proxies `/api/run` calls to `https://api.ara.so/v1/apps/<APP_ID>/run` using `ARA_RUNTIME_KEY`.
3. The Ara runtime spins up the `finance-tracker` sandbox on demand.

## License

MIT
