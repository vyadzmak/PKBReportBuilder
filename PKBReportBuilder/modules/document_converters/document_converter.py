import logging
import models.export_models.sheet_models as sheet_models

#convert document to sheet format
def convert_document_to_sheet_format(document):
    try:
        sheet_document = sheet_models.Sheet()

        pass
    except Exception as e:
        logging.error("Error. " + str(e))
