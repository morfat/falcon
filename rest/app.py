#This contains the deployable content for the whole project
import falcon

#from classes import Sms
#from resources import SendTransactionalSmsResource,SendBatchSmsResource,CheckSmsDeliveryStatusResource

#from middlewares import ujumbeMiddleWare
#from handlers import api_error_handler

from users.urls import users_patterns


URL_PATTERNS=[users_patterns,]


def get_app():
    app=falcon.API(#middleware=[ujumbeMiddleWare,],)

    #add roots
    for up in URL_PATTERNS:
        for i in up:
             app.add_route(i[0],i[1])

    #add cutom error handler
    #api.add_error_handler(falcon.HTTPError,handler=api_error_handler)
    
    return app




