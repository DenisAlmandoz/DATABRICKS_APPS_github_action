"""Small data/source helpers for the Databricks Dash hello-world app."""

from datetime import datetime, timezone


def get_welcome_message() -> str:
    """Return a basic message rendered in the UI."""
    return "Hello from your Databricks App 🚀"


def get_environment_hint() -> str:
    """Return a deployment hint shown in the UI."""
    return (
        "Use GitHub Actions + Databricks Asset Bundles to deploy this app "
        "across dev/stg/prd."
    )


def get_utc_timestamp() -> str:
    """Return the current UTC timestamp in ISO-8601 format."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")
