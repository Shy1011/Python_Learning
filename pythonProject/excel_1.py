# -*- coding: utf-8 -*-
import xlwings as xw
# wb = xw.Book()  # 这将创建一个新的工作簿
wb = xw.Book('FileName.xlsx')  # 连接到当前工作目录中的现有文件
# wb = xw.Book(r'C:\path\to\file.xlsx')  # 在Windows上：使用原始字符串来转义反斜杠

sht = wb.sheets['Sheet1']
sht.range('A1').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]] #写入数据
print(sht.range('A1').value)
print(sht.range('A1').expand().value) # 读取数据