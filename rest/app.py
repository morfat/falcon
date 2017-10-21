#This contains the deployable content for the whole project
import falcon
#import time

from utils.middlewares import APIMiddleWare,UserMiddleWare,AppMiddleWare
from utils.handlers import api_error_handler

from users.urls import patterns as users_patterns
from apps.urls import patterns as apps_patterns


URL_PATTERNS=[users_patterns,apps_patterns]



def get_app():
    app=falcon.API(middleware=[UserMiddleWare(),],)
   
    #add roots
    for up in URL_PATTERNS:
        for i in up:
             app.add_route(i[0],i[1])
             #print("Link URL ",i[0],)
    
    #add cutom error handler
    app.add_error_handler(falcon.HTTPError,handler=api_error_handler)
    
    return app




