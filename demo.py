from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

import logger_xhr
#创建config模板
# logger_xhr.config.createConfigFileTempl(path='haha.ini',configArgs={'loggerName':'testLog','savePath':'aa/testLog.log'})
logger_xhr.config.fileConfig('haha.ini')
# TimedRotatingFileHandler()
# #
logger=logger_xhr.getLogger(name='testLog')
logger.warning('你好')
logger.warning('你好33')
