import os
import shutil


def main():

    category_extension = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        file_extension = filename.split('.')[-1]
        if file_extension not in category_extension:
            category_name = input("What category would you like to sort {} files into? ".format(file_extension))
            category_extension[file_extension] = category_name
            try:
                os.mkdir(category_name)
            except FileExistsError:
                pass
        shutil.move(filename, "{}/{}".format(category_extension[file_extension], filename))


main()
