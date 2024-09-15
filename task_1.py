# Задание 1. Логирование с использованием нескольких файлов
# Напишите скрипт, который логирует разные типы сообщений в разные файлы.
# Логи уровня DEBUG и INFO должны сохраняться в debug_info.log,
# а логи уровня WARNING и выше — в warnings_errors.log
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

my_format = logging.Formatter('{levelname:<10} - {asctime:<10} - {msg}',style='{')


logger_debug = logging.FileHandler('debug_info.log',encoding='utf-8')
logger_debug.setLevel(logging.DEBUG)
logger_debug.setFormatter(my_format)
logger.addHandler(logger_debug)

logger_warning = logging.FileHandler(filename='warnings_errors.log',encoding='utf-8')
logger_warning.setLevel(logging.WARNING)
logger_warning.setFormatter(my_format)
logger.addHandler(logger_warning)

logger.info("Это сообщение уровня INFO")
logger.critical("Это сообщение уровня CRITICAL")
logger.error("Это сообщение уровня ERROR")




