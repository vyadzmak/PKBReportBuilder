import logging
import models.export_models.export_document_elements as export_document_models

#export  document
class ExportDocument():
    #constructor
    def __init__(self):
        try:
            #export elements
            export_elements =[]
        except Exception as e:
            logging.error("Error initialization. " + str(e))




    #add export elements
    def add_export_element(self,type):
        try:
            element = export_document_models.ExportDocumentElement(type)

        except Exception as e:
            logging.error("Error initialization. " + str(e))


    #init document schemas elements
    def init_document_elements(self):
        try:
            pass
        except Exception as e:
            logging.error("Error initialization. " + str(e))