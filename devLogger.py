class DevLogger(object):
    def __init__(self, print_logging=True, log_level=1):
        """ Constuctor for dev logger

        :param print_logging: bool for print logging
        :param log_level: int for log level, 1=debug, 2=info, 3=warning, 4=error

        """
        self.print_logging = print_logging
        self.log_level = log_level

    def debug(self, the_str):
        if (self.print_logging and self.log_level <= 1):
            print("DEBUG:: " + the_str)

    def info(self, the_str):
        if (self.print_logging and self.log_level <= 2):
            print("INFO:: " + the_str)

    def warning(self, the_str):
        if (self.print_logging and self.log_level <= 3):
            print("WARNING:: " + the_str)

    def error(self, the_str):
        if (self.print_logging and self.log_level <= 4):
            print("ERROR:: " + the_str)
