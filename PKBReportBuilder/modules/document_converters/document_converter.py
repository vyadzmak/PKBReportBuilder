import logging
import models.export_models.sheet_models as sheet_models
import models.export_models.export_document_report_model as export_document_report_model


# set zero row
def set_zero_row(document, sheet_id, widths):
    try:

        id = 1
        for width in widths:
            json = export_document_report_model.ExportDocumentReportCellContent("", width=width)
            cell = export_document_report_model.ExportDocumentReportCell(sheet_id, 0, id, json)
            document.cells.append(cell)
            id += 1
        pass

    except Exception as e:
        logging.error("Error. " + str(e))


# get max width column
def get_max_width(export_document):
    try:
        columns = []

        rows = []

        for element in export_document.export_elements:

            if (element.type.value == 0):
                rows.append(element.row)
            else:
                rows.append(element.table.header_row)
                for r in element.table.rows:
                    rows.append(r)
        for r in rows:
            id = 0
            for c in r.cells:
                l = len(str(c.value))
                if (l > 0):
                    if (len(columns) < id + 1):
                        columns.append(l)
                    else:
                        if (columns[id] < l):
                            columns[id] = l

                id += 1

        widths = []
        for c in columns:
            w = c * 8
            if (w > 320):
                w = 320
            widths.append(w)

        return widths
        pass
    except Exception as e:
        logging.error("Error. " + str(e))


# init single row
def init_row(document, row, row_index, show_grid):
    try:
        id =1
        for cell in row.cells:
            # content_type_id = cell.content_type.value
            style = cell.style

            back_color = style.bgc
            font_color = style.color
            font_family = style.ff
            font_style = style.fs
            font_size = style.fz
            text_align = style.ta

            font_weight = "normal"
            if (font_style == "bold"):
                font_weight = "bold"
                font_style = "normal"

            if (font_style == "bolditalic"):
                font_weight = "bold"
                font_style = "italic"

            if (font_style == "italic"):
                font_weight = "normal"
                font_style = "italic"

            fm = ""
            # if (
            #                         content_type_id == 4 or content_type_id == 6 or content_type_id == 7 or content_type_id == 9 or content_type_id == 11 or content_type_id == 12):
            #     fm = "money||2|none"


            cell_content = export_document_report_model.ExportDocumentReportCellContent(
                data=cell.value,
                bgc=back_color,
                color=font_color,
                ta=text_align,
                fz=font_size,
                ff=font_family,
                fw=font_weight,
                fs=font_style,
                show_grid=show_grid,
                fm=fm,
                contains_data=True

            )

            report_cell = export_document_report_model.ExportDocumentReportCell(1, row_index, id, cell_content)
            document.cells.append(report_cell)
            id += 1
            pass
        pass
    except Exception as e:
        logging.error("Error. " + str(e))


# init rows
def init_rows(export_document, document):
    try:
        rows = []

        for element in export_document.export_elements:
            if (element.type.value == 0):
                rows.append(element.row)
            else:
                rows.append(element.table.header_row)
                for r in element.table.rows:
                    rows.append(r)

        row_index = 1
        for row in rows:
            show_grid = True
            init_row(document, row, row_index, show_grid)
            row_index += 1
    except Exception as e:
        logging.error("Error. " + str(e))


# init document cells
def init_document_cells(export_document, document):
    try:

        width_columns = get_max_width(export_document)
        set_zero_row(document, 1, width_columns)
        init_rows(export_document, document)
    except Exception as e:
        logging.error("Error. " + str(e))


# convert document to sheet format
def convert_document_to_sheet_format(export_document):
    try:
        document_report_model = export_document_report_model.ExportDocumentReportModel("Отчет ПКБ")
        id = 1
        sheets = ["Детализация отчета ПКБ"]

        for sheet in sheets:
            document_report_model.add_sheet(id, sheet)
            id += 1

        init_document_cells(export_document, document_report_model)

        return document_report_model.toJSON()
        pass
    except Exception as e:
        logging.error("Error. " + str(e))
