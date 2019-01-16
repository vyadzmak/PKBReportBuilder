import models.tree_models.xml_tree_model as xml_tree
import models.tree_models.xml_tree_leaf as xml_leaf

#add tree leaf
def add_tree_leaf(tree,current_block,search_name,extract_data=False, extract_fields =None, result_array=True):
    try:
        return tree.add_leaf(current_block, search_name,extract_data, extract_fields, result_array)

        pass
    except Exception as e:
        pass

def add_public_sources():

    pass

def add_data_result_root(tree,current_root):
    try:
        result_leaf = add_tree_leaf(tree,current_root,'Result',False,None,False)
        root_data_leaf = add_tree_leaf(tree,result_leaf,'Root',False,None,False)

        pass
    except Exception as e:
        pass

#build navigate xml tree
def build_xml_tree(root):
    try:
        tree = xml_tree.XmlTree()
        add_data_result_root(tree,root)

        return tree
    except Exception as e:
        pass