#!/usr/bin/python3
"""
Module to fetch and process data from
JSONPlaceholder API using requests library.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints their titles.
    Prints the status code of the response.
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    # Fetch data from the API
    response = requests.get(url)

    # Print the status code
    print(f"Status Code: {response.status_code}")

    # If request was successful, parse and print titles
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them to a CSV file.
    The CSV file contains columns: id, title, and body.
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    # Fetch data from the API
    response = requests.get(url)

    # If request was successful, structure data and save to CSV
    if response.status_code == 200:
        posts = response.json()

        # Structure data as list of dictionaries
        posts_data = []
        for post in posts:
            posts_data.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })

        # Write to CSV file
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header
            writer.writeheader()

            # Write data rows
            writer.writerows(posts_data)

        print("Posts saved to posts.csv")


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
