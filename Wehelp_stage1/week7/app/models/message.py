from pydantic import BaseModel
from . import cursor,mydb,UserData

class MessageData(BaseModel):
    id:int=None
    name: str=None
    member_id: int
    content: str
    
    @classmethod
    def query_messages(self):
        m=[]
        sql=("select * from message")
        cursor.execute(sql)
        results = cursor.fetchall()
        for i in range(len(results)):
            queryname=UserData.query_usernamebyid(results[i][1])
            m.append(MessageData(id=results[i][0],name=queryname,member_id=results[i][1],content=results[i][2]))
        return m
        
    @classmethod
    def create_message(self,member_id:int,message:str):
        sql=("Insert into message (member_id,content) values (%s,%s)")
        val=(member_id,message)
        cursor.execute(sql, val)
        mydb.commit()

    @classmethod
    def delete_message(self,message_id:int):
        sql=("Delete from message where id = %s")
        val=(message_id,)
        cursor.execute(sql, val)
        mydb.commit()
    @classmethod
    def query_message(self,message_id:int):
        sql=("select * from message where id= %s")
        val=(message_id,)
        cursor.execute(sql,val)
        result = cursor.fetchall()
        queryname=UserData.query_usernamebyid(result[0][1])
        return MessageData(id=result[0][0],name=queryname,member_id=result[0][1],content=result[0][2])