import xml.etree.ElementTree as ET
import models.export_models.export_document as export_document
import modules.xml_parser.xml_processor as xml_processor
import modules.document_converters.document_converter as document_converter
import logging
import modules.io_modues.io_module as io_module

# parse physical file XML
def parse_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        document = export_document.ExportDocument()
        document.init_document_elements()
        xml_processor.process_document(root, document)
        result =document_converter.convert_document_to_sheet_format(document)
        logging.info("File parse  successfully completed")
        io_module.export_json_to_file(result)
        return result
    except Exception as e:
        logging.error("Error. " + str(e))


# parse data string
def parse_data_string(data):
    try:
        root = ET.fromstring(data)
        pass
    except Exception as e:
        logging.error("Error. " + str(e))
