# Cat Face Detection in Video Stream

This script detects cat faces in a video stream using a Haar cascade classifier. Each video frame is resized and converted to grayscale for efficient processing.

## Requirements

- Python 3.x
- OpenCV library

## Installation

1. Install Python 3.x from the [official website](https://www.python.org/downloads/).
2. Install OpenCV by running:

    ```bash
    pip install opencv-python
    ```

3. Download the **Haar cascade classifier** for cat faces:

    You can find the file `haarcascade_frontalcatface.xml` from the [OpenCV GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades).

## How to Run

1. Place your video file (e.g., `cats.mp4`) and the Haar cascade XML file in the same directory as the script.
2. Run the script using Python:

    ```bash
    python cat_face_detector.py
    ```

3. The program will open a video window displaying the video with detected cat faces highlighted by green rectangles.

## Script Overview

1. **`load_cascade(cascade_path)`**:
    - Loads the Haar cascade classifier from the provided path. Throws an error if the file cannot be loaded.
  
2. **`process_frame(frame, cascade, scale_factor)`**:
    - Resizes and converts each video frame to grayscale for processing.
    - Detects cat faces in the frame and draws rectangles around them.

3. **`detect_and_display_faces(video_path, cascade_path, scale_factor)`**:
    - Opens the video file, processes each frame, and displays it with detected cat faces.
    - Terminates the video when the **Esc** key is pressed or the video ends.

## Example

The script detects cat faces in the video file `cats.mp4` using the Haar cascade classifier `haarcascade_frontalcatface.xml`.

```python
if __name__ == '__main__':
    detect_and_display_faces(video_path='cats.mp4', cascade_path='haarcascade_frontalcatface.xml')
