import os
import tempfile
from argparse import ArgumentParser
import pyimgur
from PIL import Image, ImageGrab
from pathlib import Path


CLIENT_ID = os.environ.get('IMGUR_CLIENT_ID', None)


def upload(client_id, filename):
    if filename is None:
        snapshot = ImageGrab.grabclipboard()
        assert isinstance(snapshot, Image.Image)
        filename = str(Path(tempfile.gettempdir()) / 'snaphot.jpg')
        snapshot.save(filename)

    im = pyimgur.Imgur(client_id)
    result = im.upload_image(filename)

    return result.link


def main():
    parser = ArgumentParser()
    parser.add_argument('--client-id',
                        default=CLIENT_ID,
                        help='Imgur client ID')
    parser.add_argument('--filename',
                        help='The image file to upload')
    args = parser.parse_args()
    url = upload(args.client_id, args.filename)
    print(url)


if __name__ == '__main__':
    main()
