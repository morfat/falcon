
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
        if not isinstance(pk,int):
            pk="'%s'"%(str(pk))

        sql="SELECT %s FROM %s WHERE %s=%s"%(self.get_fields(),self.db_table,self.pk,pk)
        return self.db().fetchone(sql=sql)

    def raw(self,sql):
        return self.db().fetchall(sql=sql)











