from .plugin.transform import transform

from aiortc import MediaStreamTrack

class VideoTransformTrack(MediaStreamTrack):
    """
    A video stream track that transforms frames from an another track.
    """

    kind = "video"

    def __init__(self, track, transform):
        super().__init__()  # don't forget this!
        self.track = track
        self.transform = transform

    async def recv(self):
        frame = await self.track.recv()

        # apply the transform to the frame
        new_frame = transform(frame, self.transform)

        # send data to client
        return new_frame

# Path: VideoTransformTrack/edges.py
