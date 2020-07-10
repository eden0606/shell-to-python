
def Hello (name):
	print("hello " + name + " welcome to my world")
	arr=["hi", "bye", "goodbye"]
	o=open("output", "a")
	print("\n".join(arr), file=o)

print("calling hello function")
Hello("Eden")
