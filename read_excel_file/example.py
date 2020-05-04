import xlrd

wb =xlrd.open_workbook("path to excel file")
sheet = wb.sheet_by_index("0")
sheet.cell_value(0,0)
print(sheet.nrows)
print(sheet.ncols)
