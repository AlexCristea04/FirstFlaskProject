from flask import Flask
from config import Config
from controllers.mainController import main_bp
from models.models import db

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Register Blueprints
app.register_blueprint(main_bp)

# Create database tables
@app.before_request
def create_tables():
    db.create_all()
    if __name__ == '__main__':
        app.run(debug=True)