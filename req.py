#!/bin/env python
import base64
msg = "SW4gb3JkZXIgdG8gZ2VuZXJhdGUgdGhlIGludml0ZSBjb2RlLCBtYWtlIGEgUE9TVCByZXF1ZXN0IHRvIC9hcGkvaW52aXRlL2dlbmVyYXRl"
msg='UVNWRVUtVUFWT1gtVEVKUFgtSlRHUkotVllLQlg='
base64_bytes = msg.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

print(message)
