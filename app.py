import os.path
import base64
from io import BytesIO
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
import face_recognition
import cv2
import numpy as np

parser = reqparse.RequestParser()
parser.add_argument('img1_base64', type=str, help='Base64 encoded string for image 1')
parser.add_argument('img2_base64', type=str, help='Base64 encoded string for image 2')

def decode_base64_to_image(base64_string):
    try:
        decoded_image = base64.b64decode(base64_string)
        image_np_array = np.frombuffer(decoded_image, dtype=np.uint8)
        image = cv2.imdecode(image_np_array, cv2.IMREAD_COLOR)
        return image
    except Exception as e:
        raise ValueError(f"Error decoding base64 string: {str(e)}")

def image_compare(img1_base64: str, img2_base64: str) -> bool:
    try:
        img1 = decode_base64_to_image(img1_base64)
        img2 = decode_base64_to_image(img2_base64)

        register_img_encoding = face_recognition.face_encodings(img1)[0]
        scan_img_encoding = face_recognition.face_encodings(img2)[0]

        result = face_recognition.compare_faces([register_img_encoding], scan_img_encoding, tolerance=0.5)
        return result[-1]
    except Exception as e:
        raise ValueError(f"Error comparing images: {str(e)}")

app = Flask(__name__)
api = Api(app)

class FaceRecognitionApi(Resource):
    def post(self):
        args = parser.parse_args()
        img1_base64, img2_base64 = args['img1_base64'], args['img2_base64']
        if not img1_base64 or not img2_base64:
            return {'error': 'Missing base64 encoded strings for images'}, 400
        try:
            predict_result = image_compare(img1_base64, img2_base64)
            return {'result': str(predict_result)}
        except ValueError as e:
            return {'error': str(e)}, 400

api.add_resource(FaceRecognitionApi, '/predict')

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
