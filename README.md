# Exploratory data analysis - Customter loans in finance

## Purpose/Aim of project

## Installation
This project is coded in python. The following modules were required to be installed:
*PyYAML - to read yaml files
*Pandas
*sqlalchemy
*psycopg2

## Structure of Project
The first part of the project was to extract the loan payment data from a cloud database.

The second part of the project involves reviewing the data to identify any issues such as missing or incorrectly formatted data.
There are 43 columns which include 20 float, 8 integer and 15 object data types. Upon basic inspection, we can leave the float and integer data types unchanged. We then inspect the 15 coloumns with object data types as this can contain a mix of data types. Among the 15 columns containing object data types, I concluded that they can be converted into either a category or datetime64 datatype.

After correctly formatting the data, we resolve the missing data but either removing the whole column, removing row of the missing value or imputating the data using mean, median or average. Based on the data, I decided to drop all columns where the percentage of null values was above 50%. Imputate the data where the column had less 10% but greater than 1% null values. And remove the rows of data in which columns had less than 1% null values.
