import models.processing_tables.processing_table_models as processing_table_models
import logging


# init exsisting table
def init_existing_contracts_table(root):
    try:

        table_path = ['Result', 'Root', 'ExistingContracts', 'Contract']
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

                          ], 'value',
                          processing_table_models.ConditionValue(None, None, None, 'value', None,
                                                                 processing_table_models.ConvertTypesCollection(0),
                                                                 None, None, None, False),
                          processing_table_models.ExtractValueTypesCollection(1), True
                          )

        # column Роль Субъекта (гарант, созаемщик, заемщик)
        table.init_column("Наименование Заемщика/гаранта/созаемщика", "SubjectRole",
                          [
                              [
                                  ['SubjectRole']
                              ]

                          ], 'value',
                          processing_table_models.ConditionValue(None, None, None, 'value', None,
                                                                 processing_table_models.ConvertTypesCollection(0),
                                                                 None, None, None, True),
                          processing_table_models.ExtractValueTypesCollection(2), False
                          )

        # column Наименование Банка
        table.init_column("Наименование Банка", "FinancialInstitution",
                          [
                              [
                                  ['FinancialInstitution'],
                              ]

                          ], 'value',
                          processing_table_models.ConditionValue(None, None, None, 'value', None,
                                                                 processing_table_models.ConvertTypesCollection(0),
                                                                 None, None, None, False),
                          processing_table_models.ExtractValueTypesCollection(2), False
                          )

        # column Тип КЛ
        table.init_column("Тип КЛ", "TypeOfFoundingn",
                          [
                              [
                                  ['TypeOfFounding'],
                              ]

                          ], 'value',
                          processing_table_models.ConditionValue(None, None, None, 'value', None,
                                                                 processing_table_models.ConvertTypesCollection(0),
                                                                 None, None, None, False),
                          processing_table_models.ExtractValueTypesCollection(2), False
                          )

        # column Номер договора
        table.init_column("Номер договора", "AgreementNumber",
                          [
                              [
                                  ['AgreementNumber'],
                              ]

                          ], 'value',
                          processing_table_models.ConditionValue(None, None, None, 'value', None,
                                                                 processing_table_models.ConvertTypesCollection(0),
                                                                 None, None, None, False),
                          processing_table_models.ExtractValueTypesCollection(2), False
                          )

        # column Номер договора
        table.init_column("Лимит/ Общая сумма кредита (тыс. тенге)", "TotalAmount",
                          [
                              [
                                  ['TotalAmount'],
                              ]

                          ], 'value',
                          processing_table_models.ConditionValue(None, None, None, 'value', None,
                                                                 processing_table_models.ConvertTypesCollection(1),
                                                                 None, None,
                                                                 [
                                                                     #only numbers
                                                                     processing_table_models.OutputValueTypesCollection(
                                                                         1),
                                                                     #money format
                                                                     processing_table_models.OutputValueTypesCollection(
                                                                         3),
                                                                     #thousand
                                                                     processing_table_models.OutputValueTypesCollection(
                                                                         4)
                                                                 ],
                                                                 False),
                          processing_table_models.ExtractValueTypesCollection(2), False
                          )

        return table
    except Exception as e:
        pass


# init document processing dtables
def init_document_tables(root):
    try:
        tables = []
        existing_contracts_table = init_existing_contracts_table(root)
        tables.append(existing_contracts_table)

        return tables
    except Exception as e:
        logging.error("Error initialization. " + str(e))
