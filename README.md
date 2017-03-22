# Python_HDI_Satelites


Purpose
-------

Investigate satelite data and HDI for different countries

Getting Started
-------


Run all the different QuestionX.py files to generate answer for the different questions given at https://github.com/stinaanita/python_data. 
Each QuestionX.py generates a plot which is saved in the root directory of the project. Some QuestionX.py also prints answers in the console  

Prerequisites
-------
This project requires the following modules to be installed/imported:
* `numpy`
* `matplotlib.pyplot` 
* `pandas`
* `collections`
* `csv`
# Solutions

Questions asked
-------
 * Q1:Which country has the highest HDI (Human Development Index) and which has the lowest?
 * Q2:Which country has raised its HDI the most, in the period 1990 to 2014?
 * Q3:Which country has the most satelites for military usage?
 * Q4:Which country has the lightest satelite and how much does it weight?
 * Q5:Compare the usage of satelites, between the 5 poorest countries and the 5 welthiest countries, according to the HDI dataset (see first dataset), plotting optional.

## 1.Which country has the highest HDI (Human Development Index) and which has the lowest?  
  
The answer is stored in a .txt file. Results are :  
The country with the highest HDI is Norway with 0.944  
The country with the lowest HDI is Niger with 0.348
![picture alt](http://i.imgur.com/Li7vUan.jpg)
## 2.Which country has raised its HDI the most, in the period 1990 to 2014?
![picture alt](http://i.imgur.com/VZTaiFS.png)  

 ## 3.Which country has the most satelites for military usage?  
 This data includes all of the countries with military satelites
 ![picture alt](http://i.imgur.com/3XeggBr.png)  
 ## 4.Which country has the lightest satelite and how much does it weight?
 The answer is stored in a .txt file. Results look like this:  
Empty DataFrame
Columns: [Official Name of Satellite, Country/Organization of UN Registry, Operator/Owner, Country of Operator/Owner, Users, Purpose,   Detailed Purpose, Class of Orbit, Type of Orbit, Longitude of Geosynchronous Orbit (Degrees), Perigee (Kilometers), Apogee   (Kilometers), Eccentricity, Inclination (Degrees), Period (Minutes), Launch Mass (Kilograms), Dry Mass (Kilograms), Power (Watts), Date   of Launch, Expected Lifetime (Years), Contractor, Country of Contractor, Launch Site, Launch Vehicle, COSPAR Number, NORAD Number]
Index: []

[0 rows x 26 columns] ['NUDT Phonesat' 'NR' 'National University of Defense Technology/CAMSAT'  
 'China' 'Military' 'Technology Demonstration' nan 'LEO' 'Sun-Synchronous'  
 0.0 516.0 536.0 0.00145 97.47 '95.24' '0' nan nan '9/19/2015' nan  
 'National University of Defense Technology' 'China'  
 'Taiyuan Launch Center' 'Long March 6' '2015-049B' 40900.0]   

Pico satellite	0.1 to 1  
Femto satellite	<0.1

Author
-------

David Shmilowitz
