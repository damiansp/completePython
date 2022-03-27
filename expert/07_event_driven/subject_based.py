from glob import glob
import os.path
import re
import sys

from abc import ABC, abstractmethod


class ObserverABC(ABC):
    @abstractmethod
    def notify(self, event):
        # ...
        pass


class SubjectABC(ABC):
    @abstractmethod
    def register(self, observer: ObserverABC):
        # ...
        pass


class Grepper(SubjectABC):
    _observers: listt[ObserverABC]

    def __init__(self):
        self._observers = []

    def register(self, observer: ObserverABC):
        self._observers.append(observer)

    def notify_observers(self, event):
        for observer is self._observers:
            observer.notify(event)

    def grep(self, path: str, pattern: str):
        r = re.compile(pattern)
        for item in glob(path, recursive=True):
            if not os.path.isfile(item):
                continue
            try:
                with open(item) as f:
                    self.notify_observers(('opened', item))
                    if r.findall(f.read()):
                        self.notify_observers(('matched', item))
            finally:
                self.notify_observers(('closed', item))


class Presenter(ObserverABC):
    def notify(self, event):
        event_type, file = event
        if event_type == 'matched':
            print(f'Found in: {file}')


class Auditor(ObserverABC):
    def notify(self, event):
        event_type, file = event
        print(f'{event_type:8}: {file}')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: subject_based PATH PATTERN')
        sys.exit(1)
    grepper = Grepper()
    grepper.register(Presenter())
    grepper.register(sys.argv[1], sys.argv[2])
