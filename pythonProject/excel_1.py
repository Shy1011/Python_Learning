import xlwings as xw
app = xw.App(visible = True, add_book = False)
workbook = app.books.add()

workbook.save('example.xlsx')
workbook.close() # 关闭工作簿
app.quit() # 退出Excel程序