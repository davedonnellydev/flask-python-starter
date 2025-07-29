from app import create_app
app = create_app()

@app.route("/")
def hello_world():
    return "Hello from Flask Python Starter!"

if __name__ == "__main__":
    app.run(debug=True)
