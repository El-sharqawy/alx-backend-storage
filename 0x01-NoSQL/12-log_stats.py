#!/usr/bin/env python3
"""Log Stats"""

from pymongo import MongoClient


def LogsStats():
    """Log Stats"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginxLogs = client.logs.nginx

    numLogs = nginxLogs.count_documents({})
    print(f"{numLogs} logs")
    curMethods: list[str] = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in curMethods:
        curMethod: int = nginxLogs.count_documents({"method": method})
        print(f"\tmethod {method}: {curMethod}")

    docsCount: int = nginxLogs.count_documents({"method": "GET", "path": "/status"})
    print(f"{docsCount} status check")


if __name__ == "__main__":
    LogsStats()
