from mongoengine import Document, StringField, BooleanField
from django.contrib.auth.hashers import make_password

# Define User model using MongoEngine
class User(Document):
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)

# Create superuser
def create_superuser():
    username = "admin"
    email = "admin@example.com"
    password = "adminpassword"

    if not User.objects(username=username).first():
        hashed_password = make_password(password)
        user = User(username=username, email=email, password=hashed_password, is_staff=True, is_superuser=True)
        user.save()
        print("Superuser created successfully!")
    else:
        print("Superuser already exists!")

# Call the function
create_superuser()
