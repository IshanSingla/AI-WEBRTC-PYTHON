from av import VideoFrame

def AiortcToCv2(frame):
    """Convert a VideoFrame to a cv2 image."""
    img = frame.to_ndarray(format="bgr24")
    return img

def Cv2ToAiortc(img, frame):
    """Convert a cv2 image to a VideoFrame."""
    new_frame = VideoFrame.from_ndarray(img, format="bgr24")
    new_frame.pts = frame.pts
    new_frame.time_base = frame.time_base
    return new_frame