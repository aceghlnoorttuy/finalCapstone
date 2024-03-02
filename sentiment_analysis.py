# Make libraries accessible and define constants.
import spacy
import pandas as pd
import random
from textblob import TextBlob
nlp = spacy.load('en_core_web_sm')
my_csv = ('amazon_product_reviews.csv')
my_column = 'reviews.text'
# Offer option to input different csv. Continue to do so until valid path is
# given.
cont = 'yes'
while cont == 'yes':
    user_csv = input('Please enter the file path of the reviews csv you would '
                     'like to assess. To work with the default file, '
                     'enter: default. ')
    if user_csv != 'default':
        my_csv = user_csv
    else:
        my_csv = 'amazon_product_reviews.csv'
        cont = 'no'
    try:
        f = open(my_csv)
        cont = 'no'
    except:
        print(f'Error occurred when opening {my_csv} to read.')
# Read relevant column, remove blank entries, remove white space within entries
# and make uniformly lower case.
df = pd.read_csv(my_csv)
df = df.dropna(subset = [my_column])
df[my_column] = df[my_column].str.lower()
df[my_column] = df[my_column].str.strip()
# Define function for removing stopwords.
def remove_stopwords(text):
    doc = nlp(text)
    tokens_without_stopwords = [token.text for token in doc if not token.is_stop]
    return ' '.join(tokens_without_stopwords)
# Define function for sentiment analysis.
def sentiment_analysis(text):
    text = remove_stopwords(text)
    doc = nlp(text)
    tb_s = TextBlob(text).sentiment.polarity
    if tb_s > 0:
        pol = 'Positive'
    elif tb_s < 0:
        pol = 'Negative'
    else:
        pol = 'Neutral'
    # Return results.
    return (f"Review at index: {index}.\nCleaned Text reads: {text}.\nTextblob "
          f"sentiment polarity: {pol}.\nSentiment score: {tb_s}.")
# Ensure that sample size is a positive integer. Set count to 0 and add 1 each
# time while count is less than desired sample size. Pick an entry for each
# random number.
count = 0
cont = 'yes'
while cont == 'yes':
    sample_size = input('What size sample would you like to take? Enter a '
                        'positive integer. ' )
    try:
        a = int(sample_size)
        if a < 0:
            cont = 'yes'
        else:
            cont = 'no'
    except:
        cont = 'yes'
while count < int(sample_size):
    index = random.randint(0, len(df))
    count = count + 1
# Apply sentiment - analysis function.
    text = df.at[index, my_column]
    print(sentiment_analysis(text))
# Introduce similarity function.
def text_similarity(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
# Calculate the similarity between the two texts
    similarity_score = doc1.similarity(doc2)
    return similarity_score
# Apply similarity function to two review.
text1 = df[my_column][109]
text2 = df[my_column][9098]
print(f"Similarity score is {text_similarity(text1, text2)}")


