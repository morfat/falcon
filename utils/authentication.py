import falcon

class Authentication:
    def __init__(self,db):
        self._db=db


    def authenticate_app(self,app_key,app_secret):
        #authenticate app
        c=self._db.cursor()
        c.execute("SELECT id,name,is_active FROM apps_app WHERE app_key=%s AND app_secret=%s ",
                             (app_key,app_secret,))
        result=c.fetchone()
        app={'id':result[0],'name':result[1],'is_active':result[2]} if result else result
        c.close()
        

        app_key=req.get_header('app-key',required=True)
        app_secret=req.get_header('app-secret',required=True)
        #authenticate
        self._app=self.authenticate(app_key,app_secret)
        if not self._app:
            raise falcon.HTTPUnauthorized(title='Incorrect  credentials ',description='Valid API app_key and app_secret are needed')
        elif not self._app.get('is_active'):
            raise falcon.HTTPForbidden(title='Access Denied',description='You API account is disabled')
        return app


    def authenticate_user(self,token):
        token=req.get_header('token',required=True)
       
        self.authenticate(app_key,app_secret)
        if not self._app:
            raise falcon.HTTPUnauthorized(title='Incorrect  credentials ',description='Valid API app_key and app_secret are needed')
        elif not self._app.get('is_active'):
            raise falcon.HTTPForbidden(title='Access Denied',description='You API account is disabled')
        return user


