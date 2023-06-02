from datetime import datetime

import sns as sns
from faker import Faker
import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import mysql.connector
from faker import Faker
import random as rand
import requests

#community_graph= nx.barabasi_albert_graph(20, 3)
#nx.draw(community_graph, with_labels=True)

mydb = mysql.connector.connect(
  host="localhost",
  user="alex",
  password="aek21",
  database="mysql"
)

mycursor = mydb.cursor()



##############################    EXERICE 1     #########################################################
# # Create tables
# # mycursor.execute('CREATE TABLE people (user_id INTEGER PRIMARY KEY, username TEXT, age INTEGER)')
# # mycursor.execute('CREATE TABLE Band0 (band_id VARCHAR(255) PRIMARY KEY, band_name TEXT)')
# # mycursor.execute('CREATE TABLE Records0(  record_id VARCHAR(255) PRIMARY KEY, record_name TEXT, band_id VARCHAR(255), FOREIGN KEY (band_id) REFERENCES band0(band_id))')
#
# # Insert fake values in users table
# fake = Faker()
# for user_id in range(1, 21):
#   random_name = fake.name()
#   random_age = str(rand.randint(10, 65))
#
#
#   mycursor.execute("INSERT INTO people (user_id, username, age) VALUES (%s, %s, %s)", (user_id, random_name, random_age))
#   mydb.commit()





# #user records that people own
# mycursor.execute('''
#     CREATE TABLE userrecords (
#         user_id INTEGER,
#         record_id VARCHAR(255),
#         FOREIGN KEY (user_id) REFERENCES people(user_id),
#         FOREIGN KEY (record_id) REFERENCES Records0(record_id)
#     )
# ''')

# # user bands that people like
# mycursor.execute('''
#     CREATE TABLE UserBand (
#         user_id INTEGER,
#         band_id VARCHAR(255),
#         FOREIGN KEY (user_id) REFERENCES people(user_id),
#         FOREIGN KEY (band_id) REFERENCES band0(band_id),
#         PRIMARY KEY (user_id, band_id)
#     )
# ''')

##############################    EXERICE 2     #########################################################

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
#
#
# # My own band data
# band_data = ['Coldplay', 'Paramore', 'Drake', 'Future', 'Nas', 'Eminem', '2Pac', 'Foals', 'Radiohead', 'Gorillaz']
#
# # not duplicates in tables
# visited = []
# visited_name = []
# # 20 users
# for user in range(1, 21):
#     # selects for each user 1 to 3 number of bands he likes
#     num_bands = rand.randint(1, 3)
#     selected_bands = []
#     # number of bands he likes
#     for i in range(num_bands):
#         # selects random bands 1 time each
#         available_bands = list(set(band_data) - set(selected_bands))
#         band = rand.choice(available_bands)
#         selected_bands.append(band)
#         # Api key response
#         url = "http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=" + band + "&api_key=7f9cbec9572f0d227efc718253eded68&format=json"
#         response = requests.get(url)
#         #if good response
#         if response.status_code == 200:
#             # read
#             data = response.json()
#             # get artist name from json
#             artist_name = data['artist']['name']
#             # get artist id from json
#             artist_mbid = data['artist'].get('mbid', None)  # Retrieve mbid or None if missing
#             # if the band has not been inserted yet (no duplicates)
#             if artist_mbid not in visited and artist_name not in visited_name:
#                     #inserts band in database
#                     mycursor.execute("INSERT INTO band0 (band_id, band_name) VALUES (%s, %s)", (artist_mbid, artist_name))
#                     mydb.commit()
#                     # appends
#                     visited.append(artist_mbid)
#                     visited_name.append(artist_name)
#             #skip message
#             else:
#                 print(f"Skipping duplicate entry or missing mbid: {artist_mbid}")
#
#             # inserts user band table
#             mycursor.execute("INSERT INTO userband (user_id, band_id) VALUES (%s, %s)", (user, artist_mbid))
#             mydb.commit()
#         # if no response from api get
#         else:
#             print(f"Failed to fetch data for {band}")
#
#
#
# #
# records_data = ['Ghost Stories', 'Everyday Life', 'Paramore', 'RIOT!', 'Views', 'Future', 'HNDRXX', 'Illmatic', 'Recovery', 'The Eminem Show', 'Greatest Hits', 'All Eyez on Me', 'Holy Fire', 'OK Computer', 'Gorillaz', 'Demon Days']
# records_artists = ['Coldplay', 'Coldplay', 'Paramore', 'Paramore', 'Drake', 'Future', 'Future', 'Illmatic', 'Eminem', 'Eminem', '2Pac', '2Pac', 'Foals', 'Radiohead', 'Gorillaz', 'Gorillaz']
# visited = []
#
# for user in range(1, 21):
#     user_records = []  # Store the user records
#     selected_records = []  # Store the selected record indices
#
#     # Select a random number of bands/records the user likes
#     num_records = rand.randint(1, 3)
#
#     for i in range(num_records):
#         available_records = list(set(range(len(records_data))) - set(selected_records))
#         record_index = rand.choice(available_records)
#         selected_records.append(record_index)
#
#         record_data = records_data[record_index]
#         record_artist = records_artists[record_index]
#
#         url = "http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=7f9cbec9572f0d227efc718253eded68&artist=" + record_artist + "&album=" + record_data + "&format=json"
#         url2 = "http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=" + record_artist + "&api_key=7f9cbec9572f0d227efc718253eded68&format=json"
#         response = requests.get(url)
#         response2 = requests.get(url2)
#
#         if (response.status_code == 200) and (response2.status_code == 200):
#             data = response.json()
#             data2 = response2.json()
#
#             album_info = data['album']
#             record_mbid = album_info.get('mbid')
#             record_name = album_info.get('name')
#
#             artist_mbid = data2['artist'].get('mbid', None)
#             if artist_mbid:
#                 query = "SELECT band_id FROM band0 WHERE band_id = %s"
#                 mycursor.execute(query, (artist_mbid,))
#                 result = mycursor.fetchone()
#
#             if (record_name not in visited) and result:
#                 mycursor.execute("INSERT INTO records0 (record_id, record_name, band_id) VALUES (%s, %s, %s)", (record_mbid, record_name, artist_mbid))
#                 mydb.commit()
#                 visited.append(record_name)
#
#                 # Add the record_id to the user_records list
#                 user_records.append(record_mbid)
#
#         # Insert the user records into the userrecords table
#         query = "SELECT record_id FROM records0 WHERE record_id = %s"
#         mycursor.execute(query, (record_mbid,))
#         result = mycursor.fetchone()
#         if result:
#             mycursor.execute("INSERT INTO userrecords (user_id, record_id) VALUES (%s, %s)", (user, record_mbid))
#             mydb.commit()



