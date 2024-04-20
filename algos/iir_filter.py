class IIRFilter:
    r'''N-Order IIR filter
    Assumes working with float samples normalized on [-1, 1]
    ---
    Implementation details:
    Generalize n-order function based on the 2nd-order function from
      https://en.wikipedia.org/wiki/Digital_biquad_filter
    Using the following transfer function
    H(z)=\frac{b_{0}+b_{1}z^{-1}+b_{2}z^{-2}+...+b_{k}z^{-k}}{a_{0}+a_{1}z^{-1}+a_{2}z^{-2}+...+a_{k}z^{-k}}
    we can rewrite this to
    y[n]={\frac{1}{a_{0}}}\left(\left(b_{0}x[n]+b_{1}x[n-1]+b_{2}x[n-2]+...+b_{k}x[n-k]\right)-\left(a_{1}y[n-1]+a_{2}y[n-2]+...+a_{k}y[n-k]\right)\right)
    '''
    def __init__(self, order: int) -> None:
        self.order = order
        self.a_coefs = [1.] + order*[0.]
        self.b_coefs = [1.] + order*[0.]
        self.input_history = order * [0.]
        self.output_history = order * [0.]

    def set_coefs(self, a_coefs: list[float], b_coefs: list[float]) -> None:
        '''Set the coefficients for the IIR filter. These should both be of
        size order + 1.
        a_0 may be left out, and it will use 1.0 as default value.
        This method works well with scipy's filter design functions
            >>> # Make a 2nd-order 1000Hz butterworth lowpass filter
            >>> import scipy.signal
            >>> b_coeffs, a_coeffs = scipy.signal.butter(
                    2, 1000,  btype='lowpass', fs=48000)
            >>> filt = IIRFilter(2)
            >>> filt.set_coefficients(a_coeffs, b_coeffs)
        '''
        pass # TODO
