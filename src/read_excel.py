import xlrd

#打开xls文件

book = xlrd.open_workbook("C:\\Users\\lenovo\\Desktop\\test.xls")

print ("表单数量", book.nsheets)
print ("表单名称", book.sheet_names())

sh = book.sheet_by_index(0)

print ("表单 %s 共 %d 行 %d 列" % (sh.name, sh.nrows, sh.ncols))

print ("表单第二行，第三列", sh.cell_value(1, 2))

for s in book.sheets():
    for r in range(s.nrows):
        print (s.row(r))
		
		
		
#end of file
#do nothing
