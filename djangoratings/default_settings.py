from django.conf import settings

# Used to limit the number of unique IPs that can vote on a single object+field.
#   useful if you're getting rating spam by users registering multiple accounts
RATINGS_VOTES_PER_IP = 3

# Is used to determine the duration for:
# a. the cookie expiry date
# b. the length of the rate limiting feature
RATINGS_VOTES_PER_IP_DURATION = 0
