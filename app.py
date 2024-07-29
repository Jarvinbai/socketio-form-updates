from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('form.html')

@socketio.on('input_event')
def handle_input_event(data):
    emit('update_input', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
