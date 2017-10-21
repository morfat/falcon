class User:
    fields=['id','email','password','is_active','']

    def __init__(self,db):
        self.exclude=['id','email','password','is_active','']