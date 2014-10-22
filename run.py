import os
from pyblish_event import app, socket

os.environ['DEVELOP'] = "true"
socket.run(app)
