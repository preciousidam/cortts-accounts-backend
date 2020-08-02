import os
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

DEBUG=bool(os.getenv('DEBUG'))
APP= os.getenv('APP')
SERVER_PORT= int(os.getenv('SERVER_PORT'))
ENV= os.getenv('ENV')
SECRET_KEY= os.getenv('SECRET_KEY')


JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY')
SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS=bool(os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS'))


'''MAIL_DEFAULT_SENDER=os.getenv('MAIL_DEFAULT_SENDER')
MAIL_SERVER=os.getenv('MAIL_SERVER')
MAIL_PORT=int(os.getenv('MAIL_PORT'))
MAIL_DEBUG= True
MAIL_USERNAME=os.getenv('MAIL_USERNAME')
MAIL_PASSWORD=os.getenv('MAIL_PASSWORD')
MAIL_SUPPRESS_SEND= False
MAIL_USE_TLS=False
MAIL_USE_SSL=True'''