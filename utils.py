import logging

def setup_logger():
    logger = logging.getLogger("ETL")
    logger.setLevel(logging.INFO)

    if not logger.handlers:

        ch = logging.StreamHandler()
        fh = logging.FileHandler("logs/etl.log")

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger
