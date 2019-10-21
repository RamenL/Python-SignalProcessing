import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal
from scipy import fftpack

plt.figure()
f = 1000 #16-1000
a = 25 #0-25
a_mod = pow(a, 3/2)
t = np.linspace(0, 0.05, num=256)
sig_original = a_mod * np.sin(2*np.pi*f*t) + math.sqrt(3.7)
sig_quantize = a_mod * np.sin(2*np.pi*f*t) + math.sqrt(3.7)
sig_error = a_mod * np.sin(2*np.pi*f*t) + math.sqrt(3.7)

plt.plot(t, sig_original, label='Original Signal')

for x in range(len(sig_original)):
    sig_quantize[x] = round(sig_quantize[x]) #quantizer

plt.step(t, sig_quantize, label='Quantized Signal')


for x in range(len(sig_original)):
    sig_error[x] = sig_original[x] -  sig_quantize[x]

plt.plot(t, sig_error, label='Error')

plt.legend()
plt.show()

t_pow = np.linspace(0, 0.05, num=4096)
sig_power_spectra = a_mod * np.sin(2*np.pi*f*t_pow) + math.sqrt(3.7)
a, Pxx_spec = signal.periodogram(sig_power_spectra, 4096, 'flattop', scaling='spectrum')
plt.semilogy(a, np.sqrt(Pxx_spec))
plt.ylim([1e-7, 1e3])
plt.xlabel('frequency [Hz]')
plt.ylabel('Linear spectrum [V RMS]')
plt.show()

# noise floor
# https://dsp.stackexchange.com/questions/19448/why-does-d-a-quantization-error-result-in-a-noise-floor-from-a-physics-perspecti