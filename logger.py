# importing module
import logging

class Logger:
    """
    Attributes
    ----------
    _file_name : str
        name of log file created
    Methods
    -------
    get_logger_object():
        Configure logger params and returns logger object
        :return: logger object

    """
    def __init__(self):
        # Create and configure logger
        self._file_name = "vehicle-inventory.log"

    def get_logger_object(self):
        """
        Configure logger params and returns logger object
        :return: logger object
        """
        logging.basicConfig(filename=self._file_name, filemode='w', format='%(asctime)s %(levelname)s: %(message)s')
        logging.root.setLevel(logging.NOTSET)
        logger = logging.getLogger()
        logger.info("Starting logger module")
        return logger