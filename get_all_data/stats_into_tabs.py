
import pandas
from scipy.stats import ttest_ind 


TESTS = ["MBC", "RESP", "HWE-S", "ERG", "DOC", "MBN", "NH4", "NO3", "EC","AS"]
input_file = "all_tests_compound.xlsx"

def multiple_dfs(df_list, sheets, file_name, spaces):
        writer = pandas.ExcelWriter(file_name,engine='xlsxwriter')   
        row = 0
        for dataframe in df_list:
            dataframe.to_excel(writer,sheet_name=sheets,startrow=row , startcol=0)   
            row = row + len(dataframe.index) + spaces + 1
        
    

for test in TESTS:
    dataframe = pandas.read_excel(input_file, index_col=0, header=[0,1,2],
                                  sheet_name=test,
                                  na_values=["-", " "]).rename_axis("days")
    dataframe.columns.rename(["soil","treatment","replicate"],
                             level=None, inplace=True)
    dataframe.columns.set_levels(["control","MRE"],level=1, inplace=True)
    
    # means
    groupby_soil_treatment = dataframe.groupby(level=[0,1], axis=1) # group 4 replicates from every soil-treatment pair 
    means = groupby_soil_treatment.mean() # means of 4 replicates
    treatment_means = means.xs("MRE",axis=1,level=1)
    
    # standard error of means
    stde_means = groupby_soil_treatment.sem() # stnd error of means
    stde_treatment_means = stde_means.xs("MRE",axis=1,level=1) # slicing out stde of control means
    
    # treatment means normalized to control 
    diff_of_means = means.diff(periods=1,axis=1) # substracting over columns index, from right to left
    treatment_effect =  diff_of_means.xs("MRE",axis=1,level=1)# slicing out from diff_of_means the unwanted results of control minus treatment
    
    #standard error of normalized means
    control_stde_sqrd = (stde_means**2).xs("control",axis=1,level=1) # control stnd error values squared
    MRE_stde_sqrd = (stde_means**2).xs("MRE", axis=1,level=1) # treatment stnd error values squared
    stde_effect = (control_stde_sqrd + MRE_stde_sqrd)**0.5 # stnd error of treatment effect
    
    # test sgnificance between soils inside sampling day
    inside_days_Ttest = {}
    
    for day in range(len(dataframe.index) - 1):
        data_MRE = dataframe.T.xs("MRE",level=1)
        
        COM_MIN = list(ttest_ind(data_MRE.xs("COM",level=0).iloc[:,day],
                                       data_MRE.xs("MIN",level=0).iloc[:,day],
                                       equal_var=False, nan_policy='omit')          
                        )
        COM_UND = list(ttest_ind(data_MRE.xs("COM",level=0).iloc[:,day],
                                       data_MRE.xs("UND",level=0).iloc[:,day],
                                       equal_var=False, nan_policy='omit')      
                        )
        MIN_UND = list(ttest_ind(data_MRE.xs("MIN",level=0).iloc[:,day],
                                       data_MRE.xs("UND",level=0).iloc[:,day],
                                       equal_var=False, nan_policy='omit')
                        )
        
        
        all_pairs = {"COM-MIN": COM_MIN[1],
                     "COM-UND": COM_UND[1],
                     "MIN-UND": MIN_UND[1]
                     }
        inside_days_Ttest[day] = all_pairs
        
    inday_Ttest = pandas.DataFrame.from_dict(inside_days_Ttest).T
    concated_means = pandas.concat({"means": means,'stde_means': stde_means}, axis=1)
    concated_effect =  pandas.concat(
                                      {"means normalized": treatment_effect,
                                      'stde of normalized means': stde_effect},
                                       axis=1
                                     )
    
        
    multiple_dfs([concated_means,concated_effect,inday_Ttest], test,
                 "all_stats.xlsx", 5
                 )    

            