from dash import Dash, html

from layout import layout  # if you have a separate layout.py


# create app


app = Dash(__name__)
app.layout = layout if 'layout' in globals() else html.Div("Hello World")

# Entry point for Databricks App
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8080)