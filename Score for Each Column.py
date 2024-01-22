import pandas as pd
from sklearn.metrics import classification_report  
df_Predict = pd.read_excel('(Predict) Uteri Cancer.xlsx')
df_TRUE = pd.read_excel('(True) Uteri Cancer.xlsx')
#Replace null value into 0
Predict = df_Predict.fillna(0)
TRUE = df_TRUE

dic = {
    'column_name': [],
    'precision': [],
    'recall': [],
    'F-measure': []
}

column_name_list = [
    'PRIMARY_SITE', 'LATERALITY', 'HISTOLOGY', 'BEHAVIOR','DIAGNOSIS_CONFIRMATION', 'NODE_EXAMINED', 'NODE_POSITIVE', 'DIAG_STAGE_SUR', 'PATH_T', 'PATH_N', 'PATH_M', 'PATH_STAGE_DESC', 'FIRST_OP_DATE', 'SURGERY_DATE', 'SURGERY_TYPE', 'SURGICAL_MARGIN','LN_SURGERY_SCOPE' 
]
for column in column_name_list:
    # Convert DataFrame to list using df.values.tolist()
    Pred_to_list = Predict[column].tolist()
    True_to_list = TRUE[column + '_true'].tolist()



    cls_report = classification_report(True_to_list, Pred_to_list, output_dict=True, zero_division=0.0)
    # Conert the score into Dataframe
    df = pd.DataFrame(cls_report).transpose().round(2)
    #print(column)
    #print(df)

    
    dic['column_name'].append(column)
    dic['precision'].append(df.loc['weighted avg', 'precision'])
    dic['recall'].append(df.loc['weighted avg', 'recall'])
    dic['F-measure'].append(df.loc['weighted avg', 'f1-score'])

    
    # df.to_excel(f'uteri_cancer_score_{column}.xlsx', index=True, sheet_name='20230707')
    # print('Congrats!uteri_cancer_score successfully exported to your location!')


df_score = pd.DataFrame.from_dict(dic)
df_score = df_score.set_index('column_name')
print(df_score)
df_score.to_excel('uteri_score.xlsx', index=True, sheet_name='20230707')
print('Congrats!uteri_score successfully exported to your location!')
