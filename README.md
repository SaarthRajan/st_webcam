# st_webcam - Effortless webcam integration for computer vision projects with Streamlit.

## What is st_webcam?
st_webcam is a Python package designed to simplify computer vision projects, providing an easy-to-use interface for common computer vision tasks, such as accessing and displaying webcam feeds, applying basic image processing techniques, and integrating with popular libraries like OpenCV and Streamlit. It is perfect for anyone who wants to get started quickly with computer vision applications without dealing with the complexities of managing camera devices and frame handling.

## Features
WebCam Class: Easily integrate and control webcam feeds from various sources.
Streamlit Integration: Seamlessly display webcam feeds in Streamlit apps.
Image Processing: Provides a simple interface for processing frames captured from the webcam.
Multi-WebCam Support: Support for multiple webcams with different indexes.
Lightweight and Easy to Use: Simple class-based structure, perfect for beginners and prototyping.

## How to install st_webcam?
run the following command `pip install st-webcam`

## Setup your project in Streamlit
Import the libraries by using

```python
import streamlit as st
from st-webcam import WebCam
```
After writing your code, run the following command to see the streamlit app
`streamlit run main.py` where main.py is your python file

## Usage Examples

### Default Usage
```python
# Create a WebCam object
webcam = WebCam()

# If the webcam is started, capture and display frames
frames = webcam.start()

# Ensure frames is not None before trying to iterate
if frames: 
    for frame in frames:
        webcam.display_frame(frame) # Display frames for webcam

# Stop the webcam when done
webcam.stop()
```

### Use Grayscale
```python
def convert_grayscale(frame):
    return cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

# Initialize WebCam instance for webcam 0
webcam = WebCam(index=0)

# Start capturing frames
frames = webcam.start()

# Display frames with grayscale conversion
if frames:
    for frame in frames:
        webcam.display_frame(frame, frame_func=convert_grayscale)

# Stop the webcam feed once done
webcam.stop()
```

### Multiple Displays with different effects
```python
def apply_canny_edge_detection(frame):
    # Convert the frame to grayscale (Canny edge detection works on grayscale images)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    
    # Apply Canny edge detection
    edges = cv2.Canny(gray_frame, 100, 200)
    
    # Convert the edges to RGB for display in Streamlit
    edges_rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    
    return edges_rgb

def apply_cartoon_effect(frame):
    # Apply bilateral filter to smooth the image while preserving edges
    bilateral_filtered_frame = cv2.bilateralFilter(frame, d=9, sigmaColor=75, sigmaSpace=75)
    
    # Convert to grayscale for edge detection
    gray_frame = cv2.cvtColor(bilateral_filtered_frame, cv2.COLOR_RGB2GRAY)
    
    # Apply median blur to the grayscale frame to reduce noise
    blurred_gray = cv2.medianBlur(gray_frame, 7)
    
    # Apply adaptive thresholding to detect edges
    cartoon_edges = cv2.adaptiveThreshold(blurred_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                          cv2.THRESH_BINARY, blockSize=9, C=9)
    
    # Convert the original frame to RGB (for color effect)
    cartoon_frame = cv2.bitwise_and(bilateral_filtered_frame, bilateral_filtered_frame, mask=cartoon_edges)
    
    return cartoon_frame

def apply_sobel_edge_detection(frame):
    # Convert the frame to grayscale (Sobel works on grayscale images)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    
    # Apply Sobel operator in the X direction (horizontal edges)
    sobel_x = cv2.Sobel(gray_frame, cv2.CV_64F, 1, 0, ksize=3)
    
    # Apply Sobel operator in the Y direction (vertical edges)
    sobel_y = cv2.Sobel(gray_frame, cv2.CV_64F, 0, 1, ksize=3)
    
    # Combine both X and Y gradients to get the final edge image
    sobel_edges = cv2.magnitude(sobel_x, sobel_y)
    
    # Convert to uint8 and back to RGB for display
    sobel_edges = cv2.convertScaleAbs(sobel_edges)
    sobel_edges_rgb = cv2.cvtColor(sobel_edges, cv2.COLOR_GRAY2RGB)
    
    return sobel_edges_rgb

# Initialize WebCam instance for webcam 0
webcam = WebCam(index=0, label="Cartoon")

# Start capturing frames if webcam is running
frames = webcam.start()

placeholder1 = st.empty()
placeholder2 = st.empty()

# Display frames in Streamlit if available
if frames:
    for frame in frames:
        webcam.display_frame(frame, apply_canny_edge_detection)
        webcam.display_frame(frame, apply_cartoon_effect, placeholder1)
        webcam.display_frame(frame, apply_sobel_edge_detection, placeholder2)
        
# Stop the webcam feed once done
webcam.stop()
```

## Development
Feel free to fork the project, contribute, or create an issue for any bugs or new features you'd like to see. If you're interested in collaborating, please follow the standard GitHub contribution workflow: fork, clone, create a branch, and submit a pull request.

## License
st_webcam is licensed under the MIT License. See the License file for more details.
