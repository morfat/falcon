from .database import Db

from .authentication import Authentication
import falcon

class BaseMiddleWare:

    def __init__(self,):
        self._db=None
        self._app=None
     

    def process_request(self,req,resp):
        self._db=Db() #create db connection and Db object
        self._app=self.authenticate(req)
        
        if not self._app:
            raise falcon.HTTPUnauthorized(title='Authentication not implemented',description='Authenticate app credentials. As per the middleware used')

       


    def process_resource(self,req,resp,resource,params):
        resource.db=self._db
        resource.app=self._app
       


    def process_response(self,req,resource,req_succeeded):
        self._db.connection().close()


    def authenticate(self,request):
        """To be implemented by inheriting classes. To return app and user"""
        pass

    

    def get_db(self):
        return self._db

  
class NoAuthMiddleWare(BaseMiddleWare):
    """ Use this if you inted not to use any authentications """
    def process_request(self,req,resp):
        self._db=Db() #create db connection and Db object
    

class AppMiddleWare(BaseMiddleWare):
    def authenticate(self,request):
        authentication=Authentication(self.get_db())
        app_key=request.get_header('app-key',required=True)
        app_secret=request.get_header('app-secret',required=True)
        #authenticate as per given credentials
        return authentication.authenticate_app(app_key=app_key,app_secret=app_secret)


