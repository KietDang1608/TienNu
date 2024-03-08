class Category:
    def __init__(self,id: int, title: str):
        self.id = id
        self.title = title
    def __str__(self):
        return f"{ {self.id}, {self.title} }"
        
        