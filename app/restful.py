import flask.ext.restful


def api(socket, data):
    class Api(flask.ext.restful.Resource):
        def get(self):
            return data

        def post(self):
            pass

    return Api
