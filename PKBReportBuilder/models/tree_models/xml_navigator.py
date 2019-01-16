import logging

#xml tree navigator
class XmlNavigator():
    #constructor
    def __init__(self,path,attribute_name, convert_types):
        try:
            self.path = path
            self.attribute_name = attribute_name
            self.convert_types = convert_types
        except Exception as e:
            logging.error("Error initialization. " + str(e))
