import xml.etree.ElementTree as ET
import modules.xml_parser.xml_helpers as xml_helpers
import modules.xml_parser.xml_tree_builder as tree_builder
import models.export_models.export_document as export_document
import logging


#parse xml file
def recursive_navigate(node, paths, index):
    try:
        r =node
        for result in node.findall(paths[index]):
            if (index<len(paths)-1):
                return recursive_navigate(result,paths,index+1)
                # break
            else:
                return result

        return None
    except Exception as e:
        logging.error("Error. " + str(e))

#parse physical file XML
def parse_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        path1 = ['Result','Root','PublicSources','FalseBusi']
        path2 = ['Status']
        ob =recursive_navigate(root,path1,0)
        ob1 =recursive_navigate(ob,path2,0)
        for result in root.findall('Result'):
            for r_result in result.findall('Root'):
                t =0

        pass
    except Exception as e:
        logging.error("Error. " + str(e))


#parse data string
def parse_data_string(data):
    try:
        root = ET.fromstring(data)
        pass
    except Exception as e:
        logging.error("Error. " + str(e))
