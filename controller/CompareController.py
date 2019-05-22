from flask import app, request, Flask
from flask_restful import Resource, Api

from service.MainService import MainService

app = Flask(__name__)
api = Api(app)


class CompareController(Resource):

    def __init__(self, service):
        self.main_service = service

    def post(self):
        if request.headers['Content-Type'] == 'application/json':
            print("Request received")
            request_content = request.get_json()
            return main_service.is_same_announcement(request_content['img_list1'], request_content['img_list2'],
                                                     request_content['description1'], request_content['description2'])
        else:
            return "Unsupported Media Type!"


main_service = MainService()
api.add_resource(CompareController, '/compare', resource_class_kwargs={'service': main_service})
