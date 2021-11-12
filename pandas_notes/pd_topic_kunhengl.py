 -*- coding: utf-8 -*-
# *Kunheng Li(kunhengl@umich.edu)*
# *Oct 20, 2021*

import pandas as pd

# ## Topics in Pandas

# The reason I choose this function is because last homework. Before the hint from teachers, I found some ways to transfrom one row to many rows. Therefore, I will introduce a function to deal with this type of data.

# First, let's see an example.

data = {
    "first name":["kevin","betty","tony"],
    "last name":["li","jin","zhang"],
    "courses":["EECS484, STATS507","STATS507, STATS500","EECS402,EECS482,EECS491"]   
}
df = pd.DataFrame(data)
df = df.set_index(["first name", "last name"])["courses"].str.split(",", expand=True)\
    .stack().reset_index(drop=True, level=-1).reset_index().rename(columns={0: "courses"})
print(df)

# This is the first method I want to introduce, stack() or unstack(), both are similar. 
# Unstack() and stack() in DataFrame are to make itself to a Series which has secondary index.
# Unstack() is to transform its index to secondary index and its column to primary index, however, 
# stack() is to transform its index to primary index and its column to secondary index.

# However, in Pandas 0.25 version, there is a new method in DataFrame called explode(). They have the result, let's see the example.

df["courses"] = df["courses"].str.split(",")
df = df.explode("courses")
print(df)

# We can see the result is the same.
