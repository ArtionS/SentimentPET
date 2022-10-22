from com.petmedic import properties


class Logger:
    level = properties.log_level
    __DEBUG = "debug"
    __INFO = "info"

    def debug(self, message):
        if self.__DEBUG == self.level:
            print(message)

    def info(self, message):
        if self.__DEBUG == self.level or self.__INFO == self.level or self.level is None:
            print(message)


Log = Logger()
