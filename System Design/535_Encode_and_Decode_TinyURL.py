#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 19:01:44 2021

@author: jeff
"""

"""
Key Idea:
    Use 6 char from string.ascii_letters + string.digits to encode
    random choice everytime, if it exists then random choice again
"""
class Codec:
    
    url_to_code = {}
    code_to_url = {}
    
    def getCode(self):
        chars = string.ascii_letters + string.digits
        code = "".join(random.choice(chars) for i in range(6))
        return "http://tinyurl.com/" + code
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.url_to_code:
            code = self.getCode()
            while code in self.code_to_url:
                code = getCode()
            self.url_to_code[longUrl] = code
            self.code_to_url[code] = longUrl
        
        return self.url_to_code[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.code_to_url[shortUrl]