#type: ignore
import streamlit as st 
import pandas as pd
import datetime
import csv
import os

MOOD_FILE = 'mood.csv'

def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=['Date', 'Mood'])
    return pd.read_csv(MOOD_FILE)

def save_mood_data(date, mood):
    with open(MOOD_FILE, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([date, mood])

st.set_page_config(page_title='Mood Tracker', page_icon=':smiley:')    
st.title('Mood Tracker')
today = datetime.date.today()



st.subheader("How are you feeling today?")
mood = st.selectbox('Select mood:', ['Happy', 'Sad', 'Neutral', 'Angry'])
if st.button('Save Mood'):
    save_mood_data(today, mood)
    st.success('Mood saved successfully!')
    st.balloons()
    
    
mood_data = load_mood_data()
if not mood_data.empty:
    st.subheader('Mood Trends Over Time')
    mood_data['Date'] = pd.to_datetime(mood_data['Date'])
    mood_count = mood_data.groupby('Mood').count()['Date']
    st.bar_chart(mood_count)
    
if str(today) in mood_data['Date'].values:
    st.warning('You have already logged your mood for today!')
    st.write('Your mood for today is:')
    st.write(mood_data.loc[mood_data['Date'] == str(today)]['Mood'].iloc[0])
    st.write('To update your mood, please wait until tomorrow.')


st.write("built with ❤️ by [Jamila](https://github.com/Jamila654/ramadan-coding-nights-q3)")



