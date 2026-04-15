# Audio Assignment – Sine Wave Generation and Clipping

## Overview
This project generates and processes audio signals using Python.  
It demonstrates how to create a sine wave, apply clipping distortion, and play audio programmatically.

---

## Objectives
- Generate a 1-second sine wave at 440 Hz
- Apply amplitude clipping to create distortion
- Save both signals as WAV files
- Play the clipped audio directly

---

## Technologies Used
- Python
- NumPy
- SciPy (`scipy.io.wavfile`)
- SoundDevice

---

## Project Structure
```
.
├── main.py
├── sine.wav
├── clipped.wav
├── README.md
```

---

## How to Run

### 1. Install Dependencies
```
pip install numpy scipy sounddevice
```

### 2. Run the Program
```
python main.py
```

## Output
- `sine.wav` → clean sine wave  
- `clipped.wav` → clipped/distorted wave  

## Notes
- Sample rate: 48000 Hz  
- 16-bit mono audio  
- Clipping applied at ±8192  
- Sine generated using `sin()`  

## Author
Havirbhavi Pothugunta