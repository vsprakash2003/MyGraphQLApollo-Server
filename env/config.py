import os

# How to set environment variables in Mac
# Open up Terminal.
# Run the following command: sudo nano /etc/paths
#              (or sudo vim /etc/paths for vim)
# Go to the bottom of the file, and enter the path you wish to add.
# Hit control-x to quit.
# Enter 'Y' to save the modified buffer.
# Open a new terminal window then type: echo $PATH


class Config(object):
    DEBUG = False
    TESTING = False
    os.environ['DATABASE_URL'] = 'sqlite:///database.sqlite3'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # env variable
    