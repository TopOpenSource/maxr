import pandas as pd
import math

from utils.ExcelUtil import ExcelUtil


class CSV2Excel:
    def __init__(self, csv_path):
        self.csv_path = csv_path

        pass

    def readCSV(self):
        excel_util = ExcelUtil()

        data = pd.read_table(self.csv_path, sep=",")
        # 获取去重后的name,并循环
        name_data = data.drop_duplicates(subset='name')
        for name in name_data.iloc[:, 0]:
            excel_util.create_sheet(name)
            row_index = 2
            # header
            excel_util.insert_data(name, 1, 1, "Structure Name")
            excel_util.insert_data(name, 1, 2, "Dose")
            excel_util.insert_data(name, 1, 3, "Volume")

            # 步长
            step = 100
            # 当前区间
            min_dose = 0
            # 最大值 并取 向上取整  7140 -> 7200
            max_dose = data.loc[(data['name'] == name)]['dose'].max()
            max_dose = math.ceil(max_dose / 100) * 100
            # 循环并设置步长为100
            for stepDose in range(min_dose, max_dose, step):
                rows = data.loc[(data['name'] == name) & (data['dose'] >= stepDose) & (data['dose'] < (stepDose + 100))]
                # 如果有符合条件的 取第一行
                if len(rows) > 0:
                    excel_util.insert_data(name, row_index, 1, name)
                    excel_util.insert_data(name, row_index, 2, rows.iloc[0]['dose'])
                    excel_util.insert_data(name, row_index, 3, rows.iloc[0]['volume'])
                else:
                    excel_util.insert_data(name, row_index, 1, name)
                    excel_util.insert_data(name, row_index, 2, stepDose)
                    excel_util.insert_data(name, row_index, 3, 100)
                row_index = row_index + 1
        excel_util.save("D:/b.xlsx")


csv2Excel = CSV2Excel("D:/a.csv")
csv2Excel.readCSV()
