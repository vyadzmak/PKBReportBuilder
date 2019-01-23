import models.processing_tables.processing_table_models as processing_table_models
import logging


# init exsisting table
def init_existing_contracts_table():
    try:

        table = processing_table_models.ProcessingTable("Действующие договора")

        #column Наименование Заемщика/гаранта/ созаемщика
        table.init_column("Наименование Заемщика/гаранта/созаемщика", "Name",
                          [
                              ['Result', 'Root', 'Header', 'Surname'],
                              ['Result', 'Root', 'Header', 'Name'],
                              ['Result', 'Root', 'Header', 'FathersName']
                          ],
                          processing_table_models.ConditionValue(None,None,None,None,None,processing_table_models.ConvertTypesCollection(0),None,None,False),
                          processing_table_models.ExtractValueTypesCollection(2), True
                          )




    except Exception as e:
        pass


# init document processing dtables
def init_document_tables():
    try:
        init_existing_contracts_table()

    except Exception as e:
        logging.error("Error initialization. " + str(e))
