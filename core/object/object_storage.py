class ObjectStorage():
    OBJECTS = []

    @staticmethod
    def add_object(obj):
        ObjectStorage.OBJECTS.append(obj)

    def get_objects():
        return ObjectStorage.OBJECTS