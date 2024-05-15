'''Create 2nd-order IIR filters with Butterworth design.
Code based on
https://webaudio.github.io/Audio-EQ-Cookbook/audio-eq-cookbook.html
Alternatively you can use scipy.signal.butter, which should yield the same
results.
'''
from math import cos, sin, sqrt, tau

from audio_filters.iir_filter import IIRFilter


def make_lowpass(
        freq: int, sample_rate: int, q_factor: float = 1/sqrt(2)) -> IIRFilter:
    '''Create a low-pass filter
    >>> filter = make_lowpass(1000, 48000)
    >>> filter.a_coeffs + filter.b_coeffs  # doctest: +NORMALIZE_WHITESPACE
    [1.0922959556412573, -1.9828897227476208, 0.9077040443587427,
     0.004277569313094809, 0.008555138626189618, 0.004277569313094809]
    '''
    w0 = tau * freq / sample_rate
    sinw = sin(w0)
    cosw = cos(w0)
    alpha = sinw / (2 * q_factor)
    b1 = 1 - cosw
    b0 = b1 / 2
    a0 = 1 + alpha
    a1 = -2 * cosw
    a2 = 1 - alpha
    filt = IIRFilter(2)
    filt.set_coefs([a0, a1, a2], [b0, b1, b0])
    return filt


def make_highpass():
                 

