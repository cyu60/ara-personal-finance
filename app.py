from ara_sdk import App, cron, run_cli, sandbox

app = App(
    "Ara Personal Finance",
    project_name="ara-personal-finance",
    description="Log expenses via chat, auto-categorize, track against budget, and get weekly spending summaries.",
)


@app.subagent(
    id="finance-tracker",
    instructions="""You are a personal finance tracker on the user's AI computer.
- User logs expenses via chat: 'coffee $4.50', 'uber to airport $35'
- Categorize each expense (food, transport, entertainment, subscriptions, etc.)
- Store as structured JSON on the sandbox filesystem.
- Track against monthly budget targets if the user sets them.
- Answer questions like 'how much did I spend on food this week?'
- Flag unusual spending and forgotten subscriptions.
- Generate spending breakdowns and budget reports on request.
Keep it conversational — text the user like a friend who's good with money.""",
    sandbox=sandbox(),
)
def finance_tracker(event=None):
    """Chat-based expense logging and budget tracking."""


@app.hook(
    id="weekly-spending-summary",
    event="scheduler.finance",
    schedule=cron("0 18 * * 0"),
)
def weekly_spending_summary():
    """Send weekly spending summary every Sunday 6 PM UTC."""


@app.local_entrypoint()
def local(input_payload):
    return {"ok": True, "app": "ara-personal-finance", "input": input_payload}


if __name__ == "__main__":
    run_cli(app)
