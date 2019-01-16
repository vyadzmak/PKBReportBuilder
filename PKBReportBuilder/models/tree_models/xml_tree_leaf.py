class XmlLeaf():
    #constructor
    def __init__(self,current_block, search_name,extract_data=False, extract_fields =None,result_array =True):

        self.current_block =current_block
        self.search_name = search_name
        self.extract_data = extract_data
        self.extract_fields = extract_fields
        self.result_array = result_array

        self.child_leafs = []

        pass

    #add child leaf
    def add_child_leaf(self):
        pass