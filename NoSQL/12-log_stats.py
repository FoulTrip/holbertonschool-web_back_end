#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.logs
    nginx = db.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    n_logs = nginx.count_documents({})
    print(f"{n_logs} logs")

    print("Methods:")
    for method in methods:
        count = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    count_status = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{count_status} status check")
