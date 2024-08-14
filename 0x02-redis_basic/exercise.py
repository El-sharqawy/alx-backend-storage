#!/usr/bin/env python3
"""Cache Exercise"""

import redis
from typing import Union, Any, Callable, Optional
from functools import wraps
import uuid


def count_calls(method: Callable) -> Callable:
    """counts the calls"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrap func"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """calls history"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrap func"""
        outputs = method(self, *args, **kwargs)
        name = method.__qualname__
        self._redis.rpush(f"{name}:inputs", str(args))
        self._redis.rpush(f"{name}:outputs", str(outputs))
        return outputs

    return wrapper


class Cache:
    """Cache Class"""

    def __init__(self) -> None:
        """Initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store def"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    @staticmethod
    def get_str(value: bytes) -> str:
        """takes byte and returns str"""
        return str(value)

    @staticmethod
    def get_int(value: bytes) -> int:
        """takes byte and returns str"""
        return int(value)

    def get(self, key: str, fn: Optional[Any] = None) -> Any:
        """Getter Function"""
        value = self._redis.get(key)
        if fn:
            if fn == int:
                return self.get_int(value)
            elif fn == str:
                return self.get_str(value)
            else:
                return fn(value)
        return value
