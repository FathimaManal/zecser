import logging

logging.basicConfig(
    filename='logs/system.log',
    level=logging.INFO
)

logger = logging.getLogger(__name__)