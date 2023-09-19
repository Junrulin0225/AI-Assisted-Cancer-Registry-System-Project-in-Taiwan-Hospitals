#加入pandas套件
import pandas as pd
#cancer type_cancer.csv檔建成pandas dataframe形式
df = pd.read_excel('C:/Users/candy850225/Desktop/colon比對/cancer.xlsx')

#設index
df = df.set_index('ID')
#取出特定的column與row
# 目前不能做的核心欄位(new)
# # unavailable = [
#     'MCONF_DT','SDIAG_DT',
#     'AJCC_E','AJCC_D',
#     'OP_DT','OPDEF_DT','OPTYPE','MISURGERY',
#     'CH','HORM','IMMU','TARGET_H'
#     ]

#可做的核心欄位(new)
#  Cancer = df[
#     'CASITE','LATERAL','HIST','BEHAVIOR','GRADE_P','CONFIRM',
#     'PNI','LVI','NEXAM','NPOSIT','SDIAG','PT','PN','PM','PSTAGE','PDESCR',
#     'AJCC_E','AJCC_D','OPMARGS','SMARGIN_D','OPLNSCOPE'
#     ]

#可做的推薦欄位(new)
Cancer_op = [
     'DIAG_DT','GRADE_C','TSIZE','CT','CN','CM',
     'CSTAGE','CDESCR','RTB_DT','RTE_DT',
     'RTH','RTH_DOSE','RTH_NF','RTL','RTL_DOSE','RTL_NF'
     ]
column_date = df[['MCONF_DT','SDIAG_DT']].sort_values('ID')
column_date.to_excel('cancer_date_column.xlsx')

# op_value_count_list = []
# for i in Cancer_op:
#     op_value_count_list.append(df[i].value_counts())
# print(Cancer_op)
# print()
# print(i, op_value_count_list)
#print(df['TSIZE'].value_counts())

#2023Aug要做的欄位(核心+推薦)
# Cancer = df[['DIAG_DT','CASITE','LATERAL','HIST','BEHAVIOR','GRADE_C','GRADE_P','CONFIRM','TSIZE',
#     'PNI','LVI','NEXAM','NPOSIT','SDIAG','CT','CN','CM','CSTAGE','CDESCR','PT','PN','PM','PSTAGE','PDESCR',
#     'AJCC_E','AJCC_D','OPMARGS','SMARGIN_D','OPLNSCOPE','RTB_DT','RTE_DT',
#      'RTH','RTH_DOSE','RTH_NF','RTL','RTL_DOSE','RTL_NF','FIRST_OP_DATE']]
#column_date = column_date.iloc[:300,:]

#print(column_date)

#重新命名column名稱
# df_cancer_column_rename = df_cancer_column_row.rename(columns= {
#     'PRIMARY_SITE':'2.6', 'LATERALITY':'2.7', 'HISTOLOGY':'2.8', 'BEHAVIOR':'2.9', 'DIAGNOSIS_CONFIRMATION':'2.11','NODE_EXAMINED':'2.14','NODE_POSITIVE':'2.15',
#     'DIAG_STAGE_SUR':'3.2','PATH_T':'3.10','PATH_N':'3.11','PATH_M':'3.12', 'PATH_STAGE_DESC':'3.14', 
#     'FIRST_OP_DATE':'4.1.1', 'SURGERY_DATE':'4.1.2','SURGERY_TYPE':'4.1.4','SURGICAL_MARGIN':'4.1.5','LN_SURGERY_SCOPE':'4.1.7'})

# #重新命名index名稱
# df_cancer_column_rename.index.name = 'case number'


# ##只看特定編碼，未改
# #print(df_cancer_column_rename[df_cancer_column_rename['2.8']]=='8140')

#計算總共有幾個case
# print(df_cancer['PID_S'].count())

#輸出資料到excel
#Cancer.to_excel('new_CRC_TEMPLATE.xlsx', index=True)
#print('Congrats!CRC_answer successfully exported to your location!')
