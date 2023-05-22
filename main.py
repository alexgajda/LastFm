from datetime import datetime

from faker import Faker
import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import mysql.connector
from faker import Faker
import random as rand

#community_graph= nx.barabasi_albert_graph(20, 3)
#nx.draw(community_graph, with_labels=True)

mydb = mysql.connector.connect(
  host="localhost",
  user="alex",
  password="aek21",
  database="mysql"
)

mycursor = mydb.cursor()

# Create tables
# mycursor.execute('CREATE TABLE Users (user_id INTEGER PRIMARY KEY, username TEXT, age INTEGER)')
# mycursor.execute('CREATE TABLE Band0 (band_id INTEGER PRIMARY KEY, band_name TEXT, genre TEXT)')
# mycursor.execute('CREATE TABLE Records0(  record_id INTEGER PRIMARY KEY, record_name TEXT, band_id INTEGER, FOREIGN KEY (band_id) REFERENCES band0(band_id))')
#
# # Insert fake values in users table
# fake = Faker()
# for user_id in range(1, 21):
#   random_name = fake.name()
#   random_age = str(rand.randint(10, 65))
#
#
#   mycursor.execute("INSERT INTO People (user_id, username, age) VALUES (%s, %s, %s)", (user_id, random_name, random_age))
#   mydb.commit()
#
# INSERT band data
# band_data = [
#     (201, 'Coldplay', 'rock'),
#     (202, 'Paramore', 'rock'),
#     (203, 'Drake', 'hip-hop'),
#     (204, 'Future', 'hip-hop'),
#     (205, 'Nas', 'hip-hop'),
#     (206, 'Eminem', 'rap'),
#     (207, '2Pac', 'rap'),
#     (208, 'Foals', 'indie'),
#     (209, 'Radiohead', 'alternative'),
#     (210, 'Gorillaz', 'alternative')
# ]
#
# sql = "INSERT INTO band0 (band_id, band_name, genre) VALUES (%s, %s, %s)"
# mycursor.executemany(sql, band_data)
# mydb.commit()

# Fake records data
# records_data = [
#     (100, 'Ghost Stories', '201'),
#     (101, 'Everyday Life', '201'),
#     (102, 'Paramore', '202'),
#     (103, 'RIOT!', '202'),
#     (104, 'Views', '203'),
#     (105, 'FUTURE', '204'),
#     (106, 'HNDRXX', '204'),
#     (107, 'Illmatic', '205'),
#     (108, 'Recovery', '206'),
#     (109, 'The Eminem Show', '206'),
#     (110, 'Greatest Hits', '207'),
#     (111, 'All Eyez on Me', '207'),
#     (112, 'Holy Fire', '208'),
#     (113, 'OK Computer', '209'),
#     (114, 'Demon Days', '210'),
#     (115, 'Gorillaz', '210')
# ]
#
# sql = "INSERT INTO records0 (record_id, record_name, band_id) VALUES (%s, %s, %s)"
# mycursor.executemany(sql, records_data)
# mydb.commit()


# user records that people own
# mycursor.execute('''
#     CREATE TABLE UserRecords (
#         user_id INTEGER,
#         record_id INTEGER,
#         FOREIGN KEY (user_id) REFERENCES people(user_id),
#         FOREIGN KEY (record_id) REFERENCES Records0(record_id),
#         PRIMARY KEY (user_id, record_id)
#     )
# ''')


# user bands that people like
# mycursor.execute('''
#     CREATE TABLE UserBand (
#         user_id INTEGER,
#         band_id INTEGER,
#         FOREIGN KEY (user_id) REFERENCES people(user_id),
#         FOREIGN KEY (band_id) REFERENCES Band0(band_id),
#         PRIMARY KEY (user_id, band_id)
#     )
# ''')

# for user in range(1, 21):
#     how_many_bands_likes = rand.randint(1, 3)
#     how_many_records_has = rand.randint(1, 3)
#
#     random_bands = rand.sample(range(201, 211), how_many_bands_likes)
#
#     for band_id in random_bands:
#         mycursor.execute("INSERT INTO userband (user_id, band_id) VALUES (%s, %s)", (user, band_id))
#         mydb.commit()
#
#     random_records = rand.sample(range(100, 115), how_many_records_has)
#     for record_id in random_records:
#         mycursor.execute("INSERT INTO userrecords (user_id, record_id) VALUES (%s, %s)", (user, record_id))
#         mydb.commit()


