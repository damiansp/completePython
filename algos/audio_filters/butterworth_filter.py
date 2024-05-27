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
    cosw, a0, a1, a2 = _get_common_coefs(freq, sample_rate, q_factor)
    b1 = 1 - cosw
    b0 = b1 / 2
    filt = IIRFilter(2)
    filt.set_coefs([a0, a1, a2], [b0, b1, b0])
    return filt


def make_highpass(
        freq: int, sample_rate: int, q_factor: float = 1/sqrt(2)) -> IIRFilter:
    '''Creates a high-pass filter
    >>> filter = make_highpass(1000, 48000)
    >>> filter.a_coeffs + filter.b_coeffs  # doctest: +NORMALIZE_WHITESPACE
    [1.0922959556412573, -1.9828897227476208, 0.9077040443587427,
     0.9957224306869052, -1.9914448613738105, 0.9957224306869052]
    '''
    cosw, a0, a1, a2 = _get_common_coefs(freq, sample_rate, q_factor)
    b0 = (1 + cosw) / 2
    b1 = -1 - cosw
    filt = IIRFilter(2)
    filt.set_coefs([a0, a1, a2], [b0, b1, b0])
    return filt


def make_bandpass(
        freq: int, sample_rate: int, q_factor: float = 1/sqrt(2)) -> IIRFilter:
    '''Creates a band-pass filter
    >>> filter = make_bandpass(1000, 48000)
    >>> filter.a_coeffs + filter.b_coeffs  # doctest: +NORMALIZE_WHITESPACE
    [1.0922959556412573, -1.9828897227476208, 0.9077040443587427,
     0.06526309611002579, 0, -0.06526309611002579]
    '''
    cosw, a0, a1, a2 = _get_common_coefs(freq, sample_rate, q_factor)
    b0 = sinw / 2
    b1 = 0
    b2 = -b0
    filt = IIRFilter(2)
    filt.set_coefs([a0, a1, a2], [b0, b1, b2])
    return filt


def make_allpass():
    pass


def _get_common_coefs(freq: int, sample_rate: int, q_factor: float):
    w0 = tau * freq / sample_rate
    sinw = sin(w0)
    cosw = cos(w0)
    alpha = sinw / (2 * q_factor)
    a0 = 1 + alpha
    a1 = -2 * cosw
    a2 = 1 - alpha
    return cosw, a0, a1, a2
    
                 

