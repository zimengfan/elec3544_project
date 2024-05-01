import pandas as pd
from transformers import pipeline

def analyze_sentiments(tweets_file):
    # Load the tweets
    tweets_df = pd.read_csv(tweets_file)
    
    # Load the sentiment analysis pipeline
    sentiment_analysis = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
    
    # Analyze sentiment for each tweet and store the result
    tweets_df['Sentiment'] = tweets_df['Tweet'].apply(lambda tweet: sentiment_analysis(tweet)[0]['label'])
    
    # Save the dataframe with sentiment to a new CSV file
    output_file = tweets_file.replace('.csv', '_with_sentiment.csv')
    tweets_df.to_csv(output_file, index=False)
    
    return output_file

analyze_sentiments('fifa_world_cup_2022_tweets_no_sentiment.csv')