import logging

#configuring logging

logging.basicConfig(
    filename='app.log',#creates log file , and msg will be appended there.
    filemode = 'w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    )
