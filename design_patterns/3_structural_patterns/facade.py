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
