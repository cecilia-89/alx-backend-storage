#!/usr/bin/env python3
'''Writing strings to Redis'''
import redis
import uuid
from typing import Callable, Union
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """returns count of method call"""
    @wraps(method)
    def count(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return count

class Cache:
    """Redis class"""

    def __init__(self) -> None:
        """constructor mehtod"""
        self._redis = redis.Redis()
        self._redis.flushdb()


    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores the input in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


    def get(self, key: str, fn: Callable = None) -> any:
        """converts data back to the specified format"""
        result = self._redis.get(key)
        if fn is not None:
            return fn(result)
        return result

    def get_str(self, key: str) -> int:
        """converts data to an int"""
        return int(self._redis.get(key))

    def get_int(self, key: str) -> str:
        """converts data to a string"""
        return self._redis.get(key).decode("utf-8")
