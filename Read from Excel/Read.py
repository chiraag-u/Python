import xlrd as Excel 
from tkinter import filedialog as fd
Path = fd.askopenfilename()
WorkBook = Excel.open_workbook(Path)
Sheet = WorkBook.sheet_by_index(0)
Times = 0
print("\n\n")
while Times != Sheet.nrows:
    Times+=1
    print(Sheet.cell_value(Times-1, 0))