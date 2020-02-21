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

    def colorize(self):
        counter = 0
        count = len(os.listdir(self.source)) - 1
        print("Colorizing %d images" % count)
        for file in os.listdir(self.source):
            if file == '.keep':
                continue
            counter += 1
            result = self.upload(file, counter, count)
            response = requests.get(result, stream=True)
            self.download(response, file, counter, count)

    def upload(self, file, counter, count):
        print("Uploading: %s - %d/%d" % (file, counter, count))
        r = requests.post(
            secrets.API_URL,
            files={
                'image': open(os.path.join(self.source, file), 'rb')
            },
            headers={'api-key': secrets.API_KEY}
        )

        url = r.json()['output_url']
        return url

    def download(self, response, file, counter, count):
        try:
            os.stat(self.destination)
        except FileNotFoundError:
            os.mkdir(self.destination)

        print("Downloading: %s - %d/%d" % (file, counter, count))
        with open('%s/%s' % (self.destination, file), 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
