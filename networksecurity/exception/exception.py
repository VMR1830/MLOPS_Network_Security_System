import sys
from networksecurity.logging import logger

# Custom exception class for the project
# It extends Python's built-in Exception class
class NetworkSecurityException(Exception):

    # error_message -> actual error object/message
    # error_details -> sys module used to get traceback information
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message

        # exc_info() returns:
        # (exception_type, exception_value, traceback_object)
        _, _, exc_tb = error_details.exc_info()

        # Line number where the exception occurred
        self.lineno = exc_tb.tb_lineno

        # File name where the exception occurred
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    # Defines what gets printed when the exception object is printed
    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name,
            self.lineno,
            str(self.error_message)
        )


# Runs only when this file is executed directly
if __name__ == '__main__':
    try:
        # Write an INFO message to the log file
        logger.logging.info("Enter the try block")

        # Intentionally generate an error
        a = 1 / 0

        # This line will never execute because the previous line raises an exception
        print("This will not be printed", a)

    except Exception as e:
        # Catch the original exception and convert it into
        # our custom exception with file and line details
        raise NetworkSecurityException(e, sys)