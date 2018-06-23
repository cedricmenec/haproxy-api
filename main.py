from app import app

# Import APIs (Flask blueprints)
from haproxyapi.api import api

# Register APIs Blueprints :
app.register_blueprint(api, url_prefix='/api')


if __name__ == '__main__':
    app.run()
