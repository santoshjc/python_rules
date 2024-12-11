"""
Logging is a means of tracking events that happen when some software runs.
Logging is important for software developing, debugging, and running. If you
don’t have any logging record and your program crashes, there are very few
chances that you detect the cause of the problem

print statements are not pythonic , logging is pythonic
steps:-when we import logging we have to configure the basic logging settings
"""
import logging

#configuring the basic logging settings
logging.basicConfig(level=logging.DEBUG)

#log messages
logging.debug(" This is debug message")
logging.info(" This is info message")
logging.warning(" This is warning message")
logging.error(" This is error message")
logging.critical(" This is critical message")
