import pandas as  pd
import openpyxl

writer = pd.ExcelWriter("D://a.xlsx",engine='openpyxl')

pd_data=pd.DataFrame()

pd_data.to_excel(writer, "新sheet名1",index=False)
#writer.save()

pd_data2=pd.DataFrame()

pd_data2.to_excel(writer, "新sheet名2",index=False)

writer.save()