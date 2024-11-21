from shiny import App, render, ui
import pandas as pd
import matplotlib.pyplot as plt

# Sample data - replace this with your actual data loading
data = pd.DataFrame({
    'SEASON_1': ['2022', '2022', '2023'],
    'SEASON_2': ['2023', '2023', '2024'],
    'TEAM_ID': [1, 1, 2],
    'TEAM_NAME': ['Team A', 'Team A', 'Team B'],
    'PLAYER_ID': [101, 102, 103],
    'PLAYER_NAME': ['John', 'Mike', 'Sarah'],
    'POSITION_GROUP': ['OFF', 'OFF', 'DEF'],
    'POSITION': ['QB', 'WR', 'CB'],
    'GAME_DATE': ['2023-01-01', '2023-01-01', '2023-01-08'],
    'GAME_ID': [1001, 1001, 1002]
})

data = pd.read_csv("data/NBA_2024_Shots.csv")

app_ui = ui.page_fluid(
    ui.card(
        ui.card_header("Team Record Counts"),
        ui.output_plot("team_counts")
    )
)

def server(input, output, session):
    @render.plot
    def team_counts():
        # Count records by team name
        team_counts = data['TEAM_NAME'].value_counts()
        
        # Create bar plot
        fig, ax = plt.subplots(figsize=(10, 6))
        team_counts.plot(kind='bar', ax=ax)
        plt.title('Number of Records by Team')
        plt.xlabel('Team Name')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        return fig

app = App(app_ui, server)
