import logging
import os
from datetime import datetime

# Create a log file name using current date and time
# Example: 05_31_2026_12_45_30.log
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create path: current_directory/logs/<log_file_name>
# os.getcwd() returns the current working directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the directory if it doesn't already exist
# exist_ok=True prevents an error if the folder already exists
os.makedirs(logs_path, exist_ok=True)

# Full path to the log file
# Example:
# C:/Project/logs/05_31_2026_12_45_30.log/05_31_2026_12_45_30.log
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging system
logging.basicConfig(
    # Store logs in the specified file
    filename=LOG_FILE_PATH,

    # Format of each log message
    # asctime  -> timestamp
    # lineno   -> line number where logging was called
    # name     -> logger/module name
    # levelname-> INFO, ERROR, WARNING, etc.
    # message  -> actual log message
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",

    # Log messages of INFO level and above
    # Levels: DEBUG < INFO < WARNING < ERROR < CRITICAL
    level=logging.INFO,
)