import os
from pkg_resources import Requirement, resource_filename
from repomaker.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIR, 'db.sqlite3'),
    }
}

SINGLE_USER_MODE = True

ALLOWED_HOSTS = [os.getenv('REPOMAKER_HOSTNAME')]
SECRET_KEY = os.getenv('REPOMAKER_SECRET_KEY')
DEBUG = True

DEFAULT_REPO_STORAGE = [
    (os.path.join(DATA_DIR, 'repos'), 'https://%s/repos/' % os.getenv('REPOMAKER_HOSTNAME')),
]

if DEBUG:
    SASS_PROCESSOR_ENABLED = False
