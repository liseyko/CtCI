import binascii
import random


class Codec:
    def __init__(self):
        self.storage = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        key = hex(binascii.crc32(b'longUrl'))[2:]
        while key in self.storage:
            key = hex(binascii.crc32(str.encode(str(random.random()))))[2:]
        self.storage[key] = longUrl
        return "http://tinyurl.com/"+key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl.split('/')[-1]
        return self.storage[key]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
