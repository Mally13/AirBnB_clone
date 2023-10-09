# Airbnb_clone

1. A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
	- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
	- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
	- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
	- create the first abstracted storage engine of the project: File storage.
	- create all unittests to validate all our classes and storage engine
