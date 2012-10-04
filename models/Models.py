from google.appengine.ext import db

class Topic(db.Model):
    #length limits to be finalized here also the default properties
    title = db.StringProperty() 
    description = db.TextProperty()
    access_type = db.IntegerProperty()
    owner = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty()
    modifier = db.StringProperty()
    is_deleted = db.BooleanProperty()
    
    
    