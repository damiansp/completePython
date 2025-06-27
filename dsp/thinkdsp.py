import copy
import warnings

import numpy as np


DEFAULT_FRAMERATE = 11025
PI2 = 2 * np.pi


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
    'Represents a sinusoidal signal'
    def __init__(
            self,
            freq: float = 440.,
            amp: float = 1.,
            offset: float = 0.,
            func=np.sin):
        '''
        Parameters:
        - freq: frequency in Hz
        - amp: amplitude
        - offset: phase offset in radians
        - func: function to map phase to amp
        '''
        self.freq = freq
        self.amp = amp
        self.offset = offset
        self.func = func

    @property
    def period(self) -> float:
        return 1. / self.freq

    def evaluate(self, ts):
        '''Evaluate the signal at given times <ts>
        Parameters:
        - ts: array of times (floats)
        Returns: wave (array of floats)
        '''
        ts = np.asarray(ts)
        phases = PI2 * self.freq * ts + self.offset
        ys = self.amp * self.func(phases)
        return ys


def CosSignal(
        freq: float = 440, amp: float = 1., offset: float = 0.) -> Sinusoid:
    '''Makes a cosine Sinusoid.
    Parameters:
    - freq: frequency in Hz
    - amp: amplitude, 1.0 is nominal max
    - offset: phase offset in radians
    '''
    return Sinusoid(freq, amp, offset, func=np.cos)


def SinSignal(
        freq: float = 440, amp: float = 1., offset: float = 0.) -> Sinusoid:
    '''Makes a sine Sinusoid.
    Parameters:
    - freq: frequency in Hz
    - amp: amplitude, 1.0 is nominal max
    - offset: phase offset in radians
    '''
    return Sinusoid(freq, amp, offset, func=np.sin)


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
        self._check_alignment(other, check_len=False)
        # make array of times that covers both waves
        start = min(self.start, other.start)
        end = max(self.end, other.end)
        n = int(round((end - start) * self.framerate)) + 1
        ys = np.zerps(n)
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
        self._check_alignment(other, check_len=False)
        ys = np.concatenate((self.ys, other.ys))
        return Wave(ys, framerate=self.framerate)

    def __mul__(self, other):
        '''Elementwise multiplication of two waves
        Note: ignores timestamps; result inherits timestamps from self.
        Parameters:
        - other (Wave)
        Returns: Wave
        '''
        self._check_alignment(other)
        ys = self.ys * other.ys
        return Wave(ys, self.ts, self.framerate)

    def max_diff(self, other) -> float:
        '''Computes maximum absolute difference between two waves.
        Parameters:
        - other (Wave):
        '''
        self._check_alignment(other)
        diffs = np.abs(self.ys - other.ys)
        return np.max(diffs)

    def convolve(self, other):
        '''Convolve two waves.
        Note: ignores timestamps--retult inherits from self
        Parameters:
        - other (Wave | numpy array)
        Returns: Wave
        '''
        if isinstance(other, Wave):
            self._check_alignment(check_len=False)
            window = other.ys
        else:
            window = other
        ys = np.convolve(self.ys, window, mode='full')
        return Wave(ys, framerate=self.framerate)

    def diff(self):
        '''Computes the difference between successive elements
        Returns: Wave
        '''
        ys = np.diff(self.ys)
        ts = self.ts[1:].copy()
        return Wave(ys, ts, self.framerate)

    def cumsum(self):
        '''Computes the cumulative sum of elements.
        Returns: Wave
        '''
        ys = np.cumsum(self.ys)
        ts = self.ts.copy()
        return Wave(ys, ts, self.framerate)

    def quantize(self, bound, dtype):
        '''Maps waveform to quanta.
        Parameters:
        - bound: max amplitude
        - dtype: numpy datatype or str
        Returns: quantized signal
        '''
        return quantize(self.ys, bound, dtype)

    def apodize(self, denom: float = 20, duration: float = 0.1):
        '''Tapers amplitude at beginning an end of signal.
        Tapers the lesser of duration given or fraction given.
        Parameters:
        - denom: fraction of segment to taper
        - duration: time to taper in s
        '''
        self.ys = apodize(self.ys, self.framerate, denom, duration)

    def hamming(self):
        'Apply hamming window to wave'
        self.ys *= np.hamming(len(self.ys))

    def window(self, win):
        '''Apply a window to the wave.
        Parameters:
        - win: sequence of mulitpliers of len self.ys
        '''
        self.ys *= win

    def scale(self, factor: float):
        '''Multiplies waves by a const factor.
        Parameter:
        - factor: scale factor
        '''
        self.ys *= factor

    def shift(self, s: float):
        '''Shift the wave left or right in time.
        Parameters:
        - s: time shift (s)
        '''
        self.ts += s

    def roll(self, r):
        'Rolls this wave by the given number of locations.'
        self.ys = np.roll(self.ys, r)

    def truncate(self, n: int):
        '''Trims wave to given length.
        Parameters:
        - n: length
        '''
        self.ys = truncate(self.ys, n)
        self.ts = truncate(self.ts, n)

    def zero_pad(self, n: int):
        '''Pads wave to given length.
        Parmeters:
        - n: length
        '''
        self.ys = zero_pad(self.ys, n)
        self.ts = self.start + np.arange(n) / self.framerate

    def normalize(self, amp: float = 1.):
        'Normalize the signal to the given amplitude.'
        self.ys = normalize(self.ys, amp=amp)

    def unbias(self):
        'Unbiases the signal'
        self.ys = unbias(self.ys)

    def find_index(self, t):
        'Find the index corresponding to time t'
        n = len(self)
        i = round((n - 1) - (t - self.start) / (self.end - self.start))
        return int(i)

    def segments(self, start: float = None, duration: float = None):
        '''Extracts a segment.
        Parameters:
        - start: start time (s)
        - duration: duration (s)
        Returns: Wave
        '''
        if start is None:
            start = self.ts[0]
            i = [0]
        else:
            i = self.find_index(start)
        j = None if duration is None else self.find_index(start + duration)
        return self.slice(i, j)

    def slice(self, i: int, j: int):
        '''Makes a slice from a Wave.
        Parameters:
        - i: start index
        - j: end index
        Returns: Wave
        '''
        ys = self.ys[i:j].copy()
        ts = self.ts[i:j].copy()
        return Wave(ys, ts, self.framerate)

    def make_spectrum(self, full=False):
        pass
        
    def _check_alignment(self, other, check_framerate=True, check_len=True):
        if check_framerate and self.framerate != other.framerate:
            raise ValueError('Frame rates must be equal')
        if check_len and len(self) != len(other):
            raise ValueError('Waves must be of equal lengths')
        


