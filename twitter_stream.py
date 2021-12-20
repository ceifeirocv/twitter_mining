from tweepy import Stream
# tweepy.streaming import StreamListener
import open_key


class MyListener(Stream):

    def on_data(self, raw_data):
        try:
            with open('python.json', 'a') as f:
                f.write(raw_data.decode()+'\n')
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


twitter_stream = MyListener(
    open_key.consumer_key, open_key.consumer_secret,
    open_key.access_token, open_key.access_secret,
)
twitter_stream.filter(track=['#python'])
