import os
# import win32com.client
# import xlwt
from pymongo import MongoClient

# def Export2xls(cat = "purpose_txt", ofn = "actions_category.xlsx"):
#     cat = "actions_category"
#     ofn = "actions_category.xlsx"
#     if cat=="actions_category":
#         client = MongoClient()
#         client = MongoClient('localhost', 27017)
#         db = client['RKN']
#         col_edu = db.edu_records
#         posts = db.posts
#         acat_mas=[]
#         for post in col_edu.find():
#             try:
#                 post['rkn:record']['rkn:is_list']['rkn:is']
#                 actions_category=post['rkn:record']['rkn:is_list']['rkn:is']['rkn:actions_category']
#                 rkn_address=post['rkn:record']['rkn:address']
#                 rkn_name_full=post['rkn:record']['rkn:name_full']
#             except:
#                 actions_category=" "
#                 rkn_address=" "
#                 rkn_name_full=" "
#             if (len(actions_category))>3:
#                 tmas=[]
#                 # print(actions_category)
#                 # print(rkn_address)
#                 # print(rkn_name_full)
#                 tmas.append(actions_category)
#                 tmas.append(rkn_name_full)
#                 tmas.append(rkn_address)
#
#                 acat_mas.append(tmas)
#                 #print(actions_category)
#         path_1 = os.path.abspath(u'./'+ofn)
#         print(path_1)
#         #ex_file: str = path_1.replace('\\', '\\\\')
#         Excel = win32com.client.Dispatch("Excel.Application")
#         # if not (os.path.exists(path_1)):
#         #     workbook = xlwt.Workbook()
#         #     workbook.add_sheet('sheet1')
#         #     workbook.save(path_1)
#         wb = Excel.Workbooks.Open(path_1)
#         # sheet = wb.ActiveSheet
#         sheet = wb.Worksheets(u'исходные данные')
#         row_num = 2
#         for acat in acat_mas:
#             cow_num=1
#             for item in acat:
#                 sheet.Cells(row_num, cow_num).value = item
#                 cow_num += 1
#             row_num += 1
#         wb.Save()
#         wb.Close()
#         Excel.Quit()

def Export2mas():
    x = 1258
    y = 1 # Максимальное количество слов
    mmas = [["" for j in range(y)] for i in range(x)]
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client['RKN']
    col_edu = db.edu_records
    posts = db.posts
    acat_mas=[]
    for post in col_edu.find():
        try:
            post['rkn:record']['rkn:is_list']['rkn:is']
            actions_category=post['rkn:record']['rkn:is_list']['rkn:is']['rkn:actions_category']
        except:
            actions_category=" "
        if (len(actions_category))>3:
            tmas = []
            tmas.append(post["_id"])
            tmas.append(actions_category)
            tmas.append(post['rkn:record']["rkn:name_full"])
            acat_mas.append(tmas)
            #print(actions_category)

    return acat_mas

