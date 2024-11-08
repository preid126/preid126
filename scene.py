class Scene:
    """Scene has all info for the raytracing"""

    def __init__(self, camera, objects, width, height):
        self.camera = camera
        self.objects = objects
        self.width = width
        self.height = height