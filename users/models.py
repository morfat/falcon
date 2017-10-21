from utils.models import Model 



class User(Model):
    db_table='users'
    fields=['id','first_name','last_name','app','email','token'] #display fields

    




