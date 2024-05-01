import pandas as pd

# Load the original dataset
file_path = 'fifa_world_cup_2022_tweets.csv'
data = pd.read_csv(file_path)

# Drop the 'Sentiment' column
data_cleaned = data.drop(columns=['Sentiment'])

# Save the cleaned dataset to a new CSV file
output_path = 'fifa_world_cup_2022_tweets_no_sentiment.csv'
data_cleaned.to_csv(output_path, index=False)