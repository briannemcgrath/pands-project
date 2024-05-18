#analysis.py
#Analysis of Fisher's Iris Data Set
#Author: Brianne McGrath 

#Importing Necessary Libararies
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#Load the Iris dataset
df = pd.read_csv('iris.data')

#Reviewing the first few rows of the Dataset
df.head()

#Spot checking a random sample of the Dataset
df.sample(5)

#Displaying information about the Dataset
df.info()

#Showing summary statistics of the Dataset
df.describe() 

#Checking for missing values in the Dataset
df.isnull().sum()

#Counting the number of flowers in each species
df['Species'].value_counts()

#Counting the number of flowers in each species
flowers_count_by_species = df['Species'].value_counts()

#Defining colours for each species
colours =['lightblue', 'mediumaquamarine', 'pink']

#Creating a bar chart to visualise the count of flowers by species
plt.figure(figsize=(6,4))
plt.bar(flowers_count_by_species.index, flowers_count_by_species.values, color=colours)
plt.title('Count of Flowers by Species')
plt.xlabel('Species')
plt.ylabel('Count of Flowers')
plt.xticks(rotation=45)
plt.show()

#Summary of Each Variable - Single Text File: 

#Calculating summary statistics for each variable
summary = df.describe()

#Format the summary information
summary_text = summary.to_string()

#Saving summary statistics to a text file
with open("variable_summary.txt", "w") as file:
    file.write(summary_text)
print("Summary of variables written to 'variable_summary.txt' file.")

# Defining the output folder for histograms
output_folder = 'histograms'

#Function to save historgrams of each variable
def save_histograms(df, output_folder):
    # Defining colours for each Histogram
    colours = ['mediumaquamarine', 'pink', 'lightblue', 'mediumorchid']

    # Loop through each column and color
    for column, color in zip(df.columns, colours):
        # Create a histogram for the variable and save it as a PNG file
        df[column].plot(kind='hist', bins=10, color=color)
        plt.title(f'Histograms of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.grid(True) # Show grid
        plt.savefig(f'{output_folder}/{column}_histogram.png')
        plt.close()
    print("Histograms of variables output to 'histograms' folder.")

# Call the function to save histograms
save_histograms(df, output_folder)

#Scatter Plot for Each Variable

for column in df.columns[:-1]: #Species Column Excluded
    plt.figure(figsize=(8,6))
    sns.scatterplot(data=df, x=column, y='Species', hue='Species', palette='pastel')
    plt.title(f"Scatterplot of {column} for each Species")
    plt.xlabel(column)
    plt.ylabel("Species")
    plt.grid() 
    plt.show()

    #Creating a Pairplot
sns.pairplot(df, hue='Species', palette='pastel')
plt.show()

# Boxplot for each variable
plt.figure(figsize=(12, 6))

#Defining Colours 
colours=['mediumaquamarine', 'lightblue', 'pink', 'navajowhite'] 
for i, column in enumerate(df.columns[:-1]):  # Exclude the Species column
    plt.subplot(2, 2, i + 1)
    sns.boxplot(x='Species', y=column, data=df, color=colours[i % len(colours)])
    plt.title(f'Boxplot of {column} for each species')
plt.tight_layout()
plt.show()

#Calculate Pearson correlation coefficient for Iris Setosa
setosa_correlation = df[df['Species'] == 'Iris-setosa']['PetalWidthCm'].corr(df[df['Species'] == 'Iris-setosa']['PetalLengthCm'])

#Calculate Pearson correlation coefficient for Iris Versicolor
versicolor_correlation = df[df['Species'] == 'Iris-versicolor']['PetalWidthCm'].corr(df[df['Species'] == 'Iris-versicolor']['PetalLengthCm'])

#Calculate Pearson correlation coefficient for Iris Virginica
viriginica_correlation = df[df['Species'] == 'Iris-virginica']['PetalWidthCm'].corr(df[df['Species'] == 'Iris-virginica']['PetalLengthCm'])


#Print the correlation coefficients for Petal Width vs Petal Length
print("Pearson correlation coefficient for Petal Width vs Petal Length - Iris Setosa:", setosa_correlation)
print("Pearson correlation coefficient for Petal Width vs Petal Length - Iris Versicolor:", versicolor_correlation)
print("Pearson correlation coefficient for Petal Width vs Petal Length - Iris Virginica:", viriginica_correlation)

# lmplot seperated by Species

#Scatter Plots 

sns.lmplot(x='PetalLengthCm', y='PetalWidthCm', data=df, hue='Species', palette='pastel')
plt.title('Petal Width vs Petal Length')
plt.xlabel('Petal Length (CM)')
plt.ylabel('Petal Width (CM)')
plt.grid()
plt.show()