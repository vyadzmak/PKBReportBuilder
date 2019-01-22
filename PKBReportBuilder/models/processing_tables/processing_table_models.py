import logging
from enum import Enum


# collection of value data types
class ValueDataTypesCollection(Enum):
    SIMPLE_VALUE = 0
    GROUP_VALUE = 1
    ARRAY_VALUE = 2
    CONDITION_VALUE = 3


# convert types collection
class ConvertTypesCollection(Enum):
    WITHOUT = 0
    ONLY_NUMBERS = 1
    DATE = 1


# CONDITION TYPES
class ConditionTypesCollection():
    EQUAL = 0
    NOT_EQUAL = 1
    MORE_THAN = 2
    LESS_THAN = 3
    EXISTS = 4


# OUTPUT|EXTRACTED FORMAT
class OutputValueTypesCollection(Enum):
    WITHOUT = 0
    ONLY_NUMBERS = 1
    DATE = 1
    MONEY_FORMAT = 2
    THOUSAND_FORMAT = 3


# condition value
class ConditionValue():
    # constructor
    def __init__(self,
                 # path to xml condition block
                 path_to_condition,
                 # condition value attribute path value in xml block
                 value_for_check_condition_attribute,
                 # path to extracted value
                 path_to_value,
                 # attribute for extracted path value in xml block
                 value_attribute,
                 # ConvertTypesCollection for condition value
                 convert_value_for_checking_type,
                 # ConvertTypesCollection for extract value
                 convert_value_type,
                 # ConditionTypesCollection
                 condition_logic,
                 # condition equal values array
                 condition_equal_values,
                 # is mulitple value or single
                 is_mutiple_values=False):
        try:

            self.path_to_condition = path_to_condition
            self.value_for_check_condition_attribute = value_for_check_condition_attribute
            self.path_to_value = path_to_value
            self.value_attribute = value_attribute,
            self.convert_value_for_checking_type = convert_value_for_checking_type
            self.convert_value_type = convert_value_type
            self.condition_logic = condition_logic
            self.condition_equal_values = condition_equal_values
            self.is_mutiple_values = is_mutiple_values

        except Exception as e:
            logging.error("Error initialization. " + str(e))


# processing table cells
class ProcessingTableCell():
    # constructor
    def __init__(self, column):
        try:
            self.value = ""
            self.column = column
            self.index = column.index

            pass
        except Exception as e:
            logging.error("Error initialization. " + str(e))


# processing table row
class ProcessingTableRow():
    # constructor
    def __init__(self, index, columns):
        try:
            self.index = index
            self.columns = columns
            self.cells = []
        except Exception as e:
            logging.error("Error initialization. " + str(e))

    # self init row cells by column params
    def init_cells_by_columns(self):
        try:
            for column in self.columns:
                self.cells.append(ProcessingTableCell(column))
        except Exception as e:
            logging.error("Error initialization. " + str(e))


# processing table header
class ProcessingTableColumn():
    # constructor
    def __init__(self, index, title, name, value_data_type_index, value_paths, value_attribute, title_paths="",
                 title_attribute=""):
        try:
            self.title = title
            self.name = name
            self.index = index
            self.value_paths = value_paths
            self.value_data_type = ValueDataTypesCollection(value_data_type_index)

            self.alt_value_check = None
            self.alt_value_paths = None
            self.condition_value = None

            self.value_attribute = None
            self.conditions = None
            self.value_type = None


        except Exception as e:
            logging.error("Error initialization. " + str(e))


# class processing table, for complex analyse
class ProcessingTable():
    # constructor
    def __init__(self, title):
        try:
            self.title = ""
            self.columns = []
            self.rows = []
            self.group_rows = []
            self.hidden_columns_in_groups = []
        except Exception as e:
            logging.error("Error initialization. " + str(e))

    # init single column
    def init_column(self, title, name, value_data_type_index, value_paths, value_attribute, title_paths="",
                    title_attribute=""):
        try:
            column_index = len(self.columns) + 1
            column = ProcessingTableColumn(column_index, title, name, value_data_type_index, value_paths,
                                           value_attribute, title_paths=title_paths, title_attribute=title_attribute)
            self.columns.append(column)

        except Exception as e:
            logging.error("Error initialization. " + str(e))

    # def group rows by column values
    def group_rows_by_values(self, column):
        try:
            pass
        except Exception as e:
            logging.error("Error initialization. " + str(e))
