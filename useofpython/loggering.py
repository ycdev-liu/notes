

# 学习logging的使用
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')  
logger.error('This is an error message')

# 输出INFO下面的等级的日志

