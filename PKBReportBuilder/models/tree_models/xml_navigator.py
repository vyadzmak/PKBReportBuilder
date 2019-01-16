import logging

#xml tree navigator
class XmlNavigator():
    #constructor
    def __init__(self,path,value_attribute, convert_types, style):
        try:
            self.path = path
            self.value_attribute = value_attribute
            self.convert_types = convert_types
            self.style =style
        except Exception as e:
            logging.error("Error initialization. " + str(e))
