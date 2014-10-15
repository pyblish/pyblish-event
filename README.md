![](images/event.gif)

## Pyblish Event

An intranet frontend for real-time updates of Pyblish events.

### How to Get Started

1. Clone this repo

 ```bash
$ git clone https://github.com/pyblish/pyblish-event.git
```

2. Install dependencies (best done within a virtual environment)

 ```bash
$ cd pyblish-event
$ pip install -r requirements.txt
```

3. Run the app

 ```bash
$ python runserver.py
```

4. Browse to app

 > [http://localhost:5000](http://localhost:5000)

### API

Communicate with Pyblish Event via the RESTful API.

##### GET

Get all events

```bash
$ curl http://localhost:5000/api -X GET
[
    "Peter01", 
    "Peter-model", 
    "MechanizedVillain06"
]

```

##### PUT

Add an event

```bash
$ curl http://localhost:5000/api -d "name=EventName01" -X PUT
```

Clients will update in real-time and events persist across sessions.