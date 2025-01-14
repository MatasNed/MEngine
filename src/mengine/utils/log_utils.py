import logging

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )

def logging_deco(func):
    def wrapper(*args, **kwargs):
        logging.debug(f"log before by {func}")
        result = func(*args, **kwargs)
        logging.debug(f"log after execution")
        return result

    return wrapper