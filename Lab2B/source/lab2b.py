import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import chirp
from scipy import fftpack


f = 575  # Frequency, in cycles per second, or Hertz
f_s = 512  # Sampling rate, or number of measurements per second

t = np.linspace(0, 2, 2 * f_s, endpoint=False)
x = np.sin(165 * 2 * np.pi * t) + \
    np.sin(295 * 2 * np.pi * t) + \
    np.sin(512 * 2 * np.pi * t) + \
    chirp(t, f0=700, f1=900, t1=f_s, method='linear')

fig, ax = plt.subplots()
ax.plot(t, x)
ax.set_xlabel('Time [s]')
ax.set_ylabel('Signal amplitude')

# Fourier Transform
f_s = 8000
X = fftpack.fft(x)
freqs = fftpack.fftfreq(len(x)) * f_s
fig, ax = plt.subplots()

ax.stem(freqs, np.abs(X))
ax.set_xlabel('Frequency in Hertz [Hz]')
ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')
ax.set_xlim(0 , f_s/2)
ax.set_ylim(-5, 520)

# Fourier Transform + Oversampling
f_s = 8000000
X = fftpack.fft(x)
freqs = fftpack.fftfreq(len(x)) * f_s
fig, ax = plt.subplots()

ax.stem(freqs, np.abs(X))
ax.set_xlabel('Frequency in Hertz [Hz]')
ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')
ax.set_xlim(0 , f_s/2)
ax.set_ylim(-5, 520)

plt.show() #display plot