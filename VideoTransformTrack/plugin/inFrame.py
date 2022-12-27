import json
import cv2
import numpy as np
import mediapipe as mp

mp_pose = mp.solutions.pose
pose_image = mp_pose.Pose(static_image_mode=True,
                          min_detection_confidence=0.5)
pose_video = mp_pose.Pose(static_image_mode=False,
                          min_detection_confidence=0.7,
                          min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Points
Nose = mp_pose.PoseLandmark.NOSE.value
Left_Pinky = mp_pose.PoseLandmark.LEFT_PINKY.value
Left_Index = mp_pose.PoseLandmark.LEFT_INDEX.value
Right_Pinky = mp_pose.PoseLandmark.RIGHT_PINKY.value
Right_Index = mp_pose.PoseLandmark.RIGHT_INDEX.value
Left_Ankle = mp_pose.PoseLandmark.LEFT_ANKLE.value
Left_Foot_Index = mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value
Right_Ankle = mp_pose.PoseLandmark.RIGHT_ANKLE.value
Right_Foot_Index = mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value

# Threshold
threshold = 0.7


def inFrame(frames, display=False):
    # frames = np.fromstring(image_text, np.uint8)
    original_image = frames.copy()
    image_in_RGB = cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)
    human = False
    inFrame = False

    resultant = pose_image.process(image_in_RGB)
    if resultant.pose_landmarks:
        human = True
        pointArray = resultant.pose_landmarks.landmark
        if ((pointArray[Nose].visibility > threshold) and (pointArray[Left_Pinky].visibility > threshold or pointArray[Left_Index].visibility > threshold) and (pointArray[Right_Pinky].visibility > threshold or pointArray[Right_Index].visibility > threshold) and (pointArray[Left_Ankle].visibility > threshold or pointArray[Left_Foot_Index].visibility > threshold) and (pointArray[Right_Ankle].visibility > threshold or pointArray[Right_Foot_Index].visibility > threshold)):
            inFrame = True

        mp_drawing.draw_landmarks(image=original_image,
                                  landmark_list=resultant.pose_landmarks,
                                  connections=mp_pose.POSE_CONNECTIONS,
                                  landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255, 255, 255),
                                                                               thickness=2, circle_radius=2),
                                  connection_drawing_spec=mp_drawing.DrawingSpec(color=(49, 125, 237),
                                                                                 thickness=2, circle_radius=2))
        if display:
            original_image = original_image[:, :, ::-1]
    newIMAGE = cv2.putText(original_image, f"Human Detected: {human}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    IMAGE = cv2.putText(newIMAGE, f"Human inFrame: {inFrame}", (10, 55), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return IMAGE, inFrame

