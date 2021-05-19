import xlrd as Excel 
import matplotlib.pyplot as Graph
from tkinter import filedialog as Dialog
Path = Dialog.askopenfilename()
WorkBook = Excel.open_workbook(Path)
Sheet = WorkBook.sheet_by_index(0)
def Evaluate(Number):
    try:
        Number = int(Number)
        if Number < 0:
            print("Enter a Positive Number")
            exit()
        else:
            return Number
    except:
        print("Enter a Number")
        exit()
Title = Sheet.cell_value(0, 0)
XAxisTitle = Sheet.cell_value(1, 0)
YAxisTitle = Sheet.cell_value(2, 0)
Bars = []
BarTimes = 0
Production = []
Labels = []
while BarTimes != Sheet.nrows-4:
    BarTimes+=1
    Bars.append(BarTimes)
    Labels.append(Sheet.cell_value(BarTimes+3, 0))
    Production.append(Sheet.cell_value(BarTimes+3, 1))
FontHeader = {'family':'Segoe UI', 'size':20}
FontAxis = {'family':'Segoe UI', 'size':15}
Graph.figure(frameon=False).canvas.toolbar.pack_forget()
Graph.bar(Bars, Production, tick_label = Labels, width = 0.5, color = ['#EF4D4D', '#42CCFF', '#42B983', '#FAE786'])
Graph.title(Title, **FontHeader)
Graph.xlabel(XAxisTitle, **FontAxis)
Graph.ylabel(YAxisTitle, **FontAxis)
Graph.show()