import logging
import copy
#check if value is root element in
def check_roots(values, value):
    try:
        for _value in values:
            if (str(_value)!=str(value) and str(_value).startswith(value)):
                return True
    except Exception as e:
        logging.error("Error. " + str(e))
        return False

#get t contract roots
def get_to_roots(values):
    try:
        root_values = []

        for value in  values:
            if (check_roots(values,value)==True):
                root_values.append(value)



        return root_values
    except Exception as e:
        logging.error("Error. " + str(e))
        return values


#get to single contracts without roots
def get_to_single_contracts(b_values, roots):
    try:

        for root in roots:
            for i in range(0,len(b_values)):
                if (str(b_values[i][0]) == str(root) or str(b_values[i][0]).startswith(str(root))):
                    b_values[i][1] = True

        single_roots =[]
        for b_value in b_values:
            if (b_value[1]==False):
                single_roots.append(b_value[0])
            pass

        return single_roots
    except Exception as e:
        logging.error("Error. " + str(e))
        return []

#group data by aggreement number
def group_data_table(table):
    try:
        column_name = 'AgreementNumber'


        values = []

        first_row = table.rows[0]

        cell_index = 0
        for cell in first_row.cells:
            if (cell.column.name==column_name):

                break
            cell_index+=1


        for row in table.rows:
            values.append(row.cells[cell_index].value)


        values.sort()

        sort_rows = []

        for value in values:
            for row in table.rows:
                if (str(row.cells[cell_index].value)==str(value)):
                    sort_rows.append(row)
                    continue

        table.rows = sort_rows



        roots =get_to_roots(values)

        b_values = []

        for value in values:
            b_values.append([value,False])

        #check all child and root elements
        single_roots = get_to_single_contracts(b_values,roots)

        result_roots = roots+single_roots


        result_roots.sort()



        sort_table = copy.deepcopy(table)
        sort_table.rows = []
        for result_root in result_roots:
            for row in table.rows:

                cell_value =row.cells[cell_index].value

                if (str(cell_value)==str(result_root) or str(cell_value).startswith(str(result_root))):
                    if(str(cell_value)!=str(result_root)):
                        #hidden_columns_in_groups
                        for cell in row.cells:
                            for hidden_column in table.hidden_columns_in_groups:
                                if (hidden_column==cell.column.name):
                                    cell.value = ''

                    sort_table.rows.append(row)





        t=0


        table = copy.deepcopy(sort_table)

        pass
    except Exception as e:
        logging.error("Error. " + str(e))