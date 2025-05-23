"""
Task 3: Create a POST Request Function

Goal:
- Create a function to send data to a server using POST.

Function requirements:
- Name: create_post(title, body, user_id)
- Sends a POST request to https://jsonplaceholder.typicode.com/posts
- Includes the title, body, and userId in the request JSON data
- Returns the server's response data

Expected Output:
{
  "title": "My Homework",
  "body": "I am learning requests!",
  "userId": 1,
  "id": 101
}

Your implementation below:
"""

# Your implementation here
import requests
def create_post(title, body, user_id):
    url=' https://jsonplaceholder.typicode.com/posts'
    response=requests.post(url,json={'body':body,'user_id':user_id,})
    return response.json()
print(create_post('hi',12,'me'))
    