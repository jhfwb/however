# logger_xhr包说明
> 包简介：

## 1.包的安装:
```cmd
pip install logger_xhr@git+https://github.com/...(后面加上文件的位置)

eg：
pip install  logger_xhr@git+https://github.com/jhfwb/logger_xhr#egg=logger_xhr
```

## 2.如何开始运行logger_xhr

## 3.logger_xhrの主要功能及介绍

#### 配置文件信息：

```ini
#config.ini
#此配置文件需要删掉注释
[loggers]
#注册日志记录器。root必加，因为是默认日志记录器
keys=root,testLog

[handlers]
#注册处理器。
#fileHandler文件处理器
#consoleHandler控制台处理器
keys=fileHandler,consoleHandler

[formatters]
#注册格式器
#simpleFormatter 普通格式
#colorFormatter 彩色字体格式：控制台用
keys=simpleFormatter,colorFormatter

[logger_root]
#定义root日志记录器
#设置处理级别，低于处理级别不做处理
level=DEBUG

#定义处理器，这里只用到控制处理器
handlers=consoleHandler


[logger_testLog]
#这个是自定义的日志处理器
level=DEBUG

#这里定义了两个
handlers=fileHandler,consoleHandler

#非root logger 此为testLog的名称，必须写，这里
qualname = testLog

#propagete=0,表示输出日志，但消息不传递，propagate=1是输出日志，同时消息往更高级别的地方传递 控制台会出现重复日志
propagate=0


[handler_consoleHandler]
class=StreamHandler
args=(sys.stdout,)
level=DEBUG
formatter=colorFormatter


[handler_fileHandler]
class=handlers.TimedRotatingFileHandler
#（日志的名称，间隔单位，间隔时间，文件保留个数）
# 间隔时间
#'S'         |  秒
#'M'         |  分
#'H'         |  时
#'D'         |  天
#'W0'-'W6'   |  周一至周日
# midnight'  |  每天的凌晨
#这个代表该文件，间隔10秒会重新创建一个新的文件，最多保留5个文件，多余文件会被删除掉。
#这个参数跟类TimedRotatingFileHandler的初始化参数是一致的。
args=('aa/testLog.log','S',10,5) 
level=DEBUG
formatter=simpleFormatter


[formatter_simpleFormatter]
format=%(asctime)s|%(levelname)8s|%(filename)s[:%(lineno)d]|%(message)s
datefmt=%Y-%m-%d %H:%M:%S

[formatter_colorFormatter]
class=colorlog.ColoredFormatter
format=%(log_color)s[ %(asctime)s |%(levelname)8s | %(filename)s[:%(lineno)d] ] %(message)s
datefmt=%Y-%m-%d %H:%M:%S

```
```python
when
'S'         |  秒

 'M'         |  分

 'H'         |  时

 'D'         |  天

 'W0'-'W6'   |  周一至周日

 'midnight'  |  每天的凌晨
```

```python

```




## 4.logger_xhrの目录结构

## 5.logger_xhrの原理
