from flask import Flask
from app.routes.routes import main_bp

app = Flask(
    __name__,
    template_folder="templates",  # HTML templates path
    static_folder="static"        # CSS, JS, and images path
)
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run(debug=True)
