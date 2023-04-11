from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable= False)
    phone_number = db.Column(db.String)
                            #  db.CheckConstraint('len(phone_number) == 10'),
                            #  nullable=False)

    @validates( 'name' )
    def validate_author(self, key, author):
        if author in [ a.name for a in Author.query.all() ]:
            raise ValueError("Sorry, name already used")
        return author
    
    @validates('phone_number')
    def validates_number(self, key, number):
        if len(number) != 10:
            raise ValueError("Length is way off!")
        return number
            
            
    # __table_args__= (
        # db.CheckConstraint( 'len(phone_number) == 10' ),
    # )



class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable= False)
    content = db.Column(db.String)
                        # db.CheckConstraint('content >= len(250)'),
                        # nullable=False)
    summary = db.Column(db.String)
    category = db.Column(db.String)

    @validates('content')
    def validates_content(self, key, content):
        if len(content) < 250:
            raise ValueError("Not long enough")
        return content
    
    @validates('summary')
    def validates_summary(self, key, summary):
        if len(summary) >= 250:
            raise ValueError("Too long!")
        return summary
    
    
    #Come back to this!!!!!!!
    @validates('category')
    def validates_category(self, key, category):
        if category != 'Fiction' and category != 'Non-Fiction':
            raise ValueError("Must be either Fiction or Non-Fiction")
        return category 
    #The test is passing but when run in the shell it only comes out with the ValueError

    @validates('title')
    def validates_title(self, key, title):
        if title != "Won't Believe" and title != "Secret" and title != "Top" and title != "Guess":
            raise ValueError("These aren't clickbait-y enough")
        return title