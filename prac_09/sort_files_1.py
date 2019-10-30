import os
import shutil


def main():
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        file_extension = filename.split('.')[-1]
        print(file_extension)
        try:
            os.mkdir(file_extension)
        except FileExistsError:
            pass
        print("{}/{}".format(file_extension, filename))
        shutil.move(filename, "{}/{}".format(file_extension, filename))


main()
