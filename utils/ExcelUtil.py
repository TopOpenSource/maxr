from openpyxl import Workbook


class ExcelUtil:
    def __init__(self):
        self.wb = Workbook()

    def create_sheet(self, sheet_name):
        self.wb.create_sheet(sheet_name)

    def insert_data(self, sheet_name, row, col, volumn):
        sheet = self.wb[sheet_name]
        sheet.cell(row=row, column=col).value = volumn

    def save(self, path):
        self.wb.save(path)
