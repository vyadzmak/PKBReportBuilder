import models.tree_models.xml_tree_leaf as xml_leaf
#class XML Tree for navigate in xml data
class XmlTree():
    #constructor
    def __init__(self):
        try:
            self.leafs = []
            pass
        except Exception as e:
            pass

    #add leaf to tree
    def add_leaf(self,current_block, search_name,extract_data=False, extract_fields =None, result_array=True):
        try:
            leaf = xml_leaf.XmlLeaf(current_block, search_name,extract_data, extract_fields,result_array)
            self.leafs.append(leaf)
            return leaf
            pass
        except Exception as e:
            pass