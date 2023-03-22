from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    phone_number = db.Column(db.String)

    @validates('name')
    def validate_name(self, key, new_name):
        names = Author.query.filter(Author.name).all()
        if not new_name:
            raise ValueError('Please enter a name')
        elif new_name in names:
            raise ValueError(f'Please enter a new name. {new_name} is already taken.')
        return new_name
    
    @validates('phone_number')
    def validate_phone_number(self, key, number):
        if len(number) != 10:
            raise ValueError('Please enter a valid phone number...bruh')
    

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable = False)
    content = db.Column(db.String)
    summary = db.Column(db.String(250))
    category = db.Column(db.String)


    @validates('title')
    def validate_title(self, key, new_title):
        bait = ["Won't Believe", "Secret", "Top", "Guess"]

        if not new_title:
            raise ValueError("Title is required")
        
        elif new_title not in bait:
            raise ValueError(f'Title must contain one of the following:{bait}')
        return new_title
    
    @validates('content')
    def validate_content(self, key, new_content):
        if len(new_content) < 250:
            raise ValueError('Post needs to be at LEAST 250 characters')
        return new_content

    @validates('summary')
    def validate_summary(self, key, new_summ):
        if len(new_summ) > 250:
            raise ValueError(f"{new_summ} is too long. Needs to be less than 250 characters.")
        return new_summ
    
    @validates('category')
    def validate_category(self, key, new_cat):
        if new_cat != 'Fiction' or new_cat != 'Non-Fiction':
            raise ValueError("Category needs to be either Fiction or Non-Fiction. Check your spelling and capitalization.")
        return new_cat
