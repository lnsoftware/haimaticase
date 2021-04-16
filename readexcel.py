import xlrd,xlwt
from openpyxl import workbook


# def writeExcel():
#     workbook = xlwt.Workbook(encoding='utf-8')
#     worksheet = workbook.add_sheet("test1")
#     for i in range(10):
#         for j in range(5):
#             worksheet.write(i,j,"xwd傻狗")
#     workbook.save('test1.xlsx')

def readExcel():
    book = xlrd.open_workbook('test.xlsx')
    sheet = book.sheet_by_name('Sheet1')
    phone = sheet.cell_value(1,0)
    rightPwd = sheet.cell_value(1,1)
    errorPwd = sheet.cell_value(2,1)
    print(int(phone),int(rightPwd),int(errorPwd))
readExcel()

#  if __name__ == '__main__':
    # writeExcel();
    # print ('写入成功')