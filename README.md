# Real Time Face Recognition using OpenCV and Face_Recognition

This project implements real-time face recognition using OpenCV and the face_recognition library. It identifies known individuals and saves images of unknown faces with a timestamp.

Features

Detects and recognizes faces in real-time using a webcam.

Matches detected faces against a predefined dataset of known faces.

Labels known individuals and highlights them in green.

Saves images of unknown persons in the Unknown_Persons directory with a timestamp.

Unknown faces are marked with a red box.

Press q to exit the application.

Requirements

Ensure you have the following dependencies installed:

pip install opencv-python face-recognition numpy

Installation & Setup

Place your known images in a directory and update the file paths in the script.

Run the script:

python face_recognition.py

Usage

The script will access your webcam and start detecting faces.

If a detected face matches a known face, the corresponding name will be displayed.

If an unknown face is detected, its image will be saved in the Unknown_Persons/ directory with a timestamp.

To stop the program, press q.

Project Structure

realtime-face-recognition/
│-- face_recognition.py  # Main script
│-- Known_Faces/         # Displays a green box around the face with person name
│-- Unknown_Persons/     # Displays a red box around the face with "Unknown". Create a  Directory "Unknown_Persons" where unknown faces are saved with timestamp

Acknowledgments

OpenCV for image processing

face_recognition library by Adam Geitgey

Example Output

Green Box: Known face (Name displayed)

Red Box: Unknown face (Saved to Unknown_Persons/ directory with timestamp)
