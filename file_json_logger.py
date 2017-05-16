import logging
import json_log_formatter
from uuid import uuid4

ERROR = "ERROR"
DEBUG = "DEBUG"
CRITICAL = "CRITICAL"
INFO = "INFO"
WARNING = "WARNING"


class CustomJsonLogger:
    def __init__(self, filename):
        self.uuid = str(uuid4())
        formatter = json_log_formatter.JSONFormatter()

        json_handler = logging.FileHandler(filename=filename + ".logs")
        json_handler.setFormatter(formatter)

        self.logger = logging.getLogger('my_json')
        self.logger.addHandler(json_handler)
        self.logger.setLevel(logging.DEBUG)

    def warning(self, message, params=None):
        if not params:
            params = {}
        params["log_id"] = self.uuid
        params["level"] = WARNING
        self.logger.warning(message, extra=params)

    def error(self, message, params=None):
        if not params:
            params = {}
        params["log_id"] = self.uuid
        params["level"] = ERROR
        self.logger.error(message, extra=params)

    def info(self, message, params=None):
        if not params:
            params = {}
        params["log_id"] = self.uuid
        params["level"] = INFO
        self.logger.info(message, extra=params)

    def critical(self, message, params=None):
        if not params:
            params = {}
        params["log_id"] = self.uuid
        params["level"] = CRITICAL
        self.logger.critical(message, extra=params)

    def debug(self, message, params=None):
        if not params:
            params = {}
        params["log_id"] = self.uuid
        params["level"] = DEBUG
        self.logger.debug(message, extra=params)
