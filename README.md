# 🧠🖐️ MotionSpeak: Real-Time Hindi Sign Language Recognizer

## 📌 Overview

**MotionSpeak** bridges the communication gap for the hearing and speech-impaired by recognizing Hindi Sign Language in real-time using computer vision and deep learning. The system converts hand gestures into readable text, allowing seamless interaction with non-sign language users.

## 🎯 Goal

To build an affordable and accessible system that enables real-time Hindi Sign Language recognition using just a webcam — no gloves or external sensors needed.

## 🚀 Features

- 🖐️ Recognizes dynamic hand gestures from live webcam feed  
- 🔤 Outputs corresponding Hindi letters/words in real-time  
- 🤖 Powered by deep learning (CNN/LSTM) for robust gesture classification  
- 🌐 Simple and intuitive GUI for ease of use  
- 📈 High accuracy with custom-trained dataset  

## 🛠️ Tech Stack

Language: Python  
Libraries: OpenCV, NumPy, TensorFlow/Keras, Tkinter  
Models: CNN (for spatial features), LSTM (for motion/temporal sequence)  
Hardware: Standard webcam

## 🧠 Model Architecture

- Input: Live video frames  
- Preprocessing: Background subtraction, contour extraction  
- Feature Extraction: CNN  
- Temporal Modeling: LSTM  
- Output: Hindi character prediction  

## 🧪 How to Run

1. Clone the repository:
   git clone https://github.com/harsharora-8/MotionSpeak.git
   cd MotionSpeak

2. Install dependencies:
   pip install -r requirements.txt

3. Run the app:
   python app.py

4. Show hand gestures in front of your webcam and get real-time predictions!

## 🚧 Future Improvements

- Add Text-to-Speech (TTS) output  
- Translate full sign language phrases  
- Create a mobile app (TensorFlow Lite)  
- Add multi-language support (English/ASL)

## 🤝 Contribution

1. Fork the repo  
2. Create a feature branch  
3. Commit and push your changes  
4. Raise a pull request  
5. Get reviewed and merged 🎉

## 🙌 Acknowledgements

- Contributors and testers  
- OpenCV and TensorFlow communities  
- Sign language trainers and educators  

---

Made with 💛 to empower inclusivity through technology.
