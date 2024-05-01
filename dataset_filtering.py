import pandas as pd
import re

def preprocess_tweets(input_csv, output_csv):
    # Load the CSV file
    df = pd.read_csv(input_csv)
    
    # Define a function to remove URLs
    def remove_urls(text):
        # Regex pattern to find URLs
        url_pattern = r'https?://\S+|www\.\S+'
        return re.sub(url_pattern, '', text)
    
    # Apply the URL removal function to each tweet
    df['Tweet'] = df['Tweet'].apply(remove_urls)
    
    # Save the preprocessed tweets back to a new CSV file
    df.to_csv(output_csv, index=False)

preprocess_tweets('fifa_world_cup_2022_tweets_dataset.csv', 'filtered_dataset.csv')
