import json
import sqlite3
import pandas as pd
import re

conn = sqlite3.connect('grainstweets1.sqlite')
cur = conn.cursor()

tweets_data_path = 'grainstweets1.txt'
tweets_data = []
tweets_file = open(tweets_data_path, "r")

for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
tweets['time'] = map(lambda tweet: tweet['created_at'], tweets_data)
tweets['user'] = map(lambda tweet: tweet['user']['screen_name'], tweets_data)
tweets['user_id'] = map(lambda tweet: tweet['user']['id'], tweets_data)
tweets['user_followers'] = map(lambda tweet: tweet['user']['followers_count'], tweets_data)
# tweets_by_lang = tweets['lang'].value_counts()

# fig, ax = plt.subplots()
# ax.tick_params(axis='x', labelsize=15)
# ax.tick_params(axis='y', labelsize=10)
# ax.set_xlabel('Languages', fontsize=15)
# ax.set_ylabel('Number of tweets' , fontsize=15)
# ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
# tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
# plt.show()

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False


tweets['corn'] = tweets['text'].apply(lambda tweet: word_in_text('corn', tweet))
tweets['soybean'] = tweets['text'].apply(lambda tweet: word_in_text('soybean', tweet))
tweets['wheat'] = tweets['text'].apply(lambda tweet: word_in_text('wheat', tweet))

print tweets['corn'].value_counts()[True]
print tweets['soybean'].value_counts()[True]
print tweets['wheat'].value_counts()[True]

def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''


tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))

tweets_soybean = tweets[tweets['soybean'] == True]
tweets_soybean_with_link = tweets_soybean[tweets_soybean['link'] != '']
tweets_corn = tweets[tweets['corn'] == True]
tweets_corn_with_link = tweets_corn[tweets_corn['link'] != '']
tweets_wheat = tweets[tweets['wheat'] == True]
tweets_wheat_with_link = tweets_wheat[tweets_wheat['link'] != '']

tweets_with_link = {'soybean': tweets_soybean_with_link,
                    'corn': tweets_corn_with_link,
                    'wheat': tweets_wheat_with_link}

cur.executescript('''
DROP TABLE IF EXISTS soybean;
DROP TABLE IF EXISTS corn;
DROP TABLE IF EXISTS wheat;
DROP TABLE IF EXISTS grain;

CREATE TABLE corn (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    text TEXT  UNIQUE,
    lang TEXT,
    country TEXT,
    time TIME , user TEXT, user_id INTEGER, user_followers INTEGER, corn TEXT, soybean TEXT, wheat TEXT, link TEXT
);
CREATE TABLE wheat (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    text TEXT  UNIQUE,
    lang TEXT,
    country TEXT,
    time TIME , user TEXT, user_id INTEGER, user_followers INTEGER, corn TEXT, soybean TEXT, wheat TEXT, link TEXT
);
CREATE TABLE grain (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    text TEXT
);
CREATE TABLE soybean (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    text TEXT  UNIQUE,
    lang TEXT,
    country TEXT,
    time TIME , user TEXT, user_id INTEGER, user_followers INTEGER, corn TEXT, soybean TEXT, wheat TEXT, link TEXT
);
''')

#print tweets_with_link['soybean'][-1:]
count = -1
count2 = 0
for entry in tweets_with_link['corn']['text']:
    count += 1
    count2 += 1
    text = tweets_with_link['corn']['text'][count:count2]
    #print text
    country = tweets_with_link['corn']['country'][count:count2]
    lang = tweets_with_link['corn']['lang'][count:count2]
    cur.execute('''INSERT OR IGNORE INTO corn (text, country, lang)
      VALUES ( ?, ?, ? )''', ( unicode(text), unicode(country), unicode(lang)) )

conn.commit()

