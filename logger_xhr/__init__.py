import logging.config
import os
import shutil
import utils_xhr
from logger_xhr.logger_ import getLoger
class config:
    def __new__(self):
        raise TypeError('初始化异常。该类config只能作为命名空间使用，不可进行初始化或者对象的创建')
    @staticmethod
    def createConfigFileTempl(path='logging.ini',configArgs={'loggerName':'applog','savePath':'applog.log'}):
        """
        创建log的配置文件模板。
        :param path: 配置文件的路径。默认在当前文件夹创建
        :return:
        """
        if not path.endswith('.ini') and not path.endswith('.conf'):
            raise NameError('配置文件名称错误:{},必须以ini结尾或者.conf结尾的文件才能作为配置文件'.format(path))
        try:
            shutil.copyfile('logger_xhr/souce/logging.ini.templ', path)
        except FileNotFoundError as e:
            os.makedirs(os.path.dirname(path))
            shutil.copyfile('logger_xhr/souce/logging.ini.templ', path)
        utils_xhr.io.replaceFileSign(path=path,signs=[('@loggerName@',configArgs.get('loggerName')),('@savePath@',configArgs.get('savePath'))])
        # fp=open(file=os.path.dirname(path),mode='w')
        # fp.close()
    @staticmethod
    def fileConfig(filePath):
        """
        读取logging配置文件路径。如果没有该配置文件。可以使用logger_xhr.config.createConfigFileTempl()方法进行创建
        :param filePath: 配置文件的路径
        :return:
        """
        if os.path.exists(filePath)==False:
            raise FileNotFoundError('该配置文件不存在:'+filePath+';请检查该路径')
        if not filePath.endswith('.ini') and not filePath.endswith('.conf'):
            raise NameError('配置文件名称错误:{},必须以ini结尾或者.conf结尾的文件才能作为配置文件'.format(filePath))
        try:
            logging.config.fileConfig(filePath)
        except FileNotFoundError as e:
            dirPath=os.path.dirname(e.filename)
            if not os.path.exists(dirPath):
                os.mkdir(dirPath)
                logging.config.fileConfig(filePath)
            else:
                raise e
def getLogger(name='root'):
    """
    获得日志对象。
    :param name:
    :return:
    """
    return getLoger(name)

__all__=['config','getLogger']