# Sound Analysis in vvvv

Part of **RC15 Resources**, the permanent tutorial library for Pervasive Urbanism.

**Software:** vvvv gamma  
**Format:** Example patch  
**Software version:** The patch references vvvv 2023.5.3; compatibility with newer versions has not been verified.  
**Original collection:** 240203_vvvv Sound Analysis

[Browse this topic](../README.md) | [Library home](../../../README.md)

## About this example

Sound can be used as an input to interactive graphics, installations and spatial experiments. This vvvv example explores how an audio signal can be analysed and translated into changing visual parameters.

Open **[240203_Sound Analysis.vl](240203_Sound%20Analysis.vl)** in vvvv and explore its labelled sections. The patch includes three related ideas:

- **Waveform:** a view of how the signal's amplitude changes over time.
- **Frequency analysis (FFT):** a way of examining how the signal is distributed across different frequencies, rather than only tracking its overall volume.
- **Audio-reactive mapping:** using information from the signal, including beat-related analysis, to influence visual behaviour.

Try comparing the response to quiet and loud sounds, or to sustained tones and short, rhythmic sounds. Consider which characteristics of sound are useful to represent, and what kinds of visual relationships they might produce in an interactive environment.

The example uses an audio input and audio-reactive components. It has not yet been checked in a current vvvv installation; microphone access, dependencies and the behaviour of the visual output require a desktop review. See the [editorial backlog](../../../EDITORIAL_BACKLOG.md).
