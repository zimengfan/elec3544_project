# elec3544_project
Fan Zimeng 3035952745<br/>
This is all the files I used and wrote for the project.
<br/>
<br/>

The csv file ***fifa_world_cup_2022_tweets_original.csv*** is the original dataset I took from https://github.com/Mr-Chang95/FIFA-Sentiment-Analysis.
<br/>
<br/>
The file ***remove_sentiment.py*** is the Python script I used to remove the "Sentiment" section/column that comes with the original file. I removed it because I want to make the sentiment analysis on my own, as that is apart of my project. The csv file ***fifa_world_cup_2022_tweets_no_sentiment.csv*** is the generated file from the Python script.
<br/>
<br/>
The file ***dataset_filtering.py*** is the Python script I used to clean the dataset and remove all unnecessary informations like the URLS. The generated csv file is ***filtered_dataset.csv***
<br/>
<br/>
The file ***Tweet_Sentiment_Analysis*** is the python script for running the "transformer" on the dataset ***filtered_dataset.csv*** to analyze the sentiments in the comments and label each comments as Negative, Neutral, or Positive. However, the generated results does not say "Negative", "Neutral", and "Positive" directly, instead it is labeled as "Label_0", "Label_1", and "Label_2".
<br/>
<br/>
The file ***convert_label.py*** does the job of converting from "Label 0/1/2" to "Negative/Neutral/Positive".
<br/>
<br/>
The file ***comprehensive_analysis.py*** is the final Python script I executed to generate all the visualizations from the dataset.
