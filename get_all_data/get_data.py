import pandas 
import numpy 


DAYS = range(29)
SOILS = ["MIN", "COM", "UND"]
TREATMENTS = ["C", "T"]
REPLICATES = [1, 2, 3, 4]

INDEXS = (DAYS, SOILS, TREATMENTS, REPLICATES)
INDEXS_TITELS = ['day of incubation', 'soil', 'treatment', 'replicate']

TESTS = ["MBC", "MBN", "HWE-S", "ERG", "DOC", "NH4", "NO3", "EC","AS","TOC"]
TESTS_BIO = ["MBC", "MBN", "HWE-S", "ERG", "DOC"]
TESTS_PHYSCHEM = ["NH4", "NO3", "EC", "AS", "TOC"]
CALCULATED_PARAMS = ["ERG/MBC"]
num_columns = len(TESTS)
num_rows = len(DAYS) * len(SOILS) * len(TREATMENTS) * len(REPLICATES)

multindex = pandas.MultiIndex.from_product(INDEXS, names=INDEXS_TITELS)
combined_dataframe = pandas.DataFrame(index=multindex, columns=TESTS)
                                      

data_bio = "tests_data_bio.xlsx"
data_chem = "tests_data_chem.xlsx"

for test in TESTS_BIO:
    for day in DAYS:
        for soil in SOILS:
            for treatment in TREATMENTS:
                for replicate in REPLICATES:
                    input_dataframe = pandas.read_excel(data_bio, index_col=0, header=[0,1,2], sheet_name=test, na_values=["-", " "])
                    if day in input_dataframe.index:
                        combined_dataframe.xs((day, soil, treatment, replicate)).loc[test] = input_dataframe.loc[day,(soil, treatment, replicate)]
                    else:
                        continue


for test in TESTS_PHYSCHEM:
    for day in DAYS:
        for soil in SOILS:
            for treatment in TREATMENTS:
                for replicate in REPLICATES:
                    input_dataframe = pandas.read_excel(data_chem, index_col=0, header=[0,1,2], sheet_name=test, na_values=["-", " "])
                    if day in input_dataframe.index:
                        combined_dataframe.xs((day, soil, treatment, replicate)).loc[test] = input_dataframe.loc[day,(soil, treatment, replicate)]
                    else:
                        continue
#mbc_data = pandas.read_excel(data_bio, index_col=0, header=[0,1,2], sheet_name="MBC", na_values=["-", " "])
#erg_data = pandas.read_excel(data_bio, index_col=0, header=[0,1,2], sheet_name="ERG", na_values=["-", " "])
#combined_dataframe['ERG/MBC'] = erg_data / mbc_data.loc[[0, 7, 14, 21, 28],:]                   
#writer = pandas.ExcelWriter("results_fulltag.xlsx")
combined_dataframe.to_excel(excel_writer=writer,merge_cells=False, na_rep='ND')
   
                 