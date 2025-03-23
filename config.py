import os

# Get DB URL from environment variables or fallback to default
SQLALCHEMY_DATABASE_URI = os.environ.get(
    "DATABASE_URL",
    "postgresql://foodzy_db_user:cWJ59OtZIhi6425x0yz3xCrqGplfJU06@dpg-cve4hfjtq21c7399v4mg-a.oregon-postgres.render.com/foodzy_db"
)

# Disable modification tracking for performance
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Secret key for session management or JWT (optional)
SECRET_KEY = os.environ.get("SECRET_KEY", "super_secret_key")
