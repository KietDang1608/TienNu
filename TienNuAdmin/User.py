class User:
    def __init__(self,username:str,password:str, name:str,datecreate:str ):
        self.username = username
        self.password = password
        self.name = name
        self.datecreate = datecreate
    def __str__(self) :
        return f"{self.username},{self.password},{self.name},{self.datecreate}"