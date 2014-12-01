## Pyblish Event

An intranet frontend for real-time updates of Pyblish events.

### Live Demo

- http://event.pyblish.com/

### API

Event supports posting new events as JSON formatted documents via standard POST requests.

> Note that the following example uses the [Requests library][requests], which may be installed via PyPI.

```python
import json
import requests

url = "http://event.pyblish.com/event"  # Note the `/event` suffix
headers = {"content-type": "application/json"}  # We're sending JSON data
payload = {
    "instance": "MyFirstInstance01",
    "comment": "My first event!",
    "author": "marcus",
    "family": "marcus.family"
}

# Before you send, pop up Pyblish Event and notice the event appear in real-time!

# Now send!
requests.post(url,
              data=json.dumps(payload),  # Data must be sent as string
              headers=headers)

```

If you install locally, the URL above will instead point to your local server.

[requests]: http://docs.python-requests.org/en/latest/

### Local Installation

If you want Event locally, this is what you do.

1. Clone this repository

 ```bash
$ git clone https://github.com/pyblish/pyblish-event.git
$ cd pyblish-event
```

2. Install requirements

 ```bash
$ pip install -r requirements.txt
```

 Also install [MongoDB][mongo]
 
 - [Having trouble?](#faq)

 [mongo]: http://docs.mongodb.org/manual/installation

3. Run

 ```bash
$ python app/app.py
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
```

4. Go to http://127.0.0.1:5000

At first, there won't be any events, as your new Mongo collection is empty. But you can add some via the API, see above.

[demo]: http://event.pyblish.com/

### FAQ

> VCVARSALL.bat / I can't install the requirements.

This is due to a limitation in one of the requirements; Gevent. Gevent requires that you compile the library and compilation on Windows typically requires an installaton of Visual Studio. To circumvent this, you have two options.

1. Install a pre-compiled binary from here.

 - http://www.lfd.uci.edu/~gohlke/pythonlibs/#gevent

2. Install a compiler for Python to use when being tasked with compiling Gevent.

 - http://www.microsoft.com/en-us/download/confirmation.aspx?id=44266
 - Next, make sure you update setuptools to 6.0, as the compiler will not be picked up otherwise.

Then re-run the installation of requirements, which will pick up from where it left off.

> MongoDB must be installed

You may have installed it, but not started it. In a nutshell, MongoDB needs to be running as a dedicated process on the computer hosting the database. On Ubuntu, this process may happen automatically upon installation, but on Windows you may have to perform an extra step. Make sure you follow through these steps.

- http://docs.mongodb.org/manual/tutorial/install-mongodb-on-windows/
