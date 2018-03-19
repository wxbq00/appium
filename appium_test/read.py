# f=open('../auto/a.txt','w')
# data='test'
# f.write(data)
# f.close()
import xdrlib,sys
import xlrd
def open_excel(file='a.xlsx'):
    try:
        data=xlrd.open_workbook(file)
        return  data
    except Exception as e:
        print(str(e))
def excel_byIndex(file='a.xlsx',colnameIndex=0,index=0):#表头行的索引，表的索引
    data=open_excel(file)
    table=data.sheets()[index]
    nrows=table.nrows#行数
    ncols=table.ncols
    colnames=table.row_values(colnameIndex)#某一行数据
    list=[]
    for rownum in range(1,nrows):
        row=table.row_values(rownum)
        if row:
            app={}
            for i in range(len(colnames)):
                app[colnames[i]]=row[i]
            list.append(app)
    return list
def main():
    tables=excel_byIndex()
    for row in tables:
        print(row)
if __name__ == '__main__':
    main()