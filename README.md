# imgur-uploader
Simple program to upload images to [imgur](http://www.imgur.com).

It uses the pyimgur package to do all the heavy lifting

# Pre-requisites

You need to have an imgur account and a [registered imgur application](http://api.imgur.com/oauth2/addclient) and pass its client ID.

# Usage

```
# pipenv run python imgur_uploader.py [--client-id=<Imgur client ID>] [image files to upload]
```

It will print the filenames and corresponding URLs of the uploaded images.
If you don't provide any filename it will upload an image from the clipboard
and print its URL.

The client ID can be defined in environment variable IMGUR_CLIENT_ID


# Reference

[Imgur API auth](https://apidocs.imgur.com/?version=latest#authorization-and-oauth)

[Imgur account | get images](https://apidocs.imgur.com/?version=latest#ee366f7c-69e6-46fd-bf26-e93303f64c84)

