import configparser

configFile = "config.ini"


class ConfigError(Exception):
    pass


class DuplicateConfigError(ConfigError):
    pass


class NoConfigError(ConfigError):
    pass


def configParser():
    config = configparser.ConfigParser()  # 创建对象
    config.read(configFile, encoding="utf-8")  # 读取配置文件，如果配置文件不存在则创建
    return config


def checkConfig():
    config = configParser()
    for section in config.sections():
        # 检查是否有同一个section同名的key
        keys = config.options(section)
        setKeys = set(keys)
        if keys.__len__() != setKeys.__len__():
            raise DuplicateConfigError("Has the same name attribute in the section: " + section)


def updateConfig(section, itemDict):
    config = configParser()
    for key, value in itemDict.items():
        if config.has_option(section, key) is False:
            raise NoConfigError('no such item ' + key + ' in ' + section)
        config.set(section, key, value)

    # writeConfig
    with open(configFile, 'w') as configfile:
        config.write(configfile)


class Setting:
    sectionName = 'setting'

    @staticmethod
    def get():
        tupleList = configParser().items(section=Setting.sectionName)
        d = {}
        for key, value in tupleList:
            d[key] = value
        return d

    @staticmethod
    def update(itemDict):
        updateConfig(Setting.sectionName, itemDict)


class UiSetting:

    @staticmethod
    def setIntoDict(tuplelist):
        d = {}
        for key, value in tuplelist:
            d[key] = value
        return d

    @staticmethod
    def get():
        d = {}
        tupleList = configParser().items(section="info")
        d.update({"info": UiSetting.setIntoDict(tupleList)})
        tupleList = configParser().items(section="contact")
        d.update({"contact": UiSetting.setIntoDict(tupleList)})
        tupleList = configParser().items(section="uisetting")
        d.update({"uisetting": UiSetting.setIntoDict(tupleList)})
        tupleList = configParser().items(section="footer")
        d.update({"footer": UiSetting.setIntoDict(tupleList)})

        sectionNames = configParser().sections()
        moneySetions = []
        for section in sectionNames:
            if section.startswith("money-"):
                moneySetions.append(section)

        d["money"] = []
        for money in moneySetions:
            d["money"].append({"name": configParser().get(money, "name"), "src": configParser().get(money, "src")})

        return d

    @staticmethod
    def update(itemDict):
        updateConfig(Setting.sectionName, itemDict)


if __name__ == '__main__':
    # d = Setting().get()
    # print(d.get("MySQL_password"))
    # print(d)
    d=UiSetting.get()
    print(d)
