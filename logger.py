import logging

import time

log_file = "./logger/"
currTime = time.strftime('%Y-%m-%d %H:%M:%S')  # 格式化当前时间
log_name = log_file + currTime + '.log'  # 设置日志文件名称
log_level = logging.DEBUG
logger = logging.getLogger("loggerr")
handler = logging.FileHandler(log_name)
formatter = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(log_level)

# test
logger.debug("this is a debug msg!")
logger.info("this is a info msg!")
logger.warning("this is a warn msg!")
logger.error("this is a error msg!")
logger.critical("this is a critical msg! \n")