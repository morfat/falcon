#This contains the deployable content for the whole project
import falcon
import time

#from classes import Sms
#from resources import SendTransactionalSmsResource,SendBatchSmsResource,CheckSmsDeliveryStatusResource

#from middlewares import ujumbeMiddleWare
#from handlers import api_error_handler

from users.urls import patterns as users_patterns


URL_PATTERNS=[users_patterns,]



def get_app():
    #app=falcon.API(middleware=[ujumbeMiddleWare,],)
    app=falcon.API()



    #add roots
    for up in URL_PATTERNS:
        for i in up:
             app.add_route(i[0],i[1])
             #print("Link URL ",i[0],)
    
    #add cutom error handler
    #api.add_error_handler(falcon.HTTPError,handler=api_error_handler)
    
    return app




