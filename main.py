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
# mycursor.execute('CREATE TABLE Users (user_id INTEGER PRIMARY KEY, username TEXT, age INTEGER, location TEXT)')
# mycursor.execute('CREATE TABLE Band (band_id INTEGER PRIMARY KEY, band_name TEXT, genre TEXT)')
# mycursor.execute('CREATE TABLE Records(  record_id INTEGER PRIMARY KEY, record_name TEXT, release_date TEXT, band_id INTEGER, FOREIGN KEY (band_id) REFERENCES Band(band_id))')

# Insert fake values in users table
# fake = Faker()
# for user_id in range(1, 21):
#   random_name = fake.name()
#   random_age = str(rand.randint(10, 65))
#
#
#   mycursor.execute("INSERT INTO users (user_id, username, age) VALUES (%s, %s, %s)", (user_id, random_name, random_age))
#   mydb.commit()

# INSERT band data
# band_data = [
#     (1, 'Coldplay', 'rock'),
#     (2, 'Paramore', 'rock'),
#     (3, 'Drake', 'hip-hop'),
#     (4, 'Future', 'hip-hop'),
#     (5, 'JAY-Z', 'hip-hop'),
#     (6, 'Nas', 'hip-hop'),
#     (7, 'Eminem', 'rap'),
#     (8, '2Pac', 'rap'),
#     (9, 'Foals', 'indie'),
#     (10, 'Bastille', 'indie'),
#     (11, 'Radiohead', 'alternative'),
#     (12, 'Gorillaz', 'alternative'),
#     (13, 'Beck', 'alternative')
# ]
#
# sql = "INSERT INTO band (band_id, band_name, genre) VALUES (%s, %s, %s)"
# mycursor.executemany(sql, band_data)
# mydb.commit()
