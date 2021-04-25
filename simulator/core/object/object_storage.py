class ObjectStorage():
    OBJECTS = []

    @staticmethod
    def add_object(obj):
        ObjectStorage.OBJECTS.append(obj)

    def get_objects():
        return ObjectStorage.OBJECTS

    def delete_object(obj):
        if obj in ObjectStorage.OBJECTS:
            ObjectStorage.OBJECTS.remove(obj)