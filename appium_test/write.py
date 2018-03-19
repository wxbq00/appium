from xlwt import Workbook
book=Workbook()
sheet1=book.add_sheet('sheet1')
book.add_sheet('sheet2')
sheet1.write(0,0,'lucas')
sheet1.write(0,1,'lucas2')
row1=sheet1.row(1)
row1.write(0,'dsjjd')
book.save('b.xls')