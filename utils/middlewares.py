import MySQLdb
import falcon 

from settings import DATABASE


class UjumbeGatewayMiddleWare:

    def authenticate(self,app_key,app_secret):
        #authenticate app
        c=self._db.cursor()
        c.execute("SELECT id,name,is_active FROM apps_app WHERE app_key=%s AND app_secret=%s ",
                             (app_key,app_secret,))
        result=c.fetchone()
        app={'id':result[0],'name':result[1],'is_active':result[2]} if result else result
        c.close()
        return app




    
    
    def __init__(self,):
        self._db=None
        #self._cursor=None
        self._app=None




    def process_request(self,req,resp):
        self._db=MySQLdb.connect(user=DATABASE.get('USER'),passwd=DATABASE.get('PASSWORD'),
                                db=DATABASE.get('NAME'),host=DATABASE.get('HOST'),port=DATABASE.get('PORT'),
                                )
                                

        app_key=req.get_header('app-key',required=True)
        app_secret=req.get_header('app-secret',required=True)
        #authenticate
        self._app=self.authenticate(app_key,app_secret)
        if not self._app:
            raise falcon.HTTPUnauthorized(title='Incorrect  credentials ',description='Valid API app_key and app_secret are needed')
        elif not self._app.get('is_active'):
            raise falcon.HTTPForbidden(title='Access Denied',description='You API account is disabled')



    def process_resource(self,req,resp,resource,params):
        resource.db=self._db
        #resource.cursor=self._cursor
        resource.app=self._app



    def process_response(self,req,resource,req_succeeded):
        #close cursor
        #self._cursor.close()
        self._db.close()

        #print (req_succeeded)
        #print ("Process response")



ujumbeMiddleWare=UjumbeGatewayMiddleWare()


