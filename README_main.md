# Image Detection App

This application allows users to upload an image and detect objects within it using the YOLOv3 deep learning model. It combines a FastAPI backend for the object detection logic and a Streamlit-based user interface.

## Prerequisites
- Python 3.7 or higher
- Docker
- streamlit

## Installation
1. Clone the repository:
```
git clone https://github.com/RSAILOCHANA/Img_Detection_AIMTA
cd Img_Detection_AIMTA
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage

### Running the Application
1. Start the application:
```
streamlit run app.py --server.filewatcherType=none
```
### Using the App
1. Upload an image by clicking the "Choose an image" button.
2. The app will send the image to the FastAPI backend for object detection.
3. The detected objects and their bounding boxes will be displayed on the image.

## Deployment (using Docker)
1. Build the Docker image:
```
docker build -t img_detection .
```
2. Run your Docker image:
```
docker images #to check image id
docker run image_ID
```
## Code Structure
- `app.py`: Contains both the FastAPI backend and the Streamlit-based user interface.
- `requirements.txt`: Lists the required Python packages.
- `Dockerfile`: Defines the Docker container for the application.

## Troubleshooting
If you encounter any issues, please check the following:
- Ensure you have the required dependencies installed.
- Verify that the YOLOv3 model file (`yolov3.pt`) is present in the project directory.
- Check the terminal output for any error messages.

## Future Improvements
- Add support for more object detection models
- Implement real-time object detection
- Enhance the user interface with additional features
