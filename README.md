# Alergy-detector

This aplication helps people, especialy parents to recognize what type of food products they eat every day alergize them or their children. Project raise becouse my own experience and becouse difficulties during feeding my doughters.

## Technology and tools used in the project: 

*Python 3.9
*pip 22.01
*Django 3.2.11
*PostgresSQL 14.1
*PgAdmin
*operation system  - Windows 10
* tool: Visual Studio Code

## Setup

To run this project, install it loccaly with following instruction:


- clone this repository: gh repo clone KamilaWZ/alergy-detector
- install Python
- install PostgresSQL
- create your main direction - mkdir alergydetector
- cd alergydetector
- create virtualenviroment in alergydetector direction with command: python -m venv myvenv
- activate virtual enviroment with command: \myvenv\Scripts\activate
- stay in alergydetector direction
- be sure you have installed actual pip package. You may use python -m pip install --upgrade pip
- with using your code editor create file named requirements.txt in alergydetector direction. In this file save the text: Django~=3.2.10
- run pip install -r requirements.txt command to install Django
- stay in alergydetector direction. In your command line run django-admin.exe startproject alergydetector .    Be sure You have white space before point. 
- create first table in date base in direction alergydetecor with command python manage.py migrate 
- run server with command python manage.py runserver 

 
## Features

You can save each meal and their details - the products that have been used.
You need to save the date and exactly hour of eating the meal.
You can make your observations by saving changes on your skin, its irritation, itching, runny nose or sneezing. 
Alergy detector automaticly shall calculate after minimum 3 days of observation (72 hours), what product may allergize you.
Remember, that using Allergy-ddetector is not real medical diagnosis. It shall only help you to cach what meal may couse your alergy problems and what you may shall eliminate for some time from ypur diet. 
If you need a professional diagnosis, contact your primary contact doctor or allergist.


## Project Status

Alergy detector is now in progress. 


 

