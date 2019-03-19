# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 07:56:12 2018

@author: everybody
"""

import pandas as pd
import numpy as np


data = np.random.randint(60, 100, 96).reshape(24, 4)

index_labels = ["soil", "treatment"]
levels = (["Gezer", "Naan", "Matzlih"], ["tipul"]*4+["bikoret"]*4)
index = pd.MultiIndex.from_product(levels, names=index_labels)
days = ["day1", "day2", "day3", "day4"]

df = pd.DataFrame(data,index,columns=days)
statistics = df.groupby(level=index_labels).agg(
                                                ['mean', 'sem']
                                            ).sort_index(
                                                    level=index_labels,
                                                    ascending=[True,False] 
                                                )
means = statistics.xs("mean", axis=1, level=1, drop_level=True)
diff_of_means = means.diff(-1)
diff_of_means_treatment = diff_of_means.xs("tipul", level="treatment")

print(df)
print(statistics)
print(diff_of_means_treatment)

writer = pd.ExcelWriter('test1.xlsx')
statistics.to_excel(writer,"statistics",startrow=3,startcol=3,merge_cells=True)
df.to_excel(writer,'data',startrow=3,startcol=3)
diff_of_means_treatment.to_excel(writer,"diff",startrow=3,startcol=3)

    
