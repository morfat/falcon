
class Model(object):
    db_table=''
    fields=['*']
    pk='id'

    def __init__(self,db):
        self.__db=db

    def db(self):
        return self.__db

    def get_fields(self):
        return ','.join(self.fields)

    def all(self):
        sql="SELECT %s FROM %s "%(self.get_fields(),self.db_table)
        return self.db().fetchall(sql=sql)

    def one(self,pk):
        pk=self.normalize_variable(pk)
        sql="SELECT %s FROM %s WHERE %s=%s"%(self.get_fields(),self.db_table,self.pk,pk)
        return self.db().fetchone(sql=sql)

    def filter(self,**kwargs): #for simple AND filtering in where clause
        filter_string=''

        for k,v in kwargs.items():
            v=self.normalize_variable(v)
            filter_string+=' '+k+' = %s AND'%(v)
        
        
        if filter_string.endswith('AND'):
            filter_string=filter_string[:-3]

        sql="SELECT %s FROM %s WHERE %s "%(self.get_fields(),self.db_table,filter_string)
        return self.db().fetchall(sql=sql)


    def normalize_variable(self,v):
        if not isinstance(v,int):
            v="'%s'"%(str(v))
        return v


    def raw(self,sql):
        return self.db().fetchall(sql=sql)











