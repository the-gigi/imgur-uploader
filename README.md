# imgur-uploader
Simple program to upload images to [imgur](http://www.imgur.com).

It uses the pyimgur package to do all the heavy lifting

# Pre-requisites

You need to have an imgur account and a [registered imgur application](http://api.imgur.com/oauth2/addclient) and pass its client ID.

# Usage

    python imgur_uploader.py [--client-id=<Imgur client ID>] [--filename=<file to upload>]


- The client ID can be defined in environment variable IMGUR_CLIENT_ID
- If you don't provide a filename it will upload an iamge from the clipboard
    
