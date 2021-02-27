from flask import Flask
from main.routes import routes
from users.routes import users

app = Flask(__name__)
app.register_blueprint(routes)
app.register_blueprint(users)

if __name__ == '__main__':
    app.run(debug=True)
