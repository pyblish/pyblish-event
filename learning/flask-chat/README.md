### Flask Chat

A Flask implementation of the socket.io example.
http://socket.io/get-started/chat/

```bash
# Usage
$ python chat.py
```

Then browse to [http://127.0.0.1:5000](http://127.0.0.1:5000)

The example illustrates a Flask application receiving events from a client via socket.io and re-sending them back to the client via broadcasting. To broadcast means that all clients connected to the app will receive the message, even the client initiating the message.

Additionally, every 10 seconds, the server will send a message to the client(s).
