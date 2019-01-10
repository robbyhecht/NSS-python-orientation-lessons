print("hello world")
zoo = ("hi", "bye")

my_set = {"foo", "bar", "foo"}

myTuple = (my_set)

print(myTuple)

cow = "wf"
dog = "woof"
if cow == "moo" and dog == "woof":
  print(cow)
elif cow == "woof":
  print("WTF")
else:
  print("the end")

for thing in my_set:
  print(thing.title())
1
for item in my_set:
  for animal in zoo:
    print("i like {0} to see {1}".format(item, animal))

# for trait in person:
#   print(trait)


last thing we did was the global variable Fred Sally example