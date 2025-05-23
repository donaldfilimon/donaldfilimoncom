import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_settings.settings")

application = get_wsgi_application()

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("wsgi.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info("WSGI application initialized.")
