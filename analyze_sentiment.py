from transformers import pipeline
import pandas as pd

# Load the dataset
file_path = 'fifa_world_cup_2022_tweets_no_sentiment.csv'
data = pd.read_csv(file_path)

# Load a pre-trained BERT model for sentiment analysis
classifier = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

# Function to classify sentiment
def classify_sentiment(text):
    result = classifier(text)
    return result[0]['label']

# Apply sentiment analysis
data['Sentiment'] = data['Tweet'].apply(classify_sentiment)

# Save the results
output_path = 'fifa_world_cup_2022_tweets_with_bert_sentiment.csv'
data.to_csv(output_path, index=False)

print(f"Sentiment analysis completed and saved to {output_path}")
