from app import create_app  # Import app factory

# Create the Flask app using the factory function
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)  # Run with debug mode for dev
