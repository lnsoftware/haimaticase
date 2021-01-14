import xlrd,xlwt
from openpyxl import workbook


def writeExcel():
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet("test1")
    for i in range(10):
        for j in range(5):
            worksheet.write(i,j,"xwd傻狗")
    workbook.save('test1.xlsx')


if __name__ == '__main__':
    writeExcel();
    print ('写入成功')