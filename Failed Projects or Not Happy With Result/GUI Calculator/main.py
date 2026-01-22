import frontend
import logging
import os

def initiate_logging(log_file="log/main.log"):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
# End function

if __name__ == "__main__":
    initiate_logging()
    frontend.initiate_tk()
