from tweepy import Stream
import open_key


class IDPrinter(Stream):

    def on_data(self, raw_data):
        print(raw_data)
        with open('python_sample.json', 'a') as f:
            f.write(raw_data.decode('UTF-8'))
            return True

    def on_status(self, status):
        print(status.id)


twitter_stream = IDPrinter(
    open_key.consumer_key, open_key.consumer_secret,
    open_key.access_token, open_key.access_secret
)
twitter_stream.sample()
