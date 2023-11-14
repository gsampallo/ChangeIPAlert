import os
import logging
from datetime import datetime


class Log:

    def __init__(self):
        
        self.log_folder = "./logs"
        if not os.path.isdir(self.log_folder):
            os.makedirs(self.log_folder)
        logfile = f"./{self.log_folder}/{datetime.today().strftime('%Y%m%d')}.log"
        logging.basicConfig(filename=logfile, level=logging.INFO)
        logging.info("ChangeIPAlert at "+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def log(self,text):
        logging.info(text)
    



