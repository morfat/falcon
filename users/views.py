import falcon

from .models import User

class List(object):
    def on_get(self,req,resp):
        resp.status=falcon.HTTP_200 #this is default
        resp.media=User(self.db).all()
        
    
        