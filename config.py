import os

# Get DB URL from environment variables or fallback to default
SQLALCHEMY_DATABASE_URI = os.environ.get(
    "DATABASE_URL",
    "postgresql://foodzy_db_user:new_password@dpg-cve4hfjtq21c7399v4mg-a.oregon-postgres.render.com/foodzy_db"
)

# Disable modification tracking for performance
SQLALCHEMY_TRACK_MODIFICATIONS = False

