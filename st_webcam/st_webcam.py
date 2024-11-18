import streamlit as st
import cv2

class WebCam:

    """
    A class that encapsulates the functionality for controlling, modifying and displaying 
    webcam feed using OpenCV and Streamlit.

    Attributes:
    - index (int): The index of the webcam device (default is 0).
    - label (str): The label of the webcam that will be displayed in the button (default is #index)
    - running_key (str): Key used in Streamlit's session state to track if the webcam is running.
    - cap_key (str): Key used in Streamlit's session state to store the VideoCapture object.
    - frame_placeholder (Streamlit placeholder): Placeholder for displaying frames in Streamlit.

    Public Methods:
    - start(): Starts the webcam feed and initializes the video capture.
    - stop(): Stops the webcam feed, releasing the resources.
    - display_frame(): Displays the captured frame in the Streamlit interface.
    """

    def __init__(self, index=0, label=None):
        
        """
        Initializes the WebCam object with default or provided webcam index and label.

        Args:
        - index (int, optional): The index of the webcam device (default is 0).
        - label (str, optional): The label for the webcam that will be displayed in the control button 
        (default is "Webcam #index", where 'index' is the webcam device index).

        Initializes the session state for controlling the webcam feed:
        - webcam_running_{index}: A boolean flag to track the webcam's running status.
        - cap_{index}: The OpenCV VideoCapture object used to capture frames from the webcam.

        Also provides Start/Stop buttons for the webcam feed in the Streamlit interface.

        Example:
        - webcam = WebCam()  # Initializes the webcam with default index 0
        - webcam = WebCam(1, "My Webcam")  # Initializes the webcam with index 1 and custom label
        """
        
        self.index = index # webcam index
        self.running_key = f"webcam_running_{index}" # session key for webcam
        self.cap_key = f"cap_{index}" # Session key for storing VideoCapture object

        # Set webcam label (defaults to "Webcam #index" if not provided)
        if label:
            self.label = label
        else:
            self.label = f" Webcam #{self.index}"

        # Initialize session state for webcam feed if not already initialized
        if self.running_key not in st.session_state:
            st.session_state[self.running_key] = False # Default to not running

        if self.cap_key not in st.session_state:
            st.session_state[self.cap_key] = None # Default to no webcam feed

        # Create control buttons (start/stop webcam)
        self._create_control_buttons()
        
        # Placeholder for displaying webcam frames
        self.frame_placeholder = st.empty()
    
    def start(self, index=None) -> None:

        """
        Starts the webcam feed and initializes the VideoCapture object.

        Args:
        - index (int, optional): The index of the webcam device (default is self.index). 

        Returns:
        - None: If the webcam feed is started successfully. If there is an error, it stops the webcam and 
        displays an error message.

        Example:
        - webcam.start()  # Starts the webcam using the default index
        - webcam.start(1)  # Starts the webcam with index 1
        """

        
        # if webcam is already running
        if st.session_state[self.running_key]:
            # If webcam is already running, return without starting it again
            return None
        
        # if index not provided, use default index
        if not index:
            index = self.index
    
        # start the webcam feed
        st.session_state[self.cap_key] = cv2.VideoCapture(index) # store the capture object
        st.session_state[self.running_key] = True # mark it as running

        if not st.session_state[self.cap_key].isOpened():
            st.error(f"Unable to access webcam at index {index}.")
            self.stop()  # Cleanup if failed
            return None

        # Start capturing frames from the webcam
        return self._capture_frames()
        

    def stop(self):
        """
        Stops the webcam feed and releases the VideoCapture object.

        This method releases the webcam resources, clears session state variables, and resets the webcam 
        to a stopped state. If the webcam is not running, it does nothing.

        Example:
        - webcam.stop()  # Stops the webcam and releases the resources
        """
        if not st.session_state[self.running_key]:
            # If the webcam is not running, exit without stopping
            return

        cap = st.session_state[self.cap_key]
        if cap and cap.isOpened():
            cap.release()  # Release the video capture object
        
        # Close any OpenCV windows
        cv2.destroyAllWindows()

        # Clear session state variables
        del st.session_state[self.cap_key]
        del st.session_state[self.running_key]

        # Mark the webcam as stopped
        st.session_state[self.running_key] = False

    def _capture_frames(self):
        
        """
        Private generator function that continuously captures frames from the webcam.

        Yields:
        - frame_rgb (ndarray): A frame captured from the webcam in RGB format.

        Stops when the webcam feed ends or is manually stopped.
        """

        while st.session_state[self.running_key]:
            ret, frame = st.session_state[self.cap_key].read()

            if not ret:
                st.write(f"Video Capture for webcam {self.index} ended.")
                break
            
            # Convert the frame from BGR to RGB (Streamlit expects RGB format)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Yield the frame for display/processing
            yield frame_rgb

    def display_frame(self, frame, frame_func=None, frame_placeholder=None):
        
        """
        Displays the provided frame in the Streamlit interface. Can apply a function before displaying. 

        Args:
        - frame (ndarray): The frame to be displayed.
        - frame_func (function, optional): A function to apply additional processing to the frame.
        - frame_placeholder (Streamlit placeholder, optional): A placeholder for displaying the frame. Defaults to the instance's placeholder.

        Example:
        - webcam.display_frame(frame)  # Displays a frame using the default placeholder
        - webcam.display_frame(frame, frame_func=apply_filter)  # Displays the frame with processing

        """

        # Use the provided placeholder or default to the instance's frame placeholder 
        if not frame_placeholder:
            frame_placeholder = self.frame_placeholder

        # Apply additional frame processing if a frame function is provided
        if frame_func :
            frame = frame_func(frame)
        
         # Display the processed frame in the Streamlit app
        frame_placeholder.image(frame, use_column_width=True, channels="RGB")

    def _create_control_buttons(self):
        
        """
        Private method to create Start/Stop control buttons for the webcam feed.

        The button toggles the webcam between running and stopped states.
        """

        if st.button(f"Start {self.label}" if st.session_state[self.running_key] else f"Stop {self.label}", type="primary"):
            if st.session_state[self.running_key]:
                self.stop()  # Stop the webcam if it's running
            else:
                self.start()  # Start the webcam if it's not running

