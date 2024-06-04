import logging


class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        if "extra" in kwargs:
            return f"{kwargs['extra']['name']} - {msg}", kwargs
        return msg, kwargs


def setup_logger():
    log = logging.getLogger("multi_category_logger")
    log.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)

    log.addHandler(ch)

    return CustomAdapter(log, {})


log = setup_logger()
