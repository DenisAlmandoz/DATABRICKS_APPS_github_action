"""Main entry point for the Databricks Dash app."""

from dash import Dash

from layout import build_layout

app = Dash(__name__)
app.layout = build_layout()
server = app.server

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
