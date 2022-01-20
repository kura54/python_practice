even = [2, 4, 6, 8, 10, 12]
print(even[1:4])

fruits = ['apple']

favorite = input("好きなフルーツは？")

if favorite in fruits:
    print("{}ですね、あるよん".format(favorite))
    fruits.remove(favorite)
else:
    print("{}ですね、仕入れました。".format(favorite))
    fruits.append(favorite)

print("今あるフルーツ{}".format(fruits))
