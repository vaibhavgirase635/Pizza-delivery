from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id : Optional[int]
    username : str
    email :str
    password : str
    is_staff : Optional[bool]
    is_active : Optional[bool]
    
    class Config:
        orm_mode = True
        schema_extra = {
            'example':{
                "username":"johndoe",
                "email":"johndoe@gmail.com",
                "password":"password",
                "is_staff":False,
                "is_active":True
            }
        }

class Settings(BaseModel):
    authjwt_secret_key:str='da6be563f103bd83fa69c6e81b055033c486d835f1ad284d273c080c855b4a91'

class LoginModel(BaseModel):
    username:str
    password:str


class OrderModel(BaseModel):
    id:Optional[int]
    quantity :int
    order_status : Optional[str] = "PENDING"
    pizza_size : Optional[str] = "SMALL"
    user_id : Optional[int]

    class config:
        orm_mode = True
        schema_extra = {
            "example":{
                "quantity":2,
                "pizza_size":"LARGE"
            }
            
        }