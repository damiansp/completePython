def main():
    chain = ConcreteHandler1(ConcreteHandler2(DefaultHandler()))
    for request in [5, 15, 25]:
        chain.handle_request(request)
        

class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        handled = self._handle(request)
        if not handled and self._successor:
            self._successor.handle_request(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass')


class ConcreteHandler1(Handler):
    def _handle(self, request):
        if 0 < request <= 10:
            print(f'Request {request} handled in handler1')
            return True


class ConcreteHandler2(Handler):
    def _handle(self, request):
        if 10 < request <= 20:
            print(f'Request {request} handled in handler2')
            return True


class DefaultHandler(Handler):
    def _handle(self, request):
        print(f'End of chain, no handler for {request}')
        return True

    
if __name__ == '__main__':
    main()
