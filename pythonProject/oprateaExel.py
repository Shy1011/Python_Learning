import pandas as pd

# 创建示例数据框架
data = {
    'Product': ['A', 'B', 'C'],
    'Price': [25.5, 30.2, 15.8],
    'Quantity': [10, 8, 4]
}

df = pd.DataFrame(data)

# 将数据框架写入 Excel 文件
df.to_excel('output_data.xlsx', index=False)
