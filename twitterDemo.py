from twitter import *

access_token = '65962166-2yYXHTmH7X0vXy5sh1hDp2RlXfbcu959VhdHnjGWh'
access_token_secret = 'QI9zsM0vRwtvTq455k4xkEbbcH2cvpHlalOj187kNN4wo'
consumer_key = 'DkPQfFHhPadZyNqvvqyoXSV1p'
consumer_secret = 'QPDDdc6fCP0ApGVPdtl7UOxfIxIbcLQSjiObX2gvsEmtv5d6i8'

t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

t.statuses.update(status="posting to twitter from pytho9n scriptssss")