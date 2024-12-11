import logging

#logging settings

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("mero_logs_heru.log"),
        logging.StreamHandler()
    ]
)

#logger is for this module 'arithmetic'
logger=logging.getLogger("ArithmeticApp")

def add(a,b):
    result=a+b
    logger.debug(f"adding {a} + {b}= {result}")
    return result

def subtract(a,b):
    result = a - b
    logger.debug(f"subtracting {a} - {b} = {result}")
    return result

def multiplication(a,b):
    result = a * b
    logger.debug(f"multiplying {a} * {b} = {result}")
    return result

def divide(a,b):
    try:
        result = a / b
        logger.debug(f"dividing {a} / {b} = {result}")
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None

add(4,8)
subtract(10,5)
multiplication(3,3)
divide(6,2)
