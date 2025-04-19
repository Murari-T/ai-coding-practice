"""Sentiment Categorizer
🎯 Problem:
You're building an AI-based feedback system. You get a list of sentiment scores from a model (0 = negative, 1 = positive).
Write a function to classify and count how many are:

Positive (> 0.6)

Neutral (0.4 to 0.6)

Negative (< 0.4)"""


def sentiment(scores):

    postive=list(filter(lambda x:x>0.6 , scores))
    netural=list(filter(lambda x:0.4<=x<=0.6 , scores))
    negative=list(filter(lambda x:x<0.4 , scores))

    return {
            "Postive":len(postive),
            "Netural":len(netural),
            "Negative":len(negative)
        }

print(f"sentiment scores {sentiment(scores=[0.9, 0.3, 0.6, 0.45, 0.2, 0.78, 0.5, 0.88, 0.1])}")