import logging 

logging.basicConfig(level=logging.DEBUG,
                    format="[%(filename)s] | %(levelname)s - %(lineno)s | %(asctime)s | Message: %(message)s",
                    datefmt="%Y/%m/%d %I:%M:%S",
                    filename="logs/logging.log",
                    filemode="a"
)
