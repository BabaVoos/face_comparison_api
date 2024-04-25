# Face Recognition API 🕵️

This project implements a Flask API for face recognition using base64 encoded images. The API accepts two base64 encoded images, decodes them, and performs face recognition using the face_recognition library. The comparison result indicates whether the images contain the same person.

## Features :
✔️ Accepts base64 encoded strings for image comparison.

✔️ Utilizes the face_recognition library for facial recognition.

✔️ Provides error handling for missing or invalid input.

## Technologies Used 💻:

✔️ Flask for the server-side API.

✔️ Python libraries including face_recognition and Flask-RESTful.

## Usage:

✔️ Send a POST request to /predict endpoint with base64 encoded images in the request body.

✔️ Receive a JSON response indicating if the images contain the same person.

