[![][image]][demo]

## Pyblish Event

An intranet frontend for real-time updates of Pyblish events.

### Live Demo

- http://event.pyblish.com/

### API

Event supports posting new events as JSON formatted documents via standard POST requests.

```python
import json
import requests

url = "http://event.pyblish.com/api"  # Note the `/api` suffix
headers = {"content-type": "application/json"}  # We're sending JSON data
payload = {
    "instance": "MyFirstInstance01",
    "comment": "My first event!",
    "author": "marcus",
    "family": "marcus.family"
}

# Before you send, pop up Events and notice the event appear in real-time!

# Now send!
requests.post(url,
              data=json.dumps(payload),  # Data must be sent as string
              headers=headers)

```

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
[image]: https://cloud.githubusercontent.com/assets/2152766/4826577/bc8aef62-5f71-11e4-97c9-0ff197212edc.png