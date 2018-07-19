from app import app

# Import APIs (Flask blueprints)
from haproxyapi.api.default import default
from haproxyapi.api.errors import errors as api_errors

# Register APIs Blueprints :
app.register_blueprint(default, url_prefix='/api')
app.register_blueprint(api_errors)

if __name__ == '__main__':
    app.run()
