# import logging
# from graypy import GELFUDPHandler
# import os
# from functools import wraps
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# def gathering_graylogger_info():
#     return {
#         "graylog_host": os.getenv("GRAYLOG_HOST", "localhost"),
#         "graylog_port": int(os.getenv("GRAYLOG_PORT", 12201)),
#         "app_name": os.getenv("APP_NAME", "fastapi_app"),
#         "environment": os.getenv("ENVIRONMENT", "dev"),
#     }


# class BaseLoggerConfig:
#     def __init__(self, log_level, server_info):
#         self.log_level = log_level
#         self.server_info = server_info

#     def configure_graylog_handler(self):
#         handler = GELFUDPHandler(
#             self.server_info.get("graylog_host"),
#             self.server_info.get("graylog_port"),
#         )
#         formatter = logging.Formatter(
#             "%(asctime)s - %(name)s - %(source)s - %(levelname)s - %(message)s",
#             datefmt="%Y-%m-%d %I:%M:%S %p",
#         )
#         handler.setFormatter(formatter)
#         return handler


# class LoggerManager:
#     _loggers = {}

#     @classmethod
#     def get_logger(cls, name, config):
#         if name not in cls._loggers:
#             logger = logging.getLogger(name)
#             logger.setLevel(config.log_level)
#             logger.addHandler(config.configure_graylog_handler())
#             cls._loggers[name] = logger
#         return cls._loggers[name]


# class LoggingComponent:
#     def __init__(self):
#         server_info = gathering_graylogger_info()
#         self.logger_config = BaseLoggerConfig(logging.INFO, server_info)

#     def get_gray_logger(self):
#         return LoggerManager.get_logger("gray_logger", self.logger_config)

# logging_component = LoggingComponent()


import logging
from graypy import GELFUDPHandler
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def gathering_graylogger_info():
    return {
        "graylog_host": os.getenv("GRAYLOG_HOST", "localhost"),
        "graylog_port": int(os.getenv("GRAYLOG_PORT", 12201)),
        "app_name": os.getenv("APP_NAME", "fastapi_app"),
        "environment": os.getenv("ENVIRONMENT", "dev"),
    }


class BaseLoggerConfig:
    def __init__(self, log_level, server_info):
        self.log_level = log_level
        self.server_info = server_info

    def configure_graylog_handler(self):
        handler = GELFUDPHandler(
            self.server_info.get("graylog_host"),
            self.server_info.get("graylog_port"),
        )
        
        # Updated formatter without 'source'
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %I:%M:%S %p",
        )
        
        handler.setFormatter(formatter)
        return handler


class LoggerManager:
    _loggers = {}

    @classmethod
    def get_logger(cls, name, config):
        if name not in cls._loggers:
            logger = logging.getLogger(name)
            logger.setLevel(config.log_level)
            logger.addHandler(config.configure_graylog_handler())
            cls._loggers[name] = logger
        return cls._loggers[name]


class LoggingComponent:
    def __init__(self):
        server_info = gathering_graylogger_info()
        self.logger_config = BaseLoggerConfig(logging.INFO, server_info)

    def get_gray_logger(self):
        return LoggerManager.get_logger("gray_logger", self.logger_config)


# Instantiate the logging component
logging_component = LoggingComponent()
