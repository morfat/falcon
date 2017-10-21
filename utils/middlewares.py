from .database import Db

from .authentication import Authentication

class APIMiddleWare:

    def __init__(self,):
        self._db=None
        self._app=None
        self._user=None


    def process_request(self,req,resp):
        self._db=Db() #create db connection and Db object
        authentication=Authentication(self._db)
        token=req.get_header('Authorization',required=False)
        app_key=req.get_header('app-key',required=False)
        app_secret=req.get_header('app-secret',required=False)

        #authenticate as per given credentials
        if token:
            self._user=authentication.authenticate_user(token=token)
        elif app_key and app_secret:
            self._app=authentication.authenticate_app(app_key=app_key,app_secret=app_secret)



    def process_resource(self,req,resp,resource,params):
        resource.db=self._db
        resource.app=self._app
        resource.user=self._user



    def process_response(self,req,resource,req_succeeded):
        self._db.connection().close()



class UserMiddleWare(APIMiddleWare):
    def process_request(self,req,resp):
        self._db=Db() #create db connection and Db object
        authentication=Authentication(self._db)
        token=req.get_header('Authorization',required=True)
        #authenticate as per given credentials
        self._user=authentication.authenticate_user(token=token)


class AppMiddleWare(APIMiddleWare):
    def process_request(self,req,resp):
        self._db=Db() #create db connection and Db object
        authentication=Authentication(self._db)
        app_key=req.get_header('app-key',required=True)
        app_secret=req.get_header('app-secret',required=True)

        #authenticate as per given credentials
        self._app=authentication.authenticate_app(app_key=app_key,app_secret=app_secret)

