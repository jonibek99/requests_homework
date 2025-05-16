"""
Task 1: Create a GET Request Function

Goal:
- Create a function to get data from a public API.

Function requirements:
- Name: get_post_data(post_id)
- Makes a GET request to https://jsonplaceholder.typicode.com/posts/{post_id}
- Returns a dictionary with the title and body of the post

Expected Output Example (post_id=1):
{
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit suscipit recusandae consequuntur expedita et cum reprehenderit molestiae ut ut quas totam nostrum rerum est autem sunt rem eveniet architecto"
}

Your implementation below:
"""

# Your implementation here
import requests
def  get_post_data(post_id):
  url=f"https://jsonplaceholder.typicode.com/posts/{post_id}"
  a=requests.get(url)
  if a.status_code==200:
    data=a.json()
    return {
      "title":data["title"],
      "body":data["body"],
    }
  else:
    return {'eror'}
print(get_post_data(1))




