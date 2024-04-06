#analysis.py
#Analysis of Fisher's Iris Data Set
#Author: Brianne McGrath 

#Importing Necessary Libararies
import pandas as pd 
import matplotlib.pyplot as plt

#Loading Dataset
df = pd.read_csv('iris.data')

#Summary of Each Variable: 
#Calculating summary statistics for each variable
summary = df.describe()

#Formtat the summary information
summary_text = summary.to_string()

#Write the summary to a text file
with open("variable_summary.txt", "w") as file:
    file.write(summary_text)
print("Summary of variables written to 'variable_summary.txt' file.")