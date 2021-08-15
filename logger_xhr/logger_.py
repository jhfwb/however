import logging
import logging.config



def getLoger(name):
    logger = logging.getLogger(name=name)
    return logger

