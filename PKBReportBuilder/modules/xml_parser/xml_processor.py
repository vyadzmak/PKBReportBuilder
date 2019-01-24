import logging
import modules.xml_parser.xml_table_processor as xml_table_processor
import models.tree_models.xml_navigator as navigator
import models.export_models.export_styles as export_styles
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


def check_field(element,name):
    try:
        v = getattr(element,name)

        return v
        pass
    except Exception as e:
        return None


#add element to document
def add_element_to_document(document,style,values):
    try:

        t=0
        navigate_params = navigator.XmlNavigator('','','',style)
        document.add_export_element([0,'',navigate_params])

        last_element = document.export_elements[len(document.export_elements)-1]
        last_element.row.set_row_style(style.bgc,style.color,style.ta,style.fz,style.fm,style.fw,style.fs,style.u,style.ff)

        str_values =[]



        for value in values:
            element_value = check_field(value,'title')

            if (element_value==None):
                element_value = check_field(value,'value')


            str_values.append(element_value)

        last_element.row.init_value_cells(navigate_params, str_values)
        last_element.row.set_row_cells_style()

        t=0

        pass
    except Exception as e:
        pass

#process table
def process_table(document):
    try:


        for table in document.xml_document_tables:

            add_element_to_document(document,export_styles.table_header_style,table.columns)

            for row in table.rows:
                add_element_to_document(document, export_styles.table_rows_content_style, row.cells)



            pass



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

        xml_table_processor.process_table(root, document)
        process_table(document)
        pass
    except Exception as e:
        logging.error("Error. " + str(e))