import requests
import json

# Define the API endpoint URL
url = 'http://20.19.62.93:5000/api/predict'

# Define the data payload for the POST request
# You should adjust this dictionary to reflect the structure expected by your Flask API
data = {
    'num_critic_for_reviews': 100,
    'duration': 150,
    'gross': 10000000,
    'num_voted_users': 10000,
    'cast_total_fb_likes': 5000,
    'num_user_for_reviews': 50,
    'budget': 20000000,
    'title_year': 2020,
    'Action': 1,
    'Adventure': 0,
    'Animation': 0,
    'Biography': 0,
    'Comedy': 0,
    'Crime': 0,
    'Documentary': 0,
    'Drama': 0,
    'Family': 0,
    'Fantasy': 0,
    'Film-Noir': 0,
    'Game-Show': 0,
    'History': 0,
    'Horror': 0,
    'Music': 0,
    'Musical': 0,
    'Mystery': 0,
    'News': 0,
    'Reality-TV': 0,
    'Romance': 0,
    'Sci-Fi': 0,
    'Short': 0,
    'Sport': 0,
    'Thriller': 0,
    'War': 0,
    'Western': 0,
    'Europe': 0,
    'North America': 1,
    'Other countries': 0,
    'English': 1,
    'Other language': 0
}

# Send a POST request and get the response
response = requests.post(url, json=data)

# Print the response from the server
print('Status Code:', response.status_code)
print('Response Body:', response.json())
