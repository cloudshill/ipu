from app import create_app
import os

env = os.getenv('ENV')
app, socketio = create_app(env)

if __name__ == '__main__':
    socketio.run(app, debug=True)
