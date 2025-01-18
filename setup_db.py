import sys
import os

# Add the 'app' directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app import create_app, db
from app.models import User

def setup_database():
    # Create all tables
    db.create_all()
    print("Database tables created successfully!")

if __name__ == "__main__":
    # Initialize the app
    app = create_app()

    # Ensure we're working within the app context
    with app.app_context():
        setup_database()

