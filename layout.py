"""Layout factory for the Databricks Dash hello-world app."""

from dash import html

from source import get_environment_hint, get_utc_timestamp, get_welcome_message


def build_layout() -> html.Div:
    """Build and return the app layout."""
    return html.Div(
        style={"fontFamily": "Arial, sans-serif", "padding": "2rem"},
        children=[
            html.H1("Databricks Dash App"),
            html.P(get_welcome_message()),
            html.P(get_environment_hint()),
            html.Hr(),
            html.P(f"Rendered at: {get_utc_timestamp()}"),
        ],
    )
