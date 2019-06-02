from flask import app, request, Flask
from flask_restful import Resource, Api

from service.MainService import MainService

app = Flask(__name__)
api = Api(app)


class CompareController(Resource):

    def __init__(self, service):
        self.main_service = service

    def post(self):
        if request.headers['Content-Type'] == 'application/json;charset=UTF-8':
            print("Request received")
            request_content = request.get_json()
            print('img_list1: ' + ", ".join(request_content['img_list1']))
            print('img_list2: ' + ", ".join(request_content['img_list2']))
            print('description1: ' + request_content['description1'])
            print('description2: ' + request_content['description2'])
            result = main_service.is_same_announcement(request_content['img_list1'], request_content['img_list2'],
                                                     request_content['description1'], request_content['description2'])
            print('result: ' + str(result))
            print("=============================================================================")
            return result
        else:
            return "Unsupported Media Type!"


main_service = MainService()
api.add_resource(CompareController, '/compare', resource_class_kwargs={'service': main_service})
