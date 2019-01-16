class Sheet():
    def __init__(self, id, name):
        self.id = id
        self.name = name

class CellJson():

    def __init__(self,data,bgc="#ffffff",color="#000000",ta="left",fz="10",fm="",fw="normal",fs="normal",u="",ff="arial",width=50,row=-1):
        self.width = width
        self.data =data
        self.bgc = bgc
        self.color = color
        self.ta = ta
        self.fz = fz
        self.fm = fm
        self.fw = fw
        self.fs = fs
        self.u = u
        self.ff = ff
        if (row>0):
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
        pass

class Cell():
    def __init__(self,sheet,row,col,cellJson):
        self.sheet = sheet
        self.row = row
        self.col = col
        self.json = cellJson
        pass