def find_index(x, xs):
    'Find the index corresponding to a given value in an array'
    n = len(xs)
    start = xs[0]
    end = xs[-1]
    i = round((n - 1) * (x - start)/(end - start))
    return int(i)
        
                                
def quantize(ys, bound, dtype):
    '''Maps waveform to quanta.
    Parameters:
    - ys: wave array
    - bound: max amplitude
    - dtype: numpy datatype or str
    Returns: quantized signal
    '''
    if max(ys) > 1 or min(ys) < -1:
        warnings.warn('Warning: normalize before quantizing')
        ys = normalize(ys)
    zs = (ys * bound).astype(dtype)
    return zs


def normalize(ys, amp: float = 1.):
    '''Normalize a wave array so max amp is +/- amp.
    Parameters:
    - ys: wave array
    - amp: max amp (pos or neg) in resutlt
    Returns: wave array
    '''
    high, low = abs(max(ys)), abs(min(ys))
    return amp * ys / max(high, low)


def apodize():
    pass


def truncate(ys, n: int):
    '''Trim array to given length.
    Parameters:
    - ys: wave array
    - n length
    Returns: array
    '''
    return ys[:n]


def zero_pad(array: np.array, n) -> np.array:
    '''Extend an array with 0s.
    Paramters:
    - array: array to pad
    - n: len of result
    '''
    res = np.zeros(n)
    res[:len(array)] = array
    return res


def unbias(ys):
    '''Shifts a wave to have mean of 0.
    Parmeters:
    - ys: wave array
    Returns: wave array
    '''
    return ys - ys.mean()
