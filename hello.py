#!/usr/bin/env python3
import os
import json

print("Content-Type: application/json")
print()
print(json.dumps(dict(os.environ), indent=2))

# print("Content-Type: text/html")
# print()
# print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")

# print("Content-Type: text/html")
# print()
# print(f"<p>HTTP_USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")

