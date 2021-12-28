from db.config import db

class Category(db.Model):
    
    def __init__(self, name):
        self.name = name
        
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True)
    
    def __str__(self):
        return f"Category: Name {self.name}"