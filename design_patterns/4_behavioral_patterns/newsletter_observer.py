def main():
    pub = NewsletterPublisher()
    a = Subscriber('Alice')
    b = Subscriber('Bob')
    c = Subscriber('Charlie')
    pub.subscribe(a)
    pub.subscribe(b)
    pub.subscribe(c)
    pub.add_news('Spotted owl spotted')
    pub.unsubscribe(b)
    pub.add_news("It's the end of the world as we know it.")
    

class NewsletterPublisher:
    def __init__(self):
        self._subscribers = []
        self._latest_news = ''

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify(self):
        for subscriber in self._subscribers:
            subscriber.update(self._latest_news)

    def add_news(self, news):
        self._latest_news = news
        self.notify()


class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f'{self.name} received news: {news}')
        

if __name__ == '__main__':
    main()
