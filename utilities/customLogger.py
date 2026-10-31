import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            filemode="a",
                            encoding="utf-8",
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S',
                            level=logging.INFO,
                            force=True
                            )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger