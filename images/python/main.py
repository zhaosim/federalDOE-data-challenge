#!/usr/bin/env python

import pandas as pd

import csv
import json
from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine("mysql://codetest:swordfish@database/codetest")
connection = engine.connect()

######
# load people.csv into database
try:
    with open('/data/people.csv', 'r') as file:
        df_people = pd.read_csv(file, encoding='utf-8')
    try:
        starttime = datetime.now()
        df_people.to_sql(name='Person', 
            con=engine, 
            if_exists='append',
            index=False, 
            chunksize=1000,
            dtype={
                'given_name': String,
                'family_name': String,
                'date_of_birth': DateTime,
                'place_of_birth': String
            })
        endtime = datetime.now()
        print("Person table loaded in " + str(endtime - starttime))
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
except (FileNotFoundError, PermissionError, OSError):
    print("Error opening file")

######
# load places.csv into database
try:
    with open('/data/places.csv', 'r') as file:
        df_places = pd.read_csv(file, encoding='utf-8')
    try:
        starttime = datetime.now()
        df_places.to_sql(name='Place', 
            con=engine, 
            if_exists='append',
            index=False, 
            chunksize=1000,
            dtype={
                'city': String,
                'county': String,
                'country': String
            })
        endtime = datetime.now()
        print("Place table loaded in " + str(endtime - starttime))
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
except (FileNotFoundError, PermissionError, OSError):
    print("Error opening file")

######
# query to summary_output json 
try:
    with open('/data/summary_output.json', 'w') as json_file:
        mysql_query = ('SELECT pl.country, COUNT(pe.person_id) '
                        'FROM Person pe '
                        'INNER JOIN Place pl ON pe.place_of_birth = pl.city '
                        'GROUP BY pl.country;'
                        )   
        try:                                
            rows = connection.execute(text(mysql_query))
            row_list = list(rows)

            rows = [{row[0]: row[1] for row in row_list}]
            
            json.dump(rows[0], json_file, separators=(',', ':'))
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
except (FileNotFoundError, PermissionError, OSError):
    print("Error opening file")
    

connection.close()
engine.dispose()