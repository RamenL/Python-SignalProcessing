import numpy as np
import matplotlib.pyplot as plt

from scipy import fftpack
from scipy import signal

f_s = 8500
t = np.linspace(0, 2, 2 * f_s, endpoint=False)

a1 = 5 # 2-5
f1 = 60 #20-60
x1 = a1 * np.sin(f1 * 2 * np.pi * t)

a2 = 10 #7-10
f2 = 240 #150-240
x2 = a2 * np.sin(f2 * 2 * np.pi * t)

a3 = 15 #12-15
f3 = 900 #700-900
x3 = a3 * np.sin(f3 * 2 * np.pi * t)

x_t = x1 + x2 + x3

x_fft = fftpack.fft(x_t)
freqs = fftpack.fftfreq(len(x_t)) * f_s

plt.figure()
#plt.plot(t, x_t) #part 1
#plt.stem(freqs, np.abs(x_fft), use_line_collection=True) #part 2
#plt.xlim(0, 4300)



fs = 8500       # Sample rate, Hz
cutoff = 100    # Desired cutoff frequency, Hz
trans_width = 75  # Width of transition from pass band to stop band, Hz
numtaps = 400      # Size of the FIR filter.
taps = signal.remez(numtaps, [0, cutoff, cutoff + trans_width, 0.5*fs], [1, 0], Hz=fs)
w, h = signal.freqz(taps, [1], worN=1024)
remez_filter = 0.5*fs*w/np.pi
remez_y = 20*np.log10(np.abs(h))
#plt.plot(remez_filter, remez_y) #part 3

filtered = signal.convolve(x_t, remez_filter, mode='same')
#plt.plot(filtered) #part 4

filter_fft = fftpack.fft(remez_filter)
filter_freqs = fftpack.fftfreq(len(remez_filter)) * fs
#plt.stem(filter_freqs, np.abs(filter_fft), use_line_collection=True)
#plt.xlim(-150, 4300) #part 5

convolve_fft = fftpack.fft(filtered)
convolve_freqs = fftpack.fftfreq(len(filtered)) * fs
plt.stem(convolve_freqs, np.abs(convolve_fft), use_line_collection=True)
plt.xlim(-150, 4300) #part 6



plt.show()