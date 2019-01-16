import xml.etree.ElementTree as ET
import models.export_models.export_document as export_document
import modules.xml_parser.xml_processor as xml_processor
import modules.document_converters.document_converter as document_converter
import logging


# parse physical file XML
def parse_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        document = export_document.ExportDocument()
        document.init_document_elements()
        xml_processor.process_document(root, document)
        document_converter.convert_document_to_sheet_format(document)

        # path1 = ['Result', 'Root', 'PublicSources', 'FalseBusi']
        # path2 = ['Status']
        # ob = recursive_navigate(root, path1, 0)
        # ob1 = recursive_navigate(ob, path2, 0)
        logging.info("File parse  successfully completed")
    except Exception as e:
        logging.error("Error. " + str(e))


# parse data string
def parse_data_string(data):
    try:
        root = ET.fromstring(data)
        pass
    except Exception as e:
        logging.error("Error. " + str(e))
