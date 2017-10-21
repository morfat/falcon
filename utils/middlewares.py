from .database import Db

class APIMiddleWare:

    
    def __init__(self,):
        self._db=None
        self._app=None
        self._user=None


    def process_request(self,req,resp):
        self._db=Db() #create db connection and Db object

                                
        """
        app_key=req.get_header('app-key',required=True)
        app_secret=req.get_header('app-secret',required=True)
        #authenticate
        self._app=self.authenticate(app_key,app_secret)
        if not self._app:
            raise falcon.HTTPUnauthorized(title='Incorrect  credentials ',description='Valid API app_key and app_secret are needed')
        elif not self._app.get('is_active'):
            raise falcon.HTTPForbidden(title='Access Denied',description='You API account is disabled')
        """


    def process_resource(self,req,resp,resource,params):
        resource.db=self._db
        resource.app=self._app
        resource.user=self._user



    def process_response(self,req,resource,req_succeeded):
        self._db.connection().close()




