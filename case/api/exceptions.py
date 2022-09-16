from rest_framework.exceptions import APIException


class RequestExceptions(APIException):
    status_code = 400
    default_detail = "Request Error"
    default_code = "invalid_json"