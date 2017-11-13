from datetime import datetime

# Define logging default value
LOG_FORMAT = '[%(levelname)s] - %(asctime)s - %(message)s'
LOG_DATE_FORMAT = '%m-%d-%Y %H:%M:%S'
LOG_FILE_NAME = "navitia_deployer_{}.log".format(datetime.now().strftime('%m%d%y_%H%M%S'))
