import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import streamlit as st


plt.style.use('fivethirtyeight')

df = pd.read_csv('train_stations_europe.csv')
df = pd.DataFrame(data=df)
st.title("European Train Stations Maps")
st.markdown("This Application is  Streamlit Dashboard ")

st.markdown('European (Train) Main Stations')

fig_px = px.scatter_mapbox(df, lat="latitude", lon="longitude",
                           hover_name="name",
                           zoom=11, height=300)
fig_px.update_layout(mapbox_style="open-street-map",
                     margin={"r": 0, "t": 0, "l": 0, "b": 0})

st.write(fig_px)

st.markdown('Find Specific European (Train) Main Stations')

city = []

for i in df['name']:
    if i not in city:
        city.append(i)

city1 = st.selectbox("City", city)
if st.button('Get Specific City You Are Searching  For!'):
    city_map = df[(df['name'] == city1)].reset_index(drop=True)
    city_map.tail()
    fig_px = px.scatter_mapbox(city_map, lat="latitude", lon="longitude",
                               hover_name="name_norm",
                               zoom=11, height=300)
    fig_px.update_layout(mapbox_style="open-street-map",
                         margin={"r": 0, "t": 0, "l": 0, "b": 0})

    st.write(fig_px)

st.markdown('European (Train) Stations in Airports')

g = sns.lmplot(x="longitude", y="latitude", data=df,
               fit_reg=False, scatter_kws={"s": 30}, hue='is_airport', height=10)

st.pyplot(g)

st.markdown('European (Train) Stations in Cities')
g = sns.lmplot(x="longitude", y="latitude", data=df,
               fit_reg=False, scatter_kws={"s": 30}, hue='is_city', height=10)

st.pyplot(g)
