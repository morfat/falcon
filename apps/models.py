from utils.models import Model 



class App(Model):
    db_table='apps'
    fields=['id','name','is_active'] #only display id and name on select query
    




