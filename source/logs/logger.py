import logging 

logging.basicConfig(level=logging.DEBUG,
                    format="[%(filename)s] | %(levelname)s - %(lineno)s | %(asctime)s | Message: %(message)s",
                    datefmt="%Y/%m/%d %I:%M:%S",
                    filename="source/logs/logging.log",
                    filemode="a"
)
