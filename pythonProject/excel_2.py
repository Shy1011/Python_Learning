# -*- coding: utf-8 -*-
import xlwings as xw
wb = xw.Book('FileName.xlsx')  # 连接到当前工作目录中的现有文件
rng = wb.sheets[0].range('A1:D5')
print(rng)