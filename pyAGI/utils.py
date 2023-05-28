import logging
import colorlog

_LOG_COLORS = {
    "DEBUG": "cyan",
    "INFO": "green",
    "WARNING": "yellow",
    "ERROR": "red",
    "CRITICAL": "bold_red",
}


def setup_logger(logger_name, level=logging.DEBUG):
    handler = logging.StreamHandler()
    handler.setLevel(level)

    formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s %(message)s",
        datefmt=None,
        reset=True,
        log_colors=_LOG_COLORS,
    )
    handler.setFormatter(formatter)

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    logger.addHandler(handler)

    file_handler = logging.FileHandler("py-agi.log")
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(level)
    logger.addHandler(file_handler)

    return logger


def log_header(logger: logging.Logger, title: str):
    logger.info("\033[92m" + f"**************** {title} ****************" + "\033[0m")


def log_content(logger: logging.Logger, content: str):
    logger.info("\033[97m" + content.strip() + "\033[0m")
