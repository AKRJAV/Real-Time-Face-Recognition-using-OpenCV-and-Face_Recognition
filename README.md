# Real Time Face Recognition using OpenCV and Face_Recognition

This project implements a real-time face recognition system using OpenCV and the `face_recognition` library. The system captures video from a webcam, detects faces, and identifies known individuals. If an unknown person is detected, their image is saved, and a red rectangle with "Unknown" is displayed. The system compares the detected faces with a set of known faces, displaying the name of the person if recognized, and saving the image if the person is not recognized.

## Features
- **Real-Time Face Recognition**: Detects and recognizes faces in real-time from the webcam feed.
- **Known Faces**: Displays the name of the recognized individual with a green rectangle around their face.
- **Unknown Person Detection**: If an unknown person is detected, a red rectangle is shown with the label "Unknown," and their image is saved in the `Unknown_Persons` directory.
- **Image Saving**: Images of unknown individuals are saved with a timestamp for future reference.

## Requirements
Before running the project, ensure you have the following dependencies installed:

- Python 3.x
- OpenCV
- face_recognition

You can install the necessary dependencies using pip:

```bash
pip install opencv-python face_recognition
```

## Usage

1) Place the images of known individuals in the correct paths within the script and update the file paths accordingly.

2) Run the script:
   ```bash
   python face_recognition_system.py
   ```

3) The webcam will start, and the system will begin detecting faces.

* If a known person is in front of the camera, their name will appear on a green rectangle.
* If an unknown person appears, a red rectangle will be shown with "Unknown," and their image will be saved in the Unknown_Persons directory.

4) Press 'q' to stop the program.


## Directory Structure

* Unknown_Persons/: Directory where images of unknown people are saved.
* face_recognition_system.py: Main script for face recognition.
