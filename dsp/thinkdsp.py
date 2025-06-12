import copy
import warnings

import numpy as np


DEFAULT_FRAMERATE = 11025


class Signal:
    'Represents a time-varying signal'
    def __add__(self, other):
        '''Add two signals
        Parameters:
        - other: another Signal
        '''
        if other:
            return SumSignal(self, other)
        return self

    __radd__ = __add__

    @property
    def period(self) -> float:
        '''Period of the signal in seconds.
        Since this is used primarily for plotting, the default behavior is to
        retun a value, 0.1s, reasonable for many signals.
        returns: seconds
        '''
        return 0.1

    def plot(self, framerate: int = DEFAULT_FRAMERATE) -> None:
        '''Plots the signal.
        The default is to plot 3 periods.
        Parameters:
        framerate: samples per second
        '''
        duration = 3 * self.period
        wave = self.make_wave(duration, start=0, framerate=framerate)
        wave.plot()

    def make_wave(
            self,
            duration: float = 1.,
            start: float = 0.,
            framerate: int = DEFAULT_FRAMERATE):
        '''Makes a Wave object.
        Parameters:
        - duration: s
        - start: s
        - framerate: frames/s
        '''
        n = round(duration * framerate)
        ts = start + np.arange(n) / framerate
        ys = self.evaluate(ts)
        return Wave(ys, ts, framerate=framerate)


class Sinusoid(Signal):
    pass


def CosSignal(
        freq: float = 440, amp: float = 1., offset: float = 0.) -> Sinusoid:
    '''Makes a cosine Sinusoid.
    Parameters:
    - freq: frequency in Hz
    - amp: amplitude, 1.0 is nominal max
    - offset: phase offset in radians
    '''
    return Sinusoid(freq, amp, offset, func=np.cos)


class SumSignal(Signal):
    'Represents the sum of signals'
    def __init__(self, *args):
        '''Initialize the sum
        Parameters:
        - args: tuple of Signals
        '''
        self.signals = args

    @property
    def period(self) -> float:
        '''Period of the signal in seconds.
        NOTE: this is not correc -- mostly a placekeeper.
        Correc for a harmonic sequencw where all component freqs are multiples
        of the fundamental.
        '''
        return max(sig.period for sig in self.signals)

    def evaluate(self, ts: list[float]):
        '''Evaluate the signal at the given times.
        Parameters:
        - ts: times
        returns: float wave array
        '''
        ts = np.asaarray(ts)
        return sum(sig.evaluate(ts) for sig in self.signals)
    
        
class Wave:
    'Represents a discrete-time waveform'
    def __init__(self, ys: list, ts: list = None, framerate: int = None):
        '''
        Parameters:
        - ys: wave array
        - ts: times
        - framerate: samples/s
        '''
        self.ys = np.asanyarray(ys)
        self.framerate = (
            framerate if framerate is not None else DEFAULT_FRAMERATE)
        if ts is None:
            self.ts = np.arange(len(ys)) / self.framerate
        else:
            self.ts = np.asanyarray(ts)

    def copy(self):
        return copy.deepcopy(self)

    def __len__(self):
        return len(self.ys)

    @property
    def start(self):
        return self.ts[0]

    @property
    def end(self):
        return self.ts[-1]

    @property
    def duration(self) -> float:
        return len(self.ys) / self.framerate

    def __add__(self, other):
        'Add 2 waves elementwise'
        if other == 0:
            return self
        if self.framerate != other.framerate:
            raise ValueError('Frame rates must be equal to add waves')
        # make array of times that covers both waves
        start = min(self.start, other.start)
        end = max(self.end, other.end)
        n = int(round((end - start) * self.framerate)) + 1
        ys = np.zeors(n)
        ts = start + np.arange(n) / self.framerate

        def add_ys(wave):
            i = find_index(wave.start, ts)
            # make sure arrays line up reasonably well
            diff = ts[i] - wave.start
            dt = 1 / wave.framerate
            if (diff/ dt) > 0.1:
                warnings.warn(
                    'Cannot add these waveforms. Time arrays do not line up')
            j = i + len(wave)
            ys[i:j] += wave.ys

        add_ys(self)
        add_ys(other)
        return Wave(ys, ts, self.framerate)

    __radd__ = __add__

    def __or__(self, other):
        '''Concatenates two waves
        Parameters;
        - other (Wave)
        Returns: Wave
        '''
        if self.framerate != other.framerate:
            raise ValueError('Wave.__or__: framerates do not agree')
        ys = np.concatenate((self.ys, other.ys))
        return Wave(ys, framerate=self.framerate)

    def __mul__(self, other):
        '''Elementwise multiplication of two waves
        Note: ignores timestamps; result inherits timestamps from self.
        Parameters:
        - other (Wave)
        Returns: Wave
        '''
        if self.framerate != other.framerate:
            raise ValueError('Frame rates must be equal to add waves')
        if len(self) != len(other):
            raise ValueError('Waves must be of equal lengths to multiply')
        ys = self.ys * other.ys
        return Wave(ys, self.ts, self.framerate)

    def max_diff(self, other) -> float:
        '''Computes maximum absolute difference between two waves.
        Parameters:
        - other (Wave):
        '''
        if self.framerate != other.framerate:
            raise ValueError('Frame rates must be equal to add waves')
        if len(self) != len(other):
            raise ValueError('Waves must be of equal lengths to multiply')
        diffs = np.abs(self.ys - other.ys)
        return np.max(diffs)

    def convolve(self, other):
        pass  # TODO


def find_index(x, xs):
    'Find the index corresponding to a given value in an array'
    n = len(xs)
    start = xs[0]
    end = xs[-1]
    i = round((n - 1) * (x - start)/(end - start))
    return int(i)
        
                                
