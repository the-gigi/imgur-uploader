import os
from argparse import ArgumentParser
import pyimgur


CLIENT_ID = os.environ.get('IMGUR_CLIENT_ID', None)


def upload(client_id, filename):
    assert os.path.isfile(filename)
    assert client_id is not None

    im = pyimgur.Imgur(client_id)
    result = im.upload_image(filename)

    return result.link


def main():
    parser = ArgumentParser()
    parser.add_argument('--client-id',
                        required=True,
                        help='Imgur client ID')
    parser.add_argument('--filename',
                        required=True,
                        help='The image file to upload')
    args = parser.parse_args()
    url = upload(args.client_id, args.filename)
    print url


if __name__ == '__main__':
    main()
