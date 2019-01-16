import json
import uuid
class ExportDocumentReportCellContent():
    def __init__(self,projectId,data,bgc="#ffffff",color="#000000",ta="left",fz="10",fm="",fw="normal",fs="normal",u="",ff="arial",width=50,id=-1,analytical=False, month=-1,year=-1, document_type=-1, analytical_type=-1, period=-1,row=-1, show_grid=False, analysis_type=0,contains_data=False):
        self.projectId = projectId
        self.width = width
        self.data = data
        self.bgc = bgc
        self.color = color
        self.ta = ta
        self.fz = fz
        self.fm = fm
        self.fw = fw
        self.fs = fs
        self.u = u
        self.ff = ff
        self.onCellMouseMoveFn = "CELL_FOCUS_CALLBACK_FN"
        self.id = id
        self.analysis_type = analysis_type
        self.analytical = analytical
        self.month = month
        self.year = year
        self.document_type = document_type
        self.analytical_type = analytical_type
        self.period = str(period)
        self.uid = str(uuid.uuid4())[:8]
        if (show_grid and contains_data==False):
            self.bls = 'solid'
            self.brs = 'solid'
            self.bts = 'solid'
            self.bbs = 'solid'

            self.blc = '#7f7f7f'
            self.brc = '#7f7f7f'
            self.btc = '#7f7f7f'
            self.bbc = '#7f7f7f'

            self.blt = 'solid'
            self.brt = 'solid'
            self.btt = 'solid'
            self.bbt = 'solid'
        elif (show_grid and contains_data==True):
            self.bls = 'solid'
            self.brs = 'solid'
            self.bts = 'solid'
            self.bbs = 'solid'

            self.bgc = '#FFE996'

            self.blc = '#7f7f7f'
            self.brc = '#7f7f7f'
            self.btc = '#7f7f7f'
            self.bbc = '#7f7f7f'

            self.blt = 'double'
            self.brt = 'double'
            self.btt = 'double'
            self.bbt = 'double'


        pass


class ExportDocumentReportCell():
    def __init__(self,sheet,row,col,cellJson):
        self.sheet = sheet
        self.row = row
        self.col = col
        self.json = cellJson
        pass

class ExportDocumentGroup():
    def __init__(self,level,span):
        self.level = level
        self.span = span

    def toJSON(self):
            return json.dumps(self, default=lambda o: o.__dict__,
                              sort_keys=True, indent=4)

class ExportDocumentReportFloatings():
    def __init__(self,sheet,name,ftype,json):
        self.sheet = sheet
        self.name = name
        self.ftype = ftype
        self.json = json
        pass

class ExportDocumentReportSheet():
    def __init__(self,id, name):
        self.id =id
        self.name = name
        pass


class ExportDocumentReportModel():
    def __init__(self, fileName):
        self.fileName = fileName
        self.sheets = []
        self.floatings =[]
        self.cells = []
        pass

    #start from 1
    def add_sheet(self, id, name):
        self.sheets.append(ExportDocumentReportSheet(id,name))
        pass

    def add_cell(self):
        pass