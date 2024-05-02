import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')

# Load the dataset
file_path = 'filtered_dataset_with_sentiment.csv'  # Updated file path
data = pd.read_csv(file_path)

# Convert 'Date Created' to datetime
data['Date Created'] = pd.to_datetime(data['Date Created']).dt.date

# 1. Sentiment Distribution Analysis
sentiment_distribution = data['Sentiment'].value_counts()
sentiment_distribution.plot(kind='pie', title='Sentiment Distribution', autopct='%1.1f%%', startangle=90)
plt.ylabel('')  # Remove the label for the y-axis
plt.show()

# 2. Sentiment Trends Over Time
sentiment_trends = data.groupby(['Date Created', 'Sentiment']).size().unstack().fillna(0)
sentiment_trends.plot(kind='line', title='Sentiment Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Tweets')
plt.show()

# 3. Engagement Analysis
# Assuming 'Number of Likes' as a measure of engagement
data['Likes'] = pd.to_numeric(data['Number of Likes'], errors='coerce').fillna(0)
engagement_sentiment = data.groupby('Sentiment')['Likes'].mean()
engagement_sentiment.plot(kind='bar', title='Average Likes per Sentiment')
plt.xlabel('Sentiment')
plt.ylabel('Average Likes')
plt.xticks(rotation=0)
plt.show()

# 4. Textual Analysis
# Remove stopwords and tokenize words
stop_words = set(stopwords.words('english'))
data['Tokenized Tweets'] = data['Tweet'].apply(lambda x: [word for word in word_tokenize(x.lower()) if word.isalpha() and word not in stop_words])

# Join all tweets into one massive text
all_words = ' '.join([word for sublist in data['Tokenized Tweets'] for word in sublist])
wordcloud = WordCloud(width = 800, height = 500, random_state=21, max_font_size=110).generate(all_words)

plt.figure(figsize=(10, 7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.title('Word Cloud of Tweets')
plt.show()

# 5. Advanced analysis: Keyword frequency
freq_dist = nltk.FreqDist(word for word_list in data['Tokenized Tweets'] for word in word_list)
freq_dist.plot(30, cumulative=False)

# 6. Box Plot for sentiment across different engagement levels
sns.boxplot(x='Sentiment', y='Likes', data=data)
plt.title('Engagement Level by Sentiment')
plt.xlabel('Sentiment')
plt.ylabel('Likes')
plt.show()

# 7. Bubble Chart (assuming data contains match days)
bubble_data = data.groupby(['Date Created', 'Sentiment']).agg({'Likes': 'sum', 'Tweet': 'count'}).reset_index()
bubble_data.rename(columns={'Tweet': 'Count'}, inplace=True)
plt.scatter(bubble_data['Date Created'], bubble_data['Sentiment'], s=bubble_data['Count']*10, c=bubble_data['Likes'], cmap='viridis', alpha=0.6, edgecolors="w", linewidth=2)
plt.colorbar(label='Sum of Likes')
plt.title('Bubble Chart of Sentiments and Engagement over Time')
plt.xlabel('Date')
plt.ylabel('Sentiment')
plt.show()
