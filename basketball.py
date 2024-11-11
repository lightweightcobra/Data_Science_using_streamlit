import streamlit as st
import pandas as pd
import numpy as np

st.title('NBA Player Statistics Explorer')

st.markdown("""
This app displays NBA player statistics from an uploaded CSV file.
* **Python Libraries:** pandas, streamlit
""")

st.sidebar.header("User Input Features")

# Load CSV data
uploaded_file = '/mnt/data/2024-10-30T17-40_export.csv'

@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    return df

# Load data from the uploaded CSV file
playerstats = load_data(uploaded_file)

# Dictionary mapping team abbreviations to full team names
team_name_map = {
    'ATL': 'Atlanta Hawks', 'BOS': 'Boston Celtics', 'BRK': 'Brooklyn Nets', 
    'CHA': 'Charlotte Hornets', 'CHI': 'Chicago Bulls', 'CLE': 'Cleveland Cavaliers', 
    'DAL': 'Dallas Mavericks', 'DEN': 'Denver Nuggets', 'DET': 'Detroit Pistons',
    'GSW': 'Golden State Warriors', 'HOU': 'Houston Rockets', 'IND': 'Indiana Pacers', 
    'LAC': 'Los Angeles Clippers', 'LAL': 'Los Angeles Lakers', 'MEM': 'Memphis Grizzlies', 
    'MIA': 'Miami Heat', 'MIL': 'Milwaukee Bucks', 'MIN': 'Minnesota Timberwolves', 
    'NOP': 'New Orleans Pelicans', 'NYK': 'New York Knicks', 'OKC': 'Oklahoma City Thunder', 
    'ORL': 'Orlando Magic', 'PHI': 'Philadelphia 76ers', 'PHO': 'Phoenix Suns', 
    'POR': 'Portland Trail Blazers', 'SAC': 'Sacramento Kings', 'SAS': 'San Antonio Spurs', 
    'TOR': 'Toronto Raptors', 'UTA': 'Utah Jazz', 'WAS': 'Washington Wizards'
}

# Apply the mapping to the 'Team' column to display full team names
if 'Team' in playerstats.columns:
    playerstats['Team'] = playerstats['Team'].replace(team_name_map)

# Sidebar - Team selection with type conversion and sorting
sorted_team = sorted(playerstats['Team'].astype(str).unique())
selected_team = st.sidebar.selectbox('Team', sorted_team)

# Sidebar - Position selection, with default selection as 'All'
if 'Pos' in playerstats.columns:
    unique_pos = ['All'] + list(playerstats['Pos'].unique())
    selected_pos = st.sidebar.selectbox('Position', unique_pos)
else:
    selected_pos = 'All'

# Filter data based on selections
filtered_data = playerstats

if selected_team:
    filtered_data = filtered_data[filtered_data['Team'] == selected_team]

if selected_pos != 'All':
    filtered_data = filtered_data[filtered_data['Pos'] == selected_pos]

# Display filtered data
st.header('Displaying Player Stats of Selected Team and Position')
st.write(f'Data Dimension: {filtered_data.shape[0]} rows and {filtered_data.shape[1]} columns.')
st.dataframe(filtered_data)
