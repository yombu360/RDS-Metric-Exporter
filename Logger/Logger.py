import logging

LOG_FORMAT = (
    "%(asctime)s [%(levelname)s]: %(message)s"
)
LOG_LEVEL = logging.INFO


class Logger:

    @classmethod
    def __get_logger(cls):
        formatter = logging.Formatter(LOG_FORMAT)
        handler = logging.StreamHandler()

        handler.setFormatter(formatter)

        logger = logging.getLogger()
        logger.setLevel(LOG_LEVEL)
        logger.addHandler(handler)
        return logger

    @classmethod
    def publish_log_error(cls, message):
        logger = cls.__get_logger()
        logger.error(message)

    @classmethod
    def publish_log_info(cls, message):
        logger = cls.__get_logger()
        logger.info(message)
