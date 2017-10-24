from .database import Db

from .authentication import Authentication
import falcon

class BaseMiddleWare:

    def __init__(self,):
        self._db=None
        self._app=None
        self._user=None


    def process_request(self,req,resp):
        self._db=Db() #create db connection and Db object
        self._app,self._user=self.authenticate(req)
        
        if not (self._app or self._user):
            raise falcon.HTTPUnauthorized(title='Authentication not implemented',description='Authenticate user or app credentials. As per the middleware used')

       


    def process_resource(self,req,resp,resource,params):
        resource.db=self._db
        resource.app=self._app
        resource.user=self._user



    def process_response(self,req,resource,req_succeeded):
        self._db.connection().close()


    def authenticate(self,request):
        """To be implemented by inheriting classes. To return app and user"""
        pass

    

    def get_db(self):
        return self._db

  

class UserMiddleWare(BaseMiddleWare):
    def authenticate(self):
        authentication=Authentication(self._db)
        token=req.get_header('Authorization',required=True)
        token=token[5:].strip() #to strip off the Token value in token
        

        #authenticate as per given credentials
        self._user=authentication.authenticate_user(token=token)


class AppMiddleWare(BaseMiddleWare):
    def authenticate(self,request):
        authentication=Authentication(self.get_db())
        app_key=request.get_header('app-key',required=True)
        app_secret=request.get_header('app-secret',required=True)
        #authenticate as per given credentials
        app=authentication.authenticate_app(app_key=app_key,app_secret=app_secret)
        return (app,None,)


