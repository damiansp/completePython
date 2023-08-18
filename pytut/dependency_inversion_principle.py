from abc import ABC


class FXConverter1:
    def convert(self, from_currency, to_currency, amt):
        print(f'{amt} {from_currency} -> {1.2 * amt} {to_currency}')
        return 1.2 * amt

class App1:
    def start(self):
        converter = FXConverter1()
        converter.convert('EUR', 'USD', 100)


# Better implementation
class CurrencyConverter(ABC):
    def convert(self, from_currency, to_currency, amt) -> float:
        pass


class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amt) -> float:
        print('Converting currency using FX API')
        print(f'{amt} {from_currency} -> {1.2 * amt} {to_currency}')
        return 1.2 * amt


class App:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        self.converter.convert('EUR', 'USD', 100)


def main():
    app1 = App1()
    app1.start()

    converter = FXConverter()
    app = App(converter)
    app.start()
    
    

if __name__ == '__main__':
    main()
