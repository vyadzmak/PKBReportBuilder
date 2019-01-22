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

#process cell
def process_cell(root, cell):
    try:
        cell_value = ""
        index =0
        for path in cell.paths:
            node = recursive_navigate(root,path,0)
            if (node==None):
                return None
            value = node.get(cell.value_attribute)
            cell_value+=value
            if (index<len(cell.paths)-1):
                cell_value+='\n'
            index+=1

        cell.set_cell_value(cell_value)
        return cell

    except Exception as e:
        logging.error("Error. " + str(e))
        return None


#process single row
def process_row(root,export_element):
    try:
        for cell in export_element.row.cells:
            res =process_cell(root,cell)
            if (res==None):
                export_element.include_in_report =False
        pass
    except Exception as e:
        logging.error("Error. " + str(e))

#process table
def process_table():
    try:
        pass
    except Exception as e:
        logging.error("Error. " + str(e))

#process document
def process_document(root, document):
    try:
        for export_element in document.export_elements:
            type_id = export_element.type.value

            if (type_id==0):
                process_row(root,export_element)
            elif (type_id==1):
                pass

        pass
    except Exception as e:
        logging.error("Error. " + str(e))