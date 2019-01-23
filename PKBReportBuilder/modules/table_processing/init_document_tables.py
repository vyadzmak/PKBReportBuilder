import models.processing_tables.processing_table_models as processing_table_models
import logging


# init exsisting table
def init_existing_contracts_table(root):
    try:

        table_path = ['Result', 'Root','ExistingContracts','Contract']
        table = processing_table_models.ProcessingTable("Действующие договора", root, table_path)

        # column Наименование Заемщика/гаранта/ созаемщика
        table.init_column("Наименование Заемщика/гаранта/созаемщика", "Name",
                          [
                              [
                                  ['Result', 'Root', 'Header', 'Surname'],
                                  ['Result', 'Root', 'Header', 'Name'],
                                  ['Result', 'Root', 'Header', 'FathersName']
                              ],
                              [
                                  ['Result', 'Root', 'Header', 'NameNative']
                              ]

                          ],'value',
                          processing_table_models.ConditionValue(None, None, None, 'value', None,
                                                                 processing_table_models.ConvertTypesCollection(0),
                                                                 None, None, False),
                          processing_table_models.ExtractValueTypesCollection(1), True
                          )

        # column Роль Субъекта (гарант, созаемщик, заемщик)
        table.init_column("Наименование Заемщика/гаранта/созаемщика", "SubjectRole",
                          [
                              [
                                  ['Result', 'Root', 'ExistingContracts','Contract', 'SubjectRole'],

                              ]

                          ],'value',
                          processing_table_models.ConditionValue(None,None,None,'value',None,processing_table_models.ConvertTypesCollection(0),
                                                                 None,None,True),
                          processing_table_models.ExtractValueTypesCollection(2), False
                          )

        # column Наименование Банка
        table.init_column("Наименование Банка", "FinancialInstitution",
                          [
                              [
                                  ['Result', 'Root', 'ExistingContracts','Contract', 'FinancialInstitution'],
                              ]

                          ],'value',
                          processing_table_models.ConditionValue(None, None, None, 'value', None,
                                                                 processing_table_models.ConvertTypesCollection(0),
                                                                 None, None, False),
                          processing_table_models.ExtractValueTypesCollection(2), False
                          )

        return table
    except Exception as e:
        pass


# init document processing dtables
def init_document_tables(root):
    try:
        tables =[]
        existing_contracts_table =init_existing_contracts_table(root)
        tables.append(existing_contracts_table)

        return tables
    except Exception as e:
        logging.error("Error initialization. " + str(e))
