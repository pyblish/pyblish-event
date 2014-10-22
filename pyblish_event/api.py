import json
import flask
import pymongo
import flask.ext.restful


client = pymongo.MongoClient()
db = client.test_database
contacts = db.contacts
excludes = {"_id": False}


class ApiContact(flask.ext.restful.Resource):
    def get(self):
        return list(contacts.find(fields=excludes))

    def post(self):
        contact = flask.request.stream.read()
        contact_json = json.loads(contact)

        # Append unique ID to document
        # todo: Replace this with the actual MongoDB Id
        ids = [i['id'] for i in contacts.find()]
        contact_json['id'] = max(ids) + 1
        contacts.insert(contact_json)


class ApiContactId(flask.ext.restful.Resource):
    def get(self, id):
        return contacts.find_one({"id": int(id)},
                                 fields=excludes)

    def put(self, id):
        contact = flask.request.stream.read()
        contact_json = json.loads(contact)
        contacts.update({"id": int(id)},
                        document=contact_json)

    def delete(self, id):
        contacts.remove({"id": int(id)})
