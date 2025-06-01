import os
from django.core.wsgi import get_wsgi_application
from pathlib import Path

from whitenoise import WhiteNoise
BASE_DIR = Path(__file__).resolve().parent.parent


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pinetwork.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))
app = application