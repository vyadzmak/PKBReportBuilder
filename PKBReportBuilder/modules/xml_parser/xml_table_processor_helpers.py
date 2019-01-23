import logging

#extract value from field non table content
def extract_data_from_extra_table_field(root, column):
    try:
        return ""

        pass
    except Exception as e:
        logging.error("Error. " + str(e))


#extract value from xml table
def extract_data_from_table_row(xml_row, column):
    try:
        return ""
        pass
    except Exception as e:
        logging.error("Error. " + str(e))
