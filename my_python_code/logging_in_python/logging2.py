import logging

#configuring logging

logging.basicConfig(
    filename='app.log',#creates log file , and msg will be appended there.
    filemode = 'w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    )

logging.debug(" This is debug message")
logging.info(" This is info message")
logging.warning(" This is warning message")
logging.error(" This is error message")
logging.critical(" This is critical message")

"""at the end of the day if we are logging then we really need to save in
the file, this i am doing in line 6 above"""

