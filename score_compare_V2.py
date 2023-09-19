import pandas as pd
df_Amber = pd.read_excel('C:/Users/candy850225/Desktop/Amber_Candy_score_compare.xlsx', sheet_name= 'Amber_uteri').round(2)
df_Candy = pd.read_excel('C:/Users/candy850225/Desktop/Amber_Candy_score_compare.xlsx', sheet_name= 'Candy_uteri')


match = df_Amber.loc[:, ['precision','recall','F-measure']] == df_Candy.loc[:, ['precision','recall','F-measure']]


df_Amber = df_Amber.rename(columns={
    'precision': 'precision_Amber',
    'recall': 'recall_Amber',
    'F-measure': 'F-measure_Amber'
})


df_Candy = df_Candy.rename (columns={
    'precision': 'precision_Candy',
    'recall': 'recall_Candy',
    'F-measure': 'F-measure_Candy'
})


merge = pd.merge(df_Amber, df_Candy , on =['code','column_name'], how = 'inner')
merge['match'] = match.all(1)
print(merge)