import xlrd
from  framework.logger import Logger
import os


logger=Logger(logger="Until").getlog()

class Until(object):
    @classmethod
    def read_excal(self,excal_path,sheetNum="Sheet1"):
        workbook=xlrd.open_workbook(excal_path)
        sheet=workbook.sheet_by_name(sheetNum)
        #第一行作为key
        keys=sheet.row_values(0)
        #获取总行
        rowNum=sheet.nrows
        #获取总列
        cloNum=sheet.ncols

        if rowNum<=1:
            logger.error("excel表中的行数少于1")
        else:
            list=[]
            for i in range(1,rowNum):
                sheet_data={ }
                values=sheet.row_values(i)
                for j in range (cloNum):
                    sheet_data[keys[j]]=values[j]
                list.append(sheet_data)
        return list
if __name__=="__main__":
    data_path = os.path.dirname(os.path.abspath('.')) + '/data/data.xlsx'
    print(Until.read_excal(data_path ,"Sheet1"))


