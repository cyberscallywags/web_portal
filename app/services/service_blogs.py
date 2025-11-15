import os

import requests

from models.blog_schema import Blog

# API_BASE = os.getenv("API_BASE", "https://api.cyberscallywags.uk")
API_BASE = os.getenv("API_BASE", "http://localhost:8000")

listings = [
    {
        "id": 1,
        "title": "First Blog Post",
        "content": "This is the content of the first blog post.",
        "author": "Author One",
        "slug": "first-blog-post",
        "excerpt": "This is the excerpt for the first blog post.",
        "published_date": "2023-01-01",
        "featured_image": "http://example.com/first.jpg",
        "tags": ["tag1", "tag2"],
        "read_time": "5 min",
        "status": "published",
        "views": 100,
        "featured": True
    },
    {
        "id": 2,
        "title": "Second Blog Post",
        "content": "This is the content of the second blog post.",
        "author": "Author Two",
        "slug": "second-blog-post",
        "excerpt": "This is the excerpt for the second blog post.",
        "published_date": "2023-02-01",
        "featured_image": "http://example.com/second.jpg",
        "tags": ["tag3", "tag4"],
        "read_time": "7 min",
        "status": "draft",
        "views": 50,
        "featured": False
    },
]


def get_all_blogs() -> list[Blog]:
    # resp = requests.get(f"{API_BASE}/blogs")

    data = {'blogs': listings}
    return data


if __name__ == "__main__":

    lst = get_all_blogs()
    print(f" A blogs in a lst :: {lst}")


