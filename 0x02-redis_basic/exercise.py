#!/usr/bin/env python3
""" Module for Redis db """

import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps

"""
Create a Cache class. In the __init__ method,
store an instance of the Redis client as a private variable
named _redis (using redis.Redis())
and flush the instance using flushdb.
Create a store method that takes a data argument and returns a string.
The method should generate a random key (e.g. using uuid),
store the input data in Redis using the random key and return the key.
Type-annotate store correctly.
Remember that data can be a str, bytes, int or float.
"""

unionTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """
    decorator Counts how many times methods
    of Cache class are called
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper of decorator"""
       # key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Stores the history of inputs and outputs for a particular function """
    input_list = method.__qualname__ + ":inputs"
    output_list = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args) -> bytes:
        """ This is wrapper function for call_history method """
        self._redis.rpush(input_list, str(args))
        output = method(self, *args)
        self._redis.rpush(output_list, output)
        return output
    return wrapper


class Cache:
    """classfor operating caching systems"""

    def __init__(self):
        """Instance for redis db"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: unionTypes) -> str:
        """
        method that takes a data argument and returns a string.
        The method should generate a random key (e.g. using uuid),
        store the input data in Redis using the random key and
        return the key.
        """

        key = str(uuid4())
        self._redis.mset({key: data})

        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> unionTypes:
        """
        method that take a key string argument
        and an optional Callable argument named fn.
        This callable will be used to convert the data
        back to the desired format.
        """

        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, data: str) -> str:
        """ get a string """
        return self.get(key, str)

    def get_int(self, data: str) -> int:
        """ get an int """
        return self.get(key, int)
