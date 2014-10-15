### Angular Flask

Using Angular with Flask.

```bash
# Usage
$ python chat.py
```

Then browse to [http://127.0.0.1:5000](http://127.0.0.1:5000)

This demo illustrates one method of using Angular with Flask. It involves adding an additional filter to AngulerJS to circumvent the fact that both Jinja2 and AngularJS uses the same notation for expressions; ({{ }}).

It also illustrates how to build a factory for the socket io connection, so as to use the socket within AngularJS controllers.