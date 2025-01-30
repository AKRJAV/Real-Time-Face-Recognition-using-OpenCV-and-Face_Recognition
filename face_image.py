import cv2
import face_recognition
import os
from datetime import datetime

# Load known images and encode them
known_image1 = face_recognition.load_image_file(r"jpg_image1_file_path")
known_encoding1 = face_recognition.face_encodings(known_image1)[0]

known_image2 = face_recognition.load_image_file(r"jpg_image2_file_path")
known_encoding2 = face_recognition.face_encodings(known_image2)[0]

known_image3 = face_recognition.load_image_file(r"jpg_image3_file_path")
known_encoding3 = face_recognition.face_encodings(known_image3)[0]

# Initialize known faces and names
known_faces = [known_encoding1, known_encoding2, known_encoding3]
known_names = ["Person1", "Person2", "Person3"]

# Directory to save unknown person images
unknown_dir = "Unknown_Persons"
os.makedirs(unknown_dir, exist_ok=True)

# Initialize webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Find all face locations and encodings in the frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare each face with known faces
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"

        # If a match is found, use the corresponding name
        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]
            color = (0, 255, 0)  # Green for known
        else:
            color = (0, 0, 255)  # Red for unknown

            # Save the frame with the unknown person
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            unknown_image_path = os.path.join(unknown_dir, f"unknown_{timestamp}.jpg")
            cv2.imwrite(unknown_image_path, frame)
            print(f"Saved unknown person image: {unknown_image_path}")

        # Draw a rectangle around the face and display the name
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close any OpenCV windows
video_capture.release()
cv2.destroyAllWindows()