# SAR Highperformance Spectrogram Generator

This repository contains a Python script that generates a real-time spectrogram using the PyAudio and Matplotlib libraries. The script captures audio input from the default microphone and calculates the spectrogram using the Short-Time Fourier Transform (STFT) algorithm.

## Features

- Real-time audio input: The script uses PyAudio to open an audio stream and continuously captures audio data from the default microphone.
- Spectrogram generation: It calculates the spectrogram using the STFT algorithm provided by the `scipy.signal` module. The spectrogram represents the intensity of different frequencies over time and is displayed as a colormap plot.
- Interactive visualization: The Matplotlib library is used to create an animated plot, updating the spectrogram in real-time. The plot is continuously refreshed to display the latest audio input data.

## Requirements

To run the script, make sure you have the following dependencies installed:

- PyAudio: Library for audio input/output.
- NumPy: Library for numerical computing.
- Matplotlib: Library for plotting and visualization.
- SciPy: Library for scientific computing.

## License

This project is licensed under the MIT License, which allows for both personal and commercial use. Feel free to modify and adapt the code to suit your needs.

## Acknowledgments

The script was developed using the PyAudio and Matplotlib libraries, which provide powerful tools for working with audio and generating visualizations. Special thanks to the developers of these libraries for their contributions to the open-source community.
This README.md was generated by CHAT-GPT from recognising the code.