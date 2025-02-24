from pydantic import BaseModel
from passlib.hash import pbkdf2_sha256
from . import cursor,mydb,conn

class UserData(BaseModel):
    id:int=None
    name:str=None
    username: str
    password: str
    def set_pw(self,password):
        return pbkdf2_sha256.hash(password)
    def check_pw(self,password):
        return pbkdf2_sha256.verify(password, self.password)
    
    @classmethod
    def query_username(self,username:str):
        sql=("select * from member where username=%s")
        val=(username,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if result == []:
          return None
        else:
          return UserData(id=result[0][0],name=result[0][1],username=result[0][2],password=result[0][3])
        
    @classmethod
    def query_usernamebyid(self,id:int):
        sql=("select * from member where id=%s")
        val=(id,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return result[0][1]
    
    @classmethod
    def create_user(self,userdata:'UserData'):
        sql=("Insert into member (name,username,password) values (%s,%s,%s)")
        password_hash=self.set_pw(self,userdata.password)
        val=(userdata.name,userdata.username,password_hash,)
        cursor.execute(sql, val)
        mydb.commit()    
    @classmethod
    def update_user(self,updatename:str,username:str):
        sql=("UPDATE member SET name=%s WHERE id=%s")
        val=(updatename,username,)
        cursor.execute(sql, val)
        mydb.commit()
        return {"ok":True}

