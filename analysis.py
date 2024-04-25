#analysis.py
#Analysis of Fisher's Iris Data Set
#Author: Brianne McGrath 

#Importing Necessary Libararies
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#Loading Dataset
df = pd.read_csv('iris.data')

#Reviewing Dataset
df.head()

df.describe() 

#Summary of Each Variable: 

#Calculating summary statistics for each variable
summary = df.describe()

#Format the summary information
summary_text = summary.to_string()

#Write the summary to a text file
with open("variable_summary.txt", "w") as file:
    file.write(summary_text)
print("Summary of variables written to 'variable_summary.txt' file.")

#Histogram Trial Pt 2: 

##SUCCESS!! - Add colours to match rest of project at a later date :) 

#Defining the output folder for histograms
output_folder = 'histograms'

def save_histograms(df, output_folder):
    #Loop through each column in the dataset
    for column in df.columns: 
        #Create a histogram for the varibale and save it is a PNG file
        df[column].plot(kind='hist', bins=10)
        plt.title(f'Histograms of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.savefig(f'{output_folder}/{column}_histogram.png')
        plt.close()


#Scatter Plots 

sns.scatterplot(x='SepalLengthCm', y='SepalWidthCm', data=df, color='mediumaquamarine')
plt.title('Sepal Width vs Sepal Length')
plt.xlabel('Sepal Length (CM)')
plt.ylabel('Sepal Width (CM)')
plt.grid()
plt.show()
        

#Adding Regression Line

sns.regplot(x='SepalLengthCm', y='SepalWidthCm', data=df, color='mediumaquamarine')
plt.title('Septal Width vs Sepal Length')
plt.xlabel('Sepal Length (CM)')
plt.ylabel('Sepal Width (CM)')
plt.grid()
plt.show()

# lmplot seperated by Species

sns.lmplot(x='SepalLengthCm', y='SepalWidthCm', data=df, hue='Species', palette='pastel')
plt.title('Septal Width vs Sepal Length')
plt.xlabel('Sepal Length (CM)')
plt.ylabel('Sepal Width (CM)')
plt.grid()
plt.show()

#Scatter Plots 

sns.scatterplot(x='PetalLengthCm', y='PetalWidthCm', data=df, color='powderblue')
plt.title('Petal Width vs Petal Length')
plt.xlabel('Petal Length (CM)')
plt.ylabel('Petal Width (CM)')
plt.grid()
plt.show()

# Adding Regression Line

sns.regplot(x='PetalLengthCm', y='PetalWidthCm', data=df, color='powderblue')
plt.title('Petal Width vs Petal Length')
plt.xlabel('Petal Length (CM)')
plt.ylabel('Petal Width (CM)')
plt.grid()
plt.show()

# lmplot seperated by Species

#Scatter Plots 

sns.lmplot(x='PetalLengthCm', y='PetalWidthCm', data=df, hue='Species', palette='pastel')
plt.title('Petal Width vs Petal Length')
plt.xlabel('Petal Length (CM)')
plt.ylabel('Petal Width (CM)')
plt.grid()
plt.show()