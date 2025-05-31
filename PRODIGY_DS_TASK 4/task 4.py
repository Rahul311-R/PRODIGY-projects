import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

file_name = 'data 2.csv'
data = None
try:
    # Load the dataset with error handling
    data = pd.read_csv(file_name, on_bad_lines='skip', engine='python')
    print(data.head())
    print("Columns in the dataset:", data.columns.tolist())
except Exception as e:
    print(f"An error occurred: {e}")

if data is not None:

    if 'text' in data.columns and 'sentiment' in data.columns:
        # Data Cleaning
        data.dropna(subset=['text', 'sentiment'], inplace=True)

        # Sentiment Distribution
        plt.figure(figsize=(8, 5))
        sns.countplot(x='sentiment', data=data)
        plt.title('Sentiment Distribution')
        plt.xlabel('Sentiment')
        plt.ylabel('Count')
        plt.show()


        data['date'] = pd.to_datetime(data['date'])
        sentiment_over_time = data.groupby(data['date'].dt.date)['sentiment'].value_counts().unstack().fillna(0)
        sentiment_over_time.plot(kind='line', figsize=(12, 6))
        plt.title('Sentiment Over Time')
        plt.xlabel('Date')
        plt.ylabel('Count')
        plt.legend(title='Sentiment')
        plt.show()


        positive_words = ' '.join(data[data['sentiment'] == 'positive']['text'])
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(positive_words)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Word Cloud for Positive Sentiment')
        plt.show()
    else:
        print("The expected columns 'text' and 'sentiment' are not found in the dataset.")
else:
    print("Data could not be loaded. Please check the file name and format.")
