from flask import Response,abort,request,jsonify
import json
from run import app


class Httpstatus(object):

    @staticmethod
    def bad_request(message):
        response = jsonify({'message': message})
        response.status_code = 400
        return response

    @staticmethod
    def not_found(message):
        response = jsonify({'message': message})
        response.status_code = 404
        return response

    @staticmethod
    def int_server(message):
        response = jsonify({'message': message})
        response.status_code = 500
        return response

    @staticmethod
    def ok_server_post(message='ok'):
        response = jsonify({'message': message})
        response.status_code = 201
        return response

    @staticmethod
    def ok_server_put(message='ok'):
        response = jsonify({'message': message})
        response.status_code = 200
        return response

    @staticmethod
    def unauthorized(message = 'unauthorized'):
        response = jsonify({'message': message})
        response.status_code = 401
        return response

    @staticmethod
    def conflict(message = 'conflict'):
        response = jsonify({'message': message})
        response.status_code = 409
        return response