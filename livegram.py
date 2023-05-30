#-------------------------SAR Highperformance-----------------------
#------------------------Spectrogram Generator----------------------

import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from scipy import signal


# Set the audio parameters
RATE = 44100
CHUNK = 1024
DURATION = 0.1
MAX_FRAMES = 500

# Initialize PyAudio and open the audio stream
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK
)

# Create the figure and axes for the plot
fig, ax = plt.subplots()

# Function to update the spectrogram
def update_spectrogram(frame):
    audio_array = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    frequencies, times, Sxx = signal.spectrogram(audio_array, RATE)
    ax.clear()
    ax.pcolormesh(times, frequencies, 10 * np.log10(Sxx), shading='auto', cmap='inferno')
    ax.set_ylabel('Frequency [Hz]')
    ax.set_xlabel('Time [s]')
    ax.set_title('Spectrogram')
    return ax,


# Create the animation
ani = animation.FuncAnimation(fig, update_spectrogram, frames=None, interval=DURATION * 1000, blit=True, save_count=MAX_FRAMES)

# Show the plot
plt.show()

# Save the animation as a GIF file
ani.save('live_spectrogram.gif', writer=PillowWriter(fps=24))

# Close the audio stream
stream.stop_stream()
stream.close()
p.terminate()