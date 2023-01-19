#!/usr/bin/env python3
"""cache class"""
from typing import Union, Callable, Optional
from functools import wraps
import redis
import uuid


class cache:
    def __init__(self):
        """Stores an instanc of the redis client"""
        self._redis = redis.redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes and stores a data argument and returns a string"""
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key
