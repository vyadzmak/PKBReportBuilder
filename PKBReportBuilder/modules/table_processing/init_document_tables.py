import models.processing_tables.processing_table_models as processing_table_models
import logging


# init exsisting table
def init_existing_contracts_table():
    try:
        table = processing_table_models.ProcessingTable("Действующие договора")
        table.init_column("Наименование Заемщика/гаранта/ созаемщика","")




    except Exception as e:
        pass


# init document processing dtables
def init_document_tables():
    try:
        init_existing_contracts_table()

    except Exception as e:
        logging.error("Error initialization. " + str(e))
