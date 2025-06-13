#!/usr/bin/python3
"""
This module provides functionality to fetch posts from an external API and
either print the titles to the console or save all post data to a CSV file.

It uses the 'requests' module for HTTP operations and the 'csv' module
for file writing.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from a placeholder API and prints the titles of each post.

    It prints the HTTP response status code and, if successful (200 OK),
    iterates through each post and prints its 'title' field.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        postsDic = response.json()
        for post in postsDic:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetches posts from a placeholder API and saves them to a CSV file.

    If the response is successful (200 OK), this function:
    - Parses the JSON data from the response.
    - Writes the post data into a CSV file named 'posts.csv' with
      the fields: 'id', 'title', and 'body'.
    Otherwise, it prints the status code.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        postsDic = response.json()
        with open('posts.csv', mode='w', newline='',
                  encoding='utf-8') as csvFile:
            fileData = csv.DictWriter(
                csvFile,
                fieldnames=['id', 'title', 'body'],
                extrasaction='ignore'
            )
            fileData.writeheader()
            for post in postsDic:
                fileData.writerow(post)
    else:
        print("Status Code: {}".format(response.status_code))
