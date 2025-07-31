import os
import cv2
import numpy as np
import streamlit as st
import mediapipe as mp
import pickle

st.title("Real-Time Hindi Sign Detection in Live Video Stream")

model_dict = pickle.load(open('./model_01.p', 'rb'))
model = model_dict['model']

# Set up OpenCV video capture
cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Create a placeholder for displaying the video stream
with st.container():
    video_placeholder = st.empty()
with st.container():
    text_placeholder = st.empty()

hands = mp_hands.Hands(static_image_mode=False, min_detection_confidence=0.3)

labels_dict = {
    0: 'ए', 1: 'आ', 2: 'ऐ', 3: 'आई', 4: 'अन', 5: 'बा', 6: 'भा', 7: 'च', 8: 'छ', 9: 'द',
    10: 'डा', 11: 'ध', 12: 'धा', 13: 'ए', 14: 'ई', 15: 'फा', 16: 'ग', 17: 'घ', 18: 'ज्ञ',
    19: 'ह', 20: 'हेलो', 21: 'आइलव्ह्यू', 22: 'ज', 23: 'झ', 24: 'क', 25: 'ख', 26: 'ल',
    27: 'ला', 28: 'म', 29: 'न', 30: 'नमस्ते', 31: 'ना', 32: 'ऊ', 33: 'प', 34: 'र',
    35: 'स', 36: 'श', 37: 'षा', 38: 'त', 39: 'थ', 40: 'ठ', 41: 'धन्यवाद', 42: 'ट',
    43: 'उ', 44: 'उउ', 45: 'व', 46: 'य', 47: 'हाँ'
}

while True:
    # Read a frame from the video stream
    data_aux = []
    x_ = []
    y_ = []
    ret, frame = cap.read()

    if not ret:
        st.error("Failed to capture video.")
        break

    H, W, _ = frame.shape

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # MediaPipe Hands model
    results = hands.process(frame_rgb)


    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, 
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y

                x_.append(x)
                y_.append(y)

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))

        x1 = int(min(x_) * W) - 10
        y1 = int(min(y_) * H) - 10

        x2 = int(max(x_) * W) - 10
        y2 = int(max(y_) * H) - 10

        try:
            prediction = model.predict([np.asarray(data_aux[:42])])

            predicted_character = labels_dict[int(prediction[0])]
            text_placeholder.write(f"<div style='text-align: center; font-size: 24px;'>{predicted_character}</div>", unsafe_allow_html=True) ## Display the prediction
        except:
            pass

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)



    # Display the frame with the overlaid text
    video_placeholder.image(frame, channels="BGR", use_column_width=True)

cap.release()
cv2.destroyAllWindows()
