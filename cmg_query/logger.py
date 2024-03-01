# create logger
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# formatter = logging.Formatter('[%(asctime).19s] [%(levelname).3s] %(message)s')
formatter = logging.Formatter('[%(asctime).19s] [%(levelname)s] %(message)s')

# handler = logging.FileHandler('../logs/app.log')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)




