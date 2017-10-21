import falcon

class List(object):
    def on_get(self,req,resp):
        resp.status=falcon.HTTP_200 #this is default
        resp.body=('\nList all users')
    
        