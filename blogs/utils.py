"""
    This will have all the utility files
"""
from .models import Blog
import json


def serialize_obj(blog_obj: Blog) -> json:
    """
        obj: an object of Blog
    """
    res = {
        "id": blog_obj.id,
        "title": blog_obj.title,
        "content": blog_obj.content,
        "timestamp": blog_obj.timestamp
    }
    return res
