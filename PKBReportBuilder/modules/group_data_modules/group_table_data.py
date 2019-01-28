import logging
import copy
import models.export_models.export_styles as export_styles
# check if value is root element in
def check_roots(values, value):
    try:
        if (value==''):
            return False
        for _value in values:
            if (str(_value) != str(value) and str(_value).startswith(value)):
                return True
    except Exception as e:
        logging.error("Error. " + str(e))
        return False

# get t contract roots
def get_to_roots(values):
    try:
        root_values = []
        for value in values:
            if (check_roots(values, value) == True):
                root_values.append(value)
        return root_values
    except Exception as e:
        logging.error("Error. " + str(e))
        return values

# get to single contracts without roots
def get_to_single_contracts(b_values, roots):
    try:
        for root in roots:
            for i in range(0, len(b_values)):
                if (str(b_values[i][0]) == str(root) or str(b_values[i][0]).startswith(str(root))):
                    b_values[i][1] = True

        single_roots = []
        for b_value in b_values:
            if (len(b_value)>1):
                if (b_value[1] == False):
                    if (b_value[0]!=''):
                        single_roots.append(b_value[0])
        return single_roots
    except Exception as e:
        logging.error("Error. " + str(e))
        return []

#sum chid element
def sum_child_element(rows, group_id, column_id):
    try:
        result = 0
        founded = False
        for row in rows:
            if (row.is_root==False and row.group_id==group_id):
                value = float(row.cells[column_id].value)
                result+=value
                founded = True

        if (founded==False):
            return None

        return round(result,2)
    except Exception as e:
        logging.error("Error. " + str(e))
        return 0


#calculate child elements
def calculate_root_elements(table):
    try:
        column_names = ['TotalAmount','OutstandingAmount', 'MonthlyInstalmentAmount']
        for column_name in column_names:


            for row in table.rows:
                if (row.is_root ==True):
                    column_index = -1
                    group_id = row.group_id
                    index =0

                    for cell in row.cells:
                        if (cell.column.name == column_name):
                            column_index=index
                            break
                        index+=1
                    if (column_index==-1):
                        continue
                    sum_rows = sum_child_element(table.rows,group_id,column_index)
                    if (sum_rows!=None):
                        row.cells[column_index].value = str(sum_rows)


        t=0
    except Exception as e:
        logging.error("Error. " + str(e))



# group data by aggreement number
def group_data_table(table):
    try:
        column_name = 'AgreementNumber'
        values = []
        first_row = table.rows[0]
        cell_index = 0
        for cell in first_row.cells:
            if (cell.column.name == column_name):
                break
            cell_index += 1
        for row in table.rows:
            if (row.cells[cell_index].value!=''):
                values.append(row.cells[cell_index].value)
        values.sort()
        sort_rows = []
        for value in values:
            for row in table.rows:
                if (str(row.cells[cell_index].value) == str(value)):

                    sort_rows.append(row)
                    continue

        table.rows = sort_rows
        roots = get_to_roots(values)
        b_values = []
        for value in values:
            b_values.append([value, False])

        # check all child and root elements
        single_roots = get_to_single_contracts(b_values, roots)
        result_roots = roots + single_roots
        result_roots.sort()
        sort_table = copy.deepcopy(table)
        sort_table.rows = []
        current_group_id = -1
        for result_root in result_roots:
            current_group_id += 1

            current_row_index = 0
            start_row_group_index = -1
            end_row_group_index = -1

            for row in table.rows:
                current_row_index+=1
                cell_value = row.cells[cell_index].value
                if (str(cell_value) == str(result_root) or str(cell_value).startswith(str(result_root))):
                    row.group_id = current_group_id

                    if (str(cell_value) != str(result_root)):
                        end_row_group_index = current_row_index
                        # hidden_columns_in_groups
                        for cell in row.cells:
                            for hidden_column in table.hidden_columns_in_groups:
                                if (hidden_column == cell.column.name):
                                    cell.value = ''
                    else:
                        start_row_group_index = current_row_index
                        end_row_group_index = current_row_index
                        row.is_root = True
                        # row.set_cells_styles(export_styles.table_rows_root_content_style)
                        row.group_id= current_group_id

                    sort_table.rows.append(row)
            if (start_row_group_index!=-1 and end_row_group_index!=-1):
                if (start_row_group_index!=end_row_group_index):
                    sort_table.group_rows.append([start_row_group_index,end_row_group_index])

        calculate_root_elements(sort_table)
        table = copy.deepcopy(sort_table)
        return table
    except Exception as e:
        logging.error("Error. " + str(e))
