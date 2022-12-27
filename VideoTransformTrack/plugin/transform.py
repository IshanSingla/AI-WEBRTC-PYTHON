# from .cartoon import cartoon
# from .edges import edges
# from .rotate import rotate
# from .inFrame import inFrame
from .converter import AiortcToCv2, Cv2ToAiortc
from . import rotate, inFrame, edges, cartoon


def transform(frame, transform):

    if transform == "cartoon":

        # convert image to cv2 image
        img = AiortcToCv2(frame)

        # perform cartoonization
        img = cartoon(img)

        # rebuild a VideoFrame, preserving timing information
        new_frame = Cv2ToAiortc(img, frame)

        # send data to client
        return new_frame

    elif transform == "edges":

        # convert image to cv2 image
        img = AiortcToCv2(frame)

        # perform edge detection
        img = edges(img)

        # rebuild a VideoFrame, preserving timing information
        new_frame = Cv2ToAiortc(img, frame)

        # send data to client
        return new_frame

    elif transform == "rotate":

        # convert image to cv2 image
        img = AiortcToCv2(frame)

        # perform rotation
        img = rotate(img, frame.time * 45)

        # rebuild a VideoFrame, preserving timing information
        new_frame = Cv2ToAiortc(img, frame)

        # send data to client
        return new_frame

    elif transform == "inFrame":

        # convert image to cv2 image
        img = AiortcToCv2(frame)

        # detect pose
        img, data = inFrame(img)

        # rebuild a VideoFrame, preserving timing information
        new_frame = Cv2ToAiortc(img, frame)

        # send data to client
        return new_frame

    else:
        # send data to client
        return frame
