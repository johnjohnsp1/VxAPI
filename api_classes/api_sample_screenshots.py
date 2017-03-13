from api_classes.api_caller import ApiCaller


class ApiSampleScreenshots(ApiCaller):
    endpoint_url = '/api/sample-screenshots/:sha256'
    request_method_name = ApiCaller.CONST_REQUEST_METHOD_GET
    endpoint_auth_level = ApiCaller.CONST_API_AUTH_LEVEL_DEFAULT
