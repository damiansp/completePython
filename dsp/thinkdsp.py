import numpy as np


def CosSignal(
        freq: float = 440, amp: float = 1., offset: float = 0.) -> Sinusoid:
    '''Makes a cosine Sinusoid.
    Parameters:
    - freq: frequency in Hz
    - amp: amplitude, 1.0 is nominal max
    - offset: phase offset in radians
    '''
    return Sinusoid(freq, amp, offset, func=np.cos)


class Signal:
    'Represents a time-varying signal'
    def __add__(self, other: Signal) -> Signal:
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

    def plot(self, framerate int = 11025) -> None:
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
            framerate: int = 11025) -> Wave:
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


class SumSignal(Signal):
    'Represents the sum of signals'
    def __init__(self, *args):
        '''Initialize the sum
        Parameters:
        - args: tuple of Signals
        '''
        self.signals = signals

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
    
        
class Sinusoid(Signal):
    pass


class Wave:
    'Represents a discrete-time waveform'
    # HERE
