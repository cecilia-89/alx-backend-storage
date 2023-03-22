#!/usr/bin/env python3
"""Module: 0x002-redis_basic.web"""

import redis
import requests
cache = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """returns count of url being accessed"""
    cache.set('cached:{}'.format(url), count)
    data = requests.get(url)
    cache.incr('count: {}'.format(url))
    cache.setex('cached:{}'.format(url), 10, cache.get(
        'cached:{}'.format(url)))
    return data.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
