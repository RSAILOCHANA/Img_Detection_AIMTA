import streamlit as st
from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np
from ultralytics import YOLO

# FastAPI app
app = FastAPI()

# Load the YOLOv3 model
model = YOLO('yolov3.pt')

@app.post("/detect")
def detect_objects(file: UploadFile = File(...)):
    # Load the image
    img_bytes = file.read()
    img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)

    # Detect objects
    results = model(img)[0].boxes.xyxy.tolist()
    return results

# Streamlit app
st.set_page_config(page_title="Image Detection")
st.title("Image Detection")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Call the FastAPI endpoint to detect objects
    results = st.session_state.get("results", None)
    if results is None:
        results = detect_objects(uploaded_file)
        st.session_state["results"] = results

    # Display the detection results
    st.subheader("Detection Results:")
    st.write(results)

    # Display the image with bounding boxes
    img = cv2.imdecode(np.frombuffer(uploaded_file.getvalue(), np.uint8), cv2.IMREAD_COLOR)
    for x1, y1, x2, y2 in results:
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    st.image(img, use_container_width=True)