import WWS 

ML_dict,ML_DF = WWS.scrap("Machine Learning")
DS_dict,DS_DF = WWS.scrap("Data Science")
DA_dict,DA_DF = WWS.scrap("Data Analysis")
BI_dict,BI_DF = WWS.scrap("Business Intelligence")

DF= WWS.combine_data_frames([ML_DF,DS_DF,DA_DF,BI_DF])
DF.to_csv('Final_DATA_ALL.csv',index=False)
print("Data Saved")
