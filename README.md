![](https://github.com/pyblish/pyblish-event/wiki/images/event2.gif)

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
$ python run.py
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
    {
        "content": "Wed Oct 22 17:28:09 2014", 
        "title": "Mackan06"
    }, 
    {
        "content": "Wed Oct 22 17:28:32 2014", 
        "title": "Panzar12 was published, without errors"
    }
]


```

##### POST

Add an event, get ID in return.

```bash
$ curl http://localhost:5000/api -d "event=EventName01" -X POST
```

Clients will update in real-time and events persist across sessions.