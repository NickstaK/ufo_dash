import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path

# Page config
st.set_page_config(page_title="UFO Sightings Dashboard", layout="wide")

# Title
st.title("🛸 UFO Sightings Explorer")

# Path to cleaned data
clean_path = Path("data/clean/complete_clean.csv")

@st.cache_data
def load_data(path):
    """Load and cache the cleaned CSV data."""
    return pd.read_csv(path)

# Load data or show error
try:
    df = load_data(clean_path)
except FileNotFoundError:
    st.error(f"Clean file not found at {clean_path}. Run the cleaning script first.")
    st.stop()

# Show raw data toggle
if st.checkbox("Show raw data"):
    st.dataframe(df)

# Sidebar filters
st.sidebar.header("Filter Sightings")
if 'year' in df.columns:
    years = sorted(df['year'].unique())
    year_sel = st.sidebar.multiselect("Year", years, default=years[-3:])
    df = df[df['year'].isin(year_sel)]

if 'shape' in df.columns:
    shapes = sorted(df['shape'].dropna().unique())
    shape_sel = st.sidebar.multiselect("Shape", shapes, default=shapes[:3])
    df = df[df['shape'].isin(shape_sel)]

# Key metric: total sightings
st.markdown(f"**Total sightings:** {len(df):,}")

# Bar chart: sightings by state
if 'state' in df.columns:
    state_counts = df['state'].value_counts().reset_index()
    state_counts.columns = ['state','count']
    chart_state = alt.Chart(state_counts).mark_bar().encode(
        x=alt.X('state:N', sort='-y', title='State'),
        y=alt.Y('count:Q', title='Count of Sightings')
    ).properties(width=800, height=400)
    st.altair_chart(chart_state, use_container_width=True)

# Map view of coordinates
if {'latitude','longitude'}.issubset(df.columns):
    st.map(df[['latitude','longitude']].dropna())

# Time-series chart if datetime column exists
if 'datetime' in df.columns:
    df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
    df_time = df.dropna(subset=['datetime'])
    time_counts = df_time.groupby(df_time['datetime'].dt.year).size().reset_index(name='count')
    chart_time = alt.Chart(time_counts).mark_line(point=True).encode(
        x=alt.X('datetime:O', title='Year'),
        y=alt.Y('count:Q', title='Sightings')
    ).properties(width=800, height=300)
    st.altair_chart(chart_time, use_container_width=True)
