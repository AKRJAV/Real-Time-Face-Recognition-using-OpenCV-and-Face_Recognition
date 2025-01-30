# Real Time Face Recognition using OpenCV and Face_Recognition

# Real-Time Face Recognition System

This project implements a real-time face recognition system using OpenCV and the `face_recognition` library. The system captures video from a webcam, detects faces, and identifies known individuals. If an unknown person is detected, their image is saved, and a red rectangle with "Unknown" is displayed.

## Features
- **Real-Time Face Recognition**: Detects and recognizes faces in real-time from the webcam feed.
- **Known Faces**: Displays the name of the recognized individual with a green rectangle around their face.
- **Unknown Person Detection**: If an unknown person is detected, a red rectangle is shown with the label "Unknown," and their image is saved in the `Unknown_Persons` directory.
- **Image Saving**: Images of unknown individuals are saved with a timestamp for future reference.
- **Easy Setup**: Simple integration with pre-encoded known faces.

## Requirements
- Python 3.x
- OpenCV
- face_recognition

You can install the necessary dependencies using pip:

```bash
pip install opencv-python face_recognition
Usage
Place the images of known individuals in the correct paths within the script and update the file paths accordingly.
Run the script:
bash
Copy
Edit
python face_recognition_system.py
The webcam will start, and the system will begin detecting faces.
If a known person is in front of the camera, their name will appear on a green rectangle.
If an unknown person appears, a red rectangle will be shown with "Unknown," and their image will be saved in the Unknown_Persons directory.
Press 'q' to stop the program.
Directory Structure
Unknown_Persons/: Directory where images of unknown people are saved.
face_recognition_system.py: Main script for face recognition.
Contributing
Feel free to fork the repository and submit pull requests if you have improvements or fixes!

License
This project is licensed under the MIT License - see the LICENSE file for details.

sql
Copy
Edit

This single README provides a detailed overview of the project with installation instructions, features, and usage all in one place.

2/2

You said:
again same thing you asshole write everything in 1 prompt response
ChatGPT said:
ChatGPT
I understand now. Here's the complete README in one single prompt:

markdown
Copy
Edit
# Real-Time Face Recognition System

This project implements a real-time face recognition system using OpenCV and the `face_recognition` library. The system captures video from a webcam, detects faces, and identifies known individuals. If an unknown person is detected, their image is saved, and a red rectangle with "Unknown" is displayed.

## Features
- **Real-Time Face Recognition**: Detects and recognizes faces in real-time from the webcam feed.
- **Known Faces**: Displays the name of the recognized individual with a green rectangle around their face.
- **Unknown Person Detection**: If an unknown person is detected, a red rectangle is shown with the label "Unknown," and their image is saved in the `Unknown_Persons` directory.
- **Image Saving**: Images of unknown individuals are saved with a timestamp for future reference.
- **Easy Setup**: Simple integration with pre-encoded known faces.

## Requirements
- Python 3.x
- OpenCV
- face_recognition

You can install the necessary dependencies using pip:

```bash
pip install opencv-python face_recognition
Usage
Place the images of known individuals in the correct paths within the script and update the file paths accordingly.
Run the script:
bash
Copy
Edit
python face_recognition_system.py
The webcam will start, and the system will begin detecting faces.
If a known person is in front of the camera, their name will appear on a green rectangle.
If an unknown person appears, a red rectangle will be shown with "Unknown," and their image will be saved in the Unknown_Persons directory.
Press 'q' to stop the program.
Directory Structure
Unknown_Persons/: Directory where images of unknown people are saved.
face_recognition_system.py: Main script for face recognition.
C
