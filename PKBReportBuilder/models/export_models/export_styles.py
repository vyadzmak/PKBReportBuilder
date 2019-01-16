from models.export_models.export_document_elements import ExportElementStyle
import logging
row_title_style =None
row_value_style = None

table_header_style = None
table_rows_content_style = None

#init styles for export
def init_styles():
    try:
        global row_title_style
        row_title_style = ExportElementStyle(fw="bold")

        global row_value_style
        row_value_style = ExportElementStyle()
        logging.info("Styles init successful")
    except Exception as e:
        logging.error("Error initialization. " + str(e))