import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_settings.settings")

application = get_asgi_application()

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("asgi.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info("ASGI application initialized.")
