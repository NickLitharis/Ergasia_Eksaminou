from __future__ import unicode_literals
import pafy


def AudioDownloader(url):

    # Me me tin methodo new kai thn getbestaudio katebazoume tin kaliteri poiotita ixou apo to YouTube
    pafy.new(url).getbestaudio().download()


print("Welcome to our download manager!!!")
AudioDownloader(url=input("Please enter the url:"))