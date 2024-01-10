from configparser import ConfigParser

def readConfig(section, key):
    config = ConfigParser()
    config.read("C:\\Users\\pmrig\\OneDrive\\Desktop\\PDevelopment\\POM_design_framework\\ConfigurationData\\config.ini")
    return config.get(section, key)