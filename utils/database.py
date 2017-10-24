import MySQLdb
from collections import namedtuple

from rest.settings import DATABASE


class Db:
    def __init__(self,):
        self._connection=MySQLdb.connect(user=DATABASE.get('USER'),passwd=DATABASE.get('PASSWORD'),
                                db=DATABASE.get('NAME'),host=DATABASE.get('HOST'),port=DATABASE.get('PORT')
                            )
        self._executed_query=None



    def connection(self,):
        return self._connection


    def cursor(self): #return new  mysql cursor on each call
        return self.connection().cursor()

    def get_executed_query(self,):
        return self._executed_query

    def tuple_results(self,cursor,fields):
        return map(namedtuple('Result',[f[0] for f in cursor.description]) if not fields else namedtuple('Result',fields)._make,cursor.fetchall())
    
    def dict_results(self,cursor,fields):
        columns = [col[0] for col in cursor.description] if not fields else fields
        return [dict(zip(columns, row)) for row in cursor.fetchall()]



    def fetchall(self,cursor=None,fields=None,sql=None,as_dict=True):
        """Default is to return results as dictionary list"""

        if not cursor:
            cursor=self.cursor()
            if sql:
                cursor.execute(sql)

            results=self.tuple_results(cursor,fields) if not as_dict else self.dict_results(cursor,fields)
            cursor.close()
            return results
        else:
            if sql:
                cursor.execute(sql)
            return self.tuple_results(cursor,fields) if not as_dict else self.dict_results(cursor,fields)




    

    def fetchone(self,cursor=None,sql=None):
        "Return one row from a cursor as a dict"
        result={}
        if not cursor:
            cursor=self.cursor()
            if sql:
                cursor.execute(sql)
            r=cursor.fetchone()
            if cursor.rowcount:
                

                result=dict(zip([col[0] for col in cursor.description], r))
            cursor.close()
        else:
            if sql:
                r=cursor.execute(sql)
            r=cursor.fetchone()
            if cursor.rowcount:
                result=dict(zip([col[0] for col in cursor.description], r))
        return result






  
    def save(self,sql,commit=True):
        #saves and commits updates or inserts. must return True if done so.
        cursor=self.cursor()
        cursor.execute(sql)
        self._executed_query=cursor._last_executed

        if commit:
            self.connection().commit()
        cursor.close()
        return True



    def save_many(self,sql,data_list): #creates many separated queries.
        """ example :  #saved=mysql.save_many(sql="UPDATE sms_outgoing SET status=%s WHERE id=%s",data_list=[(STATUS_IN_QUEUE,m.id) for m in messages]) """
        #must return True to be accpted.
        cursor=self.cursor()
        cursor.executemany(sql,data_list)
        self.connection().commit()
        cursor.close()
        return True


    def fetch_results(self,sql):
        cursor=self.cursor()
        cursor.execute(sql)
        results=self.fetchall(cursor)
        cursor.close()
        return results
