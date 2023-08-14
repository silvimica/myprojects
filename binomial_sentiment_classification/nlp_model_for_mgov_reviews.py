import pandas as pd
import numpy as np
import emoji
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report


# Most common misspeling in Kazakh and Russian 

misspelling_dictionary ={'кермет':'керемет', 'рахме':'рахмет', 'kuwty':'күшті', 'отллично':'отлично', 'отшично':'отлично', 'бустро':'быстро', 'кушты':'күшті',
'хрошо':'хорошо', 'jahsy':'жақсы', 'kyshti':'күшті', 'куштии':'күшті', 'спаибо':'спасибо', 'жакс':'жақсы', 'класснр':'классно', 'жаасы':'жақсы', 'супеп':'супер',
'хоршо':'хорошо', 'отлчно':'отлично', 'жаңсы':'жақсы', 'отличнр':'отлично', 'сбасибо':'спасибо', 'окк':'ок', 'жаусы':'жақсы', 'отоично':'отлично', 'супкр':'супер',
'жаңсы':'жақсы', 'жақсыы':'жақсы', 'керемат':'керемет', 'звмечательно':'замечательно', 'кушті':'күшті', 'хорлшо':'хорошо', 'керемер':'керемет', 'отличпо':'отлично', 
'horosho':'хорошо', 'керемер':'керемет', 'хтрошо':'хорошо',  'коуто':'круто', 'жахси':'жақсы', 'хоро ':'хорошо', 'нормс':'норм',  'отте':'өте', 'оте':'өте',  'нәшар':'нашар',
 'өтте':'өте', 'долг ':'долго', 'күшт':'күшті'}
 

# This function corrects spelling based on the provided disctionary
def correct_spelling(x, dic):
    for word in dic.keys():
        x = x.replace(word, dic[word])
    return x

# This function removes duplicate letters from words, leaving only one. 
# This way, 'greaaat' and 'greaaaaaat' will be converted to the same word 'great', making a classification easier.
def remove_consec_duplicates(s):
    new_s = ""
    prev = ""
    for c in s:
        if len(new_s) == 0:
            new_s += c
            prev = c
        if c == prev:
            continue
        else:
            new_s += c
            prev = c
    return new_s

# Separating emojies written wihtout spaces. This way there is no confusion between 2 and 3 of the same emojies.
def extract_emojis(s):
    return ''.join((' '+c+' ') if c in emoji.EMOJI_DATA else c for c in s)


# This function normalizes the data using functions above
def normalize(df, dic):
    df["content_normalized"] = df["content"].str.lower()
    df["content_normalized"] = df["content_normalized"].str.replace("," , " ")
    df["content_normalized"] = df["content_normalized"].str.replace("." , " ")
    df['content_normalized'] = df['content_normalized'].apply(lambda x: extract_emojis(x))
    df['content_normalized'] = df['content_normalized'].apply(lambda x: correct_spelling(x, dic))
    df['content_normalized'] = df['content_normalized'].apply(lambda x: remove_consec_duplicates(x))
    df["content_normalized"] = df["content_normalized"].str.strip()
    return df


def prepare_data(df, column_X, column_Y):
    
    X = df[column_X]
    y = df[column_Y]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    count_vector = TfidfVectorizer(token_pattern=r'[^\s]+')

    X_train_counts = count_vector.fit_transform(X_train)

    tfidf_transformer = TfidfTransformer()

    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

    X_test_counts = count_vector.transform(X_test)

    X_test_tfidf = tfidf_transformer.transform(X_test_counts)

    return X_train_tfidf, X_test_tfidf, y_train, y_test


# Get labeled positive and negative reviews
positive = pd.read_csv('positive_reviews.csv')
negative = pd.read_csv('negative_reviews.csv')

### Preparing data

# Marking sentiment numerically

positive['sentiment_numeric'] = 1
negative['sentiment_numeric'] = 0

df = pd.concat([positive, negative])

# Normalizing data

df = normalize(df, misspelling_dictionary)

# Shuffling rows in data
df = df.sample(frac = 1)

X_train, X_test, y_train, y_test = prepare_data(df, 'content_normalized', 'sentiment_numeric')

clf = MultinomialNB().fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(classification_report(y_test, y_pred))