import re

encoded = '\u202a81.34B\u202c'

decoded = re.sub(r'\\u([0-9a-fA-F]{4})', '', encoded, 2)

print(decoded)