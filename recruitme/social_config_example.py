#Production server will have different SITE_URL!!!
SITE_URL='http://localhost:8000'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = SITE_URL
SOCIAL_AUTH_LOGIN_URL = '/'

# Twitter
SOCIAL_AUTH_TWITTER_KEY = 'KEY'
SOCIAL_AUTH_TWITTER_SECRET = 'SECRET'

# Linkedin
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = 'KEY'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'SECRET'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_basicprofile', 'r_emailaddress']
# Add the fields so they will be requested from linkedin.
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = ['email-address', 'headline', 'industry']
# Arrange to add the fields to UserSocialAuth.extra_data
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [('id', 'id'),
                                          ('firstName', 'first_name'),
                                          ('lastName', 'last_name'),
                                          ('emailAddress', 'email_address'),
                                          ('headline', 'headline'),
                                          ('industry', 'industry')]

# Github
SOCIAL_AUTH_GITHUB_KEY = 'KEY'
SOCIAL_AUTH_GITHUB_SECRET = 'SECRET'

#Google Plus
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'KEY'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'SECRET'
