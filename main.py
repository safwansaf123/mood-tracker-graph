'''MOOOD TRACKER'''

# here we will use streamlit to run applocation for python
#uv init Time-zone  folder creation
#uv add streamlit   module imported
# PANDAS new package for data manepulation to show data on UI 
# PANDAS IS PART OF STREAMLIT to install pandas
# uv add streamlit-pandas
#.venv\Scripts\activate    virtual environment activated
# rainbow csv extension is used for 


import streamlit as safoo     # today iam using streamlit as safoo (no st)    for web interface
import pandas as pd           # pandas as pd, here pandas is used for It's a library for data manipulation and analysis. 
                             #It provides data structures like DataFrame and Series to handle and process structured data efficiently
import datetime     # used for date and time
import csv          # 
import os

# wriiten in caps means used as constant variable data will not change in it
# data contain in it will be used for many purposes example read run write etc....
MOOD_FILE = "mood_log.csv"

# function created to load it or read data from csv file ie, mood.log.csv
def load_mood_data():
    # check if file exists or not
    if not os.path.exists(MOOD_FILE):      # first check that mood file have some data in it,  so logic used if not 
        # if no file, create empty dataframe with cloumns
        return pd.DataFrame(columns=["Date", "Mood"])  # in return put data in format of column of heading date and mood
    return pd.read_csv(MOOD_FILE)  # read & return existing mood data


# function created to save data or add new mood entry to csv files
def save_mood_data(date, mood):
    # open file in append mode 
    with open(MOOD_FILE, "a" ) as file:              # with.open is used to
    
        writer = csv.writer(file)       # writer variable created, to write csv data 
        writer.writerow([date, mood])   # write data in format of rows or add new mood entry


# heading creating with streamlit
safoo.title("Mood Tracker")

# in variable today current date and time added to recall later
today =  datetime.date.today()

# another heading with streamlit 
safoo.subheader("How are you feeling today")

# mood variable created which contain selection box of streamlit to select the moods, and later will be used
mood = safoo.selectbox("Select your mood", ["Happy", "Sad", "Neutral", "Angry"])

#button created & condition is used, if user click on log mood button after selection, save data in above function i.e is mood.log.csv
if safoo.button("Log Mood"):
    # save mood when button is clicked
    save_mood_data(today, mood)   # two argument passed today and mood in the function that have recalled

safoo.success("Mood logged successfuly")  # message printed that logged succes fully

# data as variable is used to load data or load2 existing mood data
data = load_mood_data()

# first check load_mood_data, contain data in it logic used
if not data.empty:       # if data variable is not empty,     empty is python

# another heading for visualization 
  safoo.subheader("Mood Trends over Time")
 
 # Convert date stings to datetime Objects
data["Date"] = pd.to_datetime(data["Date"])

# Count frequency of each mood, changes made in mood_log.csv file Date and Mood added on top as column heading use it here for count
# after grouping or groupby
mood_counts = data.groupby("Mood").count()["Date"]

# Display bar chart of mood frequencies
safoo.bar_chart(mood_counts)

# Build with love by Asharib Ali
safoo.write("learned with ❤️ by [Asharib Ali](https://github.com/AsharibAli)")