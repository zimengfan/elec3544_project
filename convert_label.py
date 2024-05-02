import pandas as pd

def update_sentiment_labels(input_csv, output_csv):
    # Load the CSV file
    df = pd.read_csv(input_csv)
    
    # Define the mapping from numeric labels to descriptive labels
    label_map = {
        'LABEL_0': 'Negative',
        'LABEL_1': 'Neutral',
        'LABEL_2': 'Positive'
    }
    
    # Replace numeric labels with descriptive labels
    df['Sentiment'] = df['Sentiment'].map(label_map)
    
    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_csv, index=False)

update_sentiment_labels('filtered_dataset_with_sentiment.csv', 'filtered_dataset_with_sentiment.csv')
