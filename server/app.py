from flask import Flask

app = Flask(__name__)

# Provided list of existing models
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

@app.get("/")
def index():
    """Default route: introduce the company."""
    return "Welcome to Flatiron Cars"

@app.get("/<model>")
def model_lookup(model):
    """Lookup a specific model by name."""
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"

if __name__ == "__main__":
    # Run the dev server (not used by tests, but handy for local dev)
    app.run(debug=True, port=5555)
