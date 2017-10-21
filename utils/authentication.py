import falcon
from users.models import User

class Authentication:
    def __init__(self,db):
        self._db=db


    def authenticate_app(self,app_key,app_secret):
        #authenticate app
     
        #authenticate
        """self._app=self.authenticate(app_key,app_secret)
        if not self._app:
            raise falcon.HTTPUnauthorized(title='Incorrect  credentials ',description='Valid API app_key and app_secret are needed')
        elif not self._app.get('is_active'):
            raise falcon.HTTPForbidden(title='Access Denied',description='You API account is disabled')
        """
        return None



    def authenticate_user(self,token):
        user=User(self._db)
        user.pk='token'
        user=user.one(pk=token)

        if not user:
            raise falcon.HTTPUnauthorized(title='Incorrect / Invalid Token ',description='Valid API token is  needed')
        return user


