from logger import logging

def add(a,b):

    logging.debug("the addition is taking place")
    return a+b

logging.debug("The addition function is called")
add(10,15)

"""
this is create log message inside 'app.log' file
"""
