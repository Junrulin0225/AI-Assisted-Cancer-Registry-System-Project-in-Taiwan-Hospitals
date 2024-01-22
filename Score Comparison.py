import pandas as pd
df_collegue = pd.read_excel('Score Comparison.xlsx', sheet_name= "Collegue's uteri score").round(2)
df_mine = pd.read_excel('Score Comparison.xlsx', sheet_name= "Jun-Ru's uteri score")


match = df_collegue.loc[:, ['precision','recall','F-measure']] == df_mine.loc[:, ['precision','recall','F-measure']]


df_collegue = df_collegue.rename(columns={
    'precision': 'precision_collegue',
    'recall': 'recall_collegue',
    'F-measure': 'F-measure_collegue'
})


df_mine = df_mine.rename (columns={
    'precision': 'precision_mine',
    'recall': 'recall_mine',
    'F-measure': 'F-measure_mine'
})


merge = pd.merge(df_collegue, df_mine , on =['code','column_name'], how = 'inner')
merge['match'] = match.all(1)
print(merge)
merge.to_excel('score compared.xlsx')
