from math import acos, degrees
import mediapipe as mp
import numpy as np
import cv2 as cv

mp_utils = mp.solutions.drawing_utils
mp_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv.VideoCapture(0)

def easy_cap():
    while(True):
        _, frame = cap.read()
        frame_rgb = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
        print(frame)
        print(type(frame))
        frame = np.array(frame)
        print(frame)
        print(type(frame))
        cv.imshow('frame', frame_rgb)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

#easy_cap()

with mp_hands.Hands(
        model_complexity=1,
        max_num_hands=2,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as hands:

    while True:
        _, frame = cap.read()
        ht, wd, __ = frame.shape
        frame = cv.flip(frame, 1)
        landmarks = hands.process(cv.cvtColor(frame, cv.COLOR_BGR2RGB))
        if landmarks.multi_hand_landmarks:
            for hand_landmark in landmarks.multi_hand_landmarks:
                mp_utils.draw_landmarks(
                    frame,
                    hand_landmark,
                    mp_hands.HAND_CONNECTIONS,
                    mp_styles.get_default_hand_landmarks_style(),
                    mp_styles.get_default_hand_connections_style()
                )
        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
cv.destroyAllWindows()
