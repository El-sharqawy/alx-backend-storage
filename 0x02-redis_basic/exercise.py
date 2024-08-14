#!/usr/bin/env python3
"""Cache Exercise"""

import redis
from typing import Union, Any, Callable, Optional
from functools import wraps
import uuid


class Cache:
    """Cache Class"""

    def __init__(self) -> None:
        """Initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

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
