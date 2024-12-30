# st-webcam
## Effortless webcam integration for computer vision projects with Streamlit

st-webcam is a Python package designed to simplify computer vision projects, providing an easy-to-use interface for common computer vision tasks, such as accessing and displaying webcam feeds, applying basic image processing techniques, and integrating with popular libraries like OpenCV and Streamlit. It is perfect for anyone who wants to get started quickly with computer vision applications without dealing with the complexities of managing camera devices and frame handling.

This package contains WebCam, which is a Python class designed to make webcam integration with Streamlit simple and effective. It abstracts away the complexity of accessing and managing webcam feeds, allowing you to focus on building computer vision applications. Whether you're prototyping a computer vision project, experimenting with real-time image processing, or just need a straightforward webcam interface, WebCam offers an easy-to-use solution.

## Show Your Support

If you find this template useful, please consider giving it a ⭐ on GitHub! It helps others discover this project and lets me know you’re interested.

[Star this repository](https://github.com/SaarthRajan/st_webcam)

## Features

**WebCam Class:** Easily integrate and control webcam feeds from various sources.

**Simple Webcam Control:** Easily start and stop webcam feeds.

**Real-time Display:** Stream webcam frames in real time within Streamlit apps.

**Custom Frame Processing:** Apply custom image processing (e.g., filters, effects) to webcam frames before displaying them.

**Multi-Webcam Support:** Manage multiple webcams by specifying different device indexes.

**Session State Management:** Leveraging Streamlit’s session state to handle webcam states and resources efficiently.

**Lightweight & Beginner-Friendly:** Easy-to-understand class-based structure designed for prototyping and learning.

## Install st-webcam?

Run the following command to install dependencies. 

```python
pip install st-webcam
```

## Quick Start

Import necessary libraries. 

```python
import streamlit as st
from st_webcam import WebCam
# import other required libraries for your project
```
Run the following command to start your streamlit app. 

```python
streamlit run app.py
```

Where app.py is your Python script that contains the code to display the webcam feed.

## Methods

### __init__(self, index=0, label=None)

**Purpose**
1. Initializes the WebCam object with default or provided webcam index and label. 
2. Initializes the session state for controlling the webcam feed.
3. Provides Start/Stop buttons for the webcam feed in the Streamlit interface

**Arguements**
- index (int, optional): The index of the webcam device (default is 0).
- label (str, optional): The label for the webcam that will be displayed in the control button (default is "Webcam #index", where 'index' is the webcam device index).

**Example**
webcam = WebCam(index=1, label="Custom")

### start(self, index=None)

**Purpose**
Starts the webcam feed and initializes the VideoCapture object.

**Arguements**
- index (int, optional): The index of the webcam device (default is self.index).

**Example**
webcam.start(index=1)

### stop(self)

**Purpose**
This method releases the webcam resources, clears session state variables, and resets the webcam to a stopped state. If the webcam is not running, it does nothing.

**Example**
- webcam.stop()

### display_frame(self, frame, frame_func=None, frame_placeholder=None)

**Purpose**
Displays the provided frame in the Streamlit interface. Can apply a function before displaying. 

**Arguements**
 - frame (ndarray): The frame to be displayed.
 - frame_func (function, optional): A function to apply additional processing to the frame.
 - frame_placeholder (Streamlit placeholder, optional): A placeholder for displaying the frame. Defaults to the instance's placeholder.

**Example**
- webcam.display_frame(frame, frame_func=apply_filter, frame_placeholder=placeholder1)

### For More info on Private Methods, Session States and Identifiers, review the code. 

## Usage Examples

### Default Usage
```python

webcam = WebCam() # webcam object

frames = webcam.start() # before use

if frames: 
    for frame in frames:
        webcam.display_frame(frame)

webcam.stop() # after use
```

### Use Grayscale
```python
import cv2

def convert_grayscale(frame):
    return cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

webcam = WebCam(index=0) # for webcam at index 0

frames = webcam.start()

if frames:
    for frame in frames:
        webcam.display_frame(frame, frame_func=convert_grayscale)

webcam.stop()
```

### Multiple Displays with different effects
```python
def apply_canny_edge_detection(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray_frame, 100, 200)
    edges_rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    return edges_rgb

def apply_cartoon_effect(frame):
    bilateral_filtered_frame = cv2.bilateralFilter(frame, d=9, sigmaColor=75, sigmaSpace=75)
    gray_frame = cv2.cvtColor(bilateral_filtered_frame, cv2.COLOR_RGB2GRAY)
    blurred_gray = cv2.medianBlur(gray_frame, 7)
    cartoon_edges = cv2.adaptiveThreshold(blurred_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                          cv2.THRESH_BINARY, blockSize=9, C=9)
    cartoon_frame = cv2.bitwise_and(bilateral_filtered_frame, bilateral_filtered_frame, mask=cartoon_edges)    
    return cartoon_frame

def apply_sobel_edge_detection(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    sobel_x = cv2.Sobel(gray_frame, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_frame, cv2.CV_64F, 0, 1, ksize=3)
    sobel_edges = cv2.magnitude(sobel_x, sobel_y)
    sobel_edges = cv2.convertScaleAbs(sobel_edges)
    sobel_edges_rgb = cv2.cvtColor(sobel_edges, cv2.COLOR_GRAY2RGB)
    return sobel_edges_rgb
```

```python
webcam = WebCam(index=0, label="Cartoon")

frames = webcam.start()

placeholder1 = st.empty()
placeholder2 = st.empty()

if frames:
    for frame in frames:
        webcam.display_frame(frame, apply_canny_edge_detection)
        webcam.display_frame(frame, apply_cartoon_effect, placeholder1)
        webcam.display_frame(frame, apply_sobel_edge_detection, placeholder2)
        
webcam.stop()
```

## Development
Feel free to fork the project, contribute, or create an issue for any bugs or new features you'd like to see. If you're interested in collaborating, please follow the standard GitHub contribution workflow: fork, clone, create a branch, and submit a pull request.

## License
st-webcam is licensed under the MIT License. See the License file for more details.
