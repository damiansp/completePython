def main():
    amp = Amplifier()
    dvd = DVDPlayer()
    projector = Projector()
    theater = HomeTheaterFacade(amp, dvd, projector)
    theater.watch_movie('Inception')
    

class Amplifier:
    def on(self):
        print('Amp is on')

    def set_volume(self, level):
        print(f'Amp volume: {level}')


class DVDPlayer:
    def on(self):
        print('DVD player is on')

    def play(self, movie):
        print(f'Playing "{movie}"')


class Projector:
    def on(self):
        print('Projector is on')

    def set_input(self, source):
        print(f'Projector input: {source}')


# Facade
class HomeTheaterFacade:
    def __init__(self, amp, dvd, projector):
        self.amp = amp
        self.dvd = dvd
        self.projector = projector

    def watch_movie(self, movie):
        print('Preparing movie...')
        self.amp.on()
        self.amp.set_volume(5)
        self.dvd.on()
        self.projector.set_input('DVD')
        self.dvd.play(movie)


if __name__ == '__main__':
    main()
