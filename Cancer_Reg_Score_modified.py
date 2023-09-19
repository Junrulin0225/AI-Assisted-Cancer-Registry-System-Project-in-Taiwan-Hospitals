# 加入pandas套件
import pandas as pd
from sklearn.metrics import classification_report  # 全部指標的報告

# 建立column list並透過for loop跑出所有欄位
cancer_lst = ['uterus', 'prostate', 'breast', 'liver', 'oral', 'colon']
column_name_list = ['PRIMARY_SITE', 'LATERALITY', 'HISTOLOGY', 'BEHAVIOR', 'DIAGNOSIS_CONFIRMATION', 'FIRST_PATHOLOGY_DATE', 'NODE_EXAMINED', 'NODE_POSITIVE', 'DIAG_STAGE_SUR_DATE', 'DIAG_STAGE_SUR',\
        'PATH_T', 'PATH_N', 'PATH_M', 'PATH_STAGE', 'PATH_STAGE_DESC', 'TNM_EDITION', 'FIRST_OP_DATE', 'SURGERY_DATE', 'SURGERY_TYPE', 'SURGICAL_MARGIN', 'LN_SURGERY_SCOPE',\
        'CHEMO', 'HT', 'IMMUNO', 'TT_OTHER_FACILITY']
# 想匯出的檔案名稱
writer = pd.ExcelWriter("all_cancer_scores.xlsx") 
for cancer in cancer_lst:
    print(cancer)
    #建一個空的dic，希望最後的表格呈現樣子是這樣
    dic = {
        'column_name': [],
        'precision': [],
        'recall': [],
        'F-measure': []
    }
    for column in column_name_list:
        # Predict檔建成pandas dataframe形式
        df = pd.read_excel('./output/{}/codings/{}.xlsx'.format(cancer, column), dtype={1:str, 2:str})
        # 把Dataframe中的NaN取代成0
        df = df.fillna('0')

        # Convert DataFrame to list using df.values.tolist()
        True_to_list = df[column+'_true'].tolist()
        Pred_to_list = df[column+'_pred'].tolist()
        # Pred_to_list = [str(pred) for pred in Pred_to_list]

        # 總和指標的報告
        cls_report = classification_report(True_to_list, Pred_to_list, output_dict=True, zero_division=0.0)

        # 把成績轉成Dataframe
        df = pd.DataFrame(cls_report).transpose().round(2)
        #print(column)
        #print(df)

        #把資料一欄一欄加入
        dic['column_name'].append(column)
        dic['precision'].append(df.loc['weighted avg', 'precision'])
        dic['recall'].append(df.loc['weighted avg', 'recall'])
        dic['F-measure'].append(df.loc['weighted avg', 'f1-score'])

        # 輸出成Excel每個欄位分數檔
        # df.to_excel(f'uteri_cancer_score_{column}.xlsx', index=True, sheet_name='20230707')
        # print('Congrats!uteri_cancer_score successfully exported to your location!')

    # 輸出成Excel所有欄位weighted score檔
    df_score = pd.DataFrame.from_dict(dic)
    df_score = df_score.set_index('column_name')
    df_score.to_excel(writer, sheet_name=f'{cancer}', index=True)
    print('Congrats!uteri_score successfully exported to your location!')
writer.close()