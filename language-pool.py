import random
import json
from datetime import date

# Language list with weight
languages = {
    'Go': 1,
    'Python': 1
}

RAND_INT_MAX = 1000000

# Generate pool
pool = []
for l in languages:
    pool += [l] * languages[l]

# Make the pool bigger for get better random results
pool *= 20
# Total number of days we want to handle
number_of_days = 25
# Make sure we get the same random numbers in order
# Update for production
random.seed(4080877)

selected_languages = []

for day in xrange(number_of_days):
    random_number = random.randint(0, RAND_INT_MAX)
    target_language = pool[random_number % len(pool)]
    if day > 1:
        while target_language == selected_languages[day - 1]:
            random_number = random.randint(0, RAND_INT_MAX)
            target_language = pool[random_number % len(pool)]
    selected_languages.append(target_language)

def response(body):
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': "*"
        },
        'body': json.dumps(body)
    }

def index(event, context):
    today = date.today()

    if today.month != 12:
        return response({
            'error': 'No AoC2018 yet! Patience, patience...'
        })

    history = {}
    for index, language in enumerate(selected_languages[0:today.day - 1]):
        history["day-%02d" % (index + 1)] = language

    if today.day > number_of_days:
        return response({
            'error': 'No more AoC2018, sorry'
        })

    return response({
        'day': 'day-%02d' % (today.day),
        'language': selected_languages[today.day - 1],
        'url': 'https://adventofcode.com/2018/day/%d' % (today.day),
        'history': history
    })

