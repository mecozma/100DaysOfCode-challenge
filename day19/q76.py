import zlib


string = "hello world!hello world!hello world!hello world!"
string_to_bites = bytes(string, "utf-8")
compressed = zlib.compress(string_to_bites)
print(compressed)
decompressed = zlib.decompress(compressed)
print(decompressed)
