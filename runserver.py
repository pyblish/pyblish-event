from pyblish_event import app


def runserver():
    app.socket.run(app.app)

if __name__ == '__main__':
    runserver()
