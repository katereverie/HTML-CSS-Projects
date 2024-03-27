def hat(**kwargs):
    for color, count in kwargs.items():
        print(type(color))
        print(f"{color}:{count}")

hat1 = hat(red=3, blue=2)
contents = []
contents.extend(['red'] * 3)
contents.extend(['blue'] * 1)
print((contents))
