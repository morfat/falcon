import falcon

from .models import App

class List(object):
    def on_get(self,req,resp):
        resp.status=falcon.HTTP_200 #this is default
        #apps=App(self.db).all()

        app=App(self.db).one(pk=1)
        resp.media=app

    
        