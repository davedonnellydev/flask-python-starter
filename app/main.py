from app import create_app
import os

# Get configuration from environment
config_name = os.environ.get('FLASK_ENV', 'development')
app = create_app(config_name)

@app.route("/")
def hello_world():
    return "Hello from Flask Python Starter!"

if __name__ == "__main__":
    app.run(debug=True)