##############################    EXERICE 3     #########################################################
# # Insert band_id but no name (missing value)
# mycursor.execute("INSERT INTO band0 (band_id, band_name) VALUES (%s, %s)", ("test1", None))
# mycursor.execute("INSERT INTO band0 (band_id, band_name) VALUES (%s, %s)", ("test2", None))
# mydb.commit()

# # sees where is null
# mycursor.execute("SELECT * FROM band0 WHERE band_id IS NULL OR band_name IS NULL")
#
# # Fetch all rows with missing values
# rows_with_missing_values = mycursor.fetchall()
#
# # Loop through the rows and delete them one by one
# for row in rows_with_missing_values:
#     sql_delete = "DELETE FROM band0 WHERE band_id = %s"  # Replace id with the primary key column name of your table
#     mycursor.execute(sql_delete, (row[0],))  # Assuming the primary key is in the first column
#
# mydb.commit()


# # Insert a fake band that is duplicate
# mycursor.execute("INSERT INTO band0 (band_id, band_name) VALUES (%s, %s)", ("test3", "2Pac"))
# mycursor.execute("INSERT INTO band0 (band_id, band_name) VALUES (%s, %s)", ("test4", "Future"))
# mydb.commit()
#
# mycursor.execute("""
#     DELETE FROM band0
#     WHERE band_id NOT IN (
#         SELECT MIN(band_id)
#         FROM band0
#         GROUP BY band_name
#         HAVING COUNT(*) > 1
#     )
# """)
# mydb.commit()
# duplicate_rows = mycursor.fetchall()
#
# # Remove duplicate rows
# for row in duplicate_rows:
#     band_name = row[0]
#     delete_query = "DELETE FROM band0 WHERE band_name = %s"
#     mycursor.execute(delete_query, (band_name,))
#     mydb.commit()


##############################    EXERICE 4     #########################################################
############## people's age #############
# # Fetch data from the people table
# people_query = "SELECT age FROM people"
# people_df = pd.read_sql(people_query, mydb)
#
# # Prints people's age statistics
# print("Users Age Statistics:\n" + people_df["age"].describe().to_string())
#
#
# ######### userbands ###############
# # Fetch data from the userbands table
# userbands_query = "SELECT * FROM userband"
# userbands_df = pd.read_sql(userbands_query, mydb)
#
# # Fetch the bands DataFrame
# bands_df = pd.read_sql("SELECT band_id, band_name FROM band0", mydb)
#
# # Merge userbands_df with bands_df based on band_id
# merged_df = pd.merge(userbands_df, bands_df, on='band_id')
#
# # Count the occurrences of each band_name
# band_counts = merged_df['band_name'].value_counts()
#
# # Print the band counts
# print("\n" + band_counts.to_string())
#
#
# ############ userrecords ##############
# # Fetch data from the userrecords table
# userrecords_query = "SELECT * FROM userrecords"
# userrecords_df = pd.read_sql(userrecords_query, mydb)
#
#
# # Fetch the records DataFrame
# records_df = pd.read_sql("SELECT record_id, record_name FROM records0", mydb)
#
# # Merge
# merged_df = pd.merge(userrecords_df, records_df, on='record_id')
#
# # Count the occurrences
# records_counts = merged_df['record_name'].value_counts()
#
# # Print
# print("\n" + records_counts.to_string())



##############################    EXERICE 5     #########################################################
####################### age ##########################
# # Define the age groups
# age_groups = [10, 25, 40, 50, 65]
#
# # Cut the age column into groups
# people_df['age_group'] = pd.cut(people_df['age'], bins=age_groups)
#
# # Count the number of individuals in each age group
# age_counts = people_df['age_group'].value_counts().sort_index()
#
# # Create a bar plot
# age_counts.plot(kind='bar')
#
# # Set the title and labels
# plt.title('Age Group Counts')
# plt.xlabel('Age Group')
# plt.ylabel('Count')
#
# # Display the plot
# plt.show()
#
# ####################### bands ##########################
# # Create a bar plot
# band_counts.plot(kind='bar')
#
# # Set the title and labels
# plt.title('Band Counts')
# plt.xlabel('Band')
# plt.ylabel('Count')
#
# # Display the plot
# plt.show()
#
# ####################### records ##########################
# # Create a bar plot
# records_counts.plot(kind='bar')
#
# # Set the title and labels
# plt.title('record Counts')
# plt.xlabel('Record')
# plt.ylabel('Count')
#
# # Display the plot
# plt.show()



##############################    EXERICE 6     #########################################################
