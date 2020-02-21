import os
import shutil
import requests
import secrets


class Colorize:
    def __init__(self, args):
        if args.source is not None:
            self.source = args.source
        else:
            self.source = os.path.join(os.getcwd(), 'source')

        if args.destination is not None:
            self.destination = args.destination
        else:
            self.destination = os.path.join(os.getcwd(), 'result')

        for file in os.listdir(self.source):
            if self.is_local_file(self.source):
                r = requests.post(
                    secrets.API_URL,
                    files={
                        'image': open(os.path.join(self.source, file), 'rb')
                    },
                    headers={'api-key': secrets.API_KEY}
                )
            else:
                r = requests.post(
                    secrets.API_URL,
                    data={
                        'image': file
                    },
                    headers={'api-key': secrets.API_KEY}
                )

            url = r.json()['output_url']
            image_name = url.split('/')[4] + "." + url.split('/')[6].split('.')[1]
            response = requests.get(url, stream=True)

            try:
                os.stat(self.destination)
            except FileNotFoundError:
                os.mkdir(self.destination)

            with open('%s/%s' % (self.destination, image_name), 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response

    @staticmethod
    def is_local_file(path):
        if path.startswith("http"):
            return False
        return True
