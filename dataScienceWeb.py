import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

#streamlit run dataScienceWeb.py

#Constants
DATA_PATH = "./data/Motor_Vehicle_Collisions_-_Crashes.csv"

st.title("Motor Vehicle Collisions 👨‍💼")

st.markdown("### This web aplications is created to create a dashboard that show where and how many collitions happened in NYC")

@st.cache(persist=True)
def load_data(rows=None):
    data = pd.read_csv(DATA_PATH, nrows=rows, parse_dates=[['CRASH_DATE', 'CRASH_TIME']])
    data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
    data.rename(lambda lt: str(lt).lower(), inplace=True, axis='columns')
    data.rename(columns={'crash_date_crash_time': 'date/time'}, inplace=True)
    return data

data = load_data(100000)
st.header('Data CSV')
st.write(data)

st.header("Positions of collisions at number")
slide = st.slider("Number of Collisions at same point", 1, 10)
st.map(data.query("injured_persons >= @slide")[['latitude', 'longitude']].dropna(how="any"))


st.header("Collisions filter by daytime")
if st.checkbox("Show Filter", False):
    hour = st.selectbox("Select the timeday: ", range(0, 24), 1)
    data_2 = data[data['date/time'].dt.hour == hour]
    st.subheader("Data: ")
    st.write(data_2)
    if st.checkbox("Show Map CSV", False):
        st.map(data_2[['latitude', 'longitude']].dropna(how="any"))


st.write(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state={
        "latitude": np.average(data['latitude']),
        "longitude": np.average(data['longitude']),
        "zoom": 11,
        "pitch": 60
    },
    layers=[
        pdk.Layer(
            "HexagonLayer",
            data = data[['latitude', 'longitude']],
            get_position = ['longitude', 'latitude'],
            radius = 100,
            extruded = True,
            pickable = True,
            elevation_scale = 5,
            elevation_range = [0, 1000]
        )
    ]
))


st.header("Data analisys:")
st.subheader("Top dangerous streets to pedestrians")
st.write(data.query("injured_pedestrians >= 1")[['on_street_name', 'injured_pedestrians']].sort_values(by=['injured_pedestrians'], ascending=False).dropna(how="any")[:5])
