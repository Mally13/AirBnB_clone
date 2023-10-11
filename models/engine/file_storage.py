class FileStorage:
    def __init__(self):
        self.__objects = {}
        self.__state = {}  # Dictionary to store State objects
        self.__city = {}   # Dictionary to store City objects
        self.__place = {}  # Dictionary to store Place objects
        self.__amenity = {}  # Dictionary to store Amenity objects
        self.__review = {}  # Dictionary to store Review objects

    def all(self, cls=None):
        """Return a dictionary of all objects or objects of a specific class."""
        if cls is None:
            return self.__objects
        if cls == "State":
            return self.__state
        # Add similar conditions for City, Place, Amenity, and Review

    def new(self, obj):
        """Set the object with a given key in the objects dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    # Add methods for serialization and deserialization of new classes

# Other methods and attributes for FileStorage
