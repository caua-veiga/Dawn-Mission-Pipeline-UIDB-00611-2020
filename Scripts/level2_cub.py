import os


def level2_cub(input_dic):
    """"
    Transform all .cub level1 files of an directory into level 2 ISIS cubes using spiceinit tool
    input_dic: Path of the directory that contains the level1 cubes
    """


    # To make sure that the input directory exist
    key = False
    while not key:
        try:
            # Array containing all the files in the input directory
            ls = os.listdir(repr(input_dic)[1:-1])  # repr to use exactly the path passed, so that the python string doesn't missread //
            key = True
        except Exception as e:
            print(e)
            input_dic = input("Enter a valid input directory: ")


    # List of .cub files
    cubes = []
    for file in ls:
        # Make sure that we only append the cubes
        if file[-4:].lower() == ".cub":
            cubes.append(file)


    ncubes = 0
    # Convert files into level 2 isiscube
    for cub in cubes:
        try:
            ncubes += 1
            cub = input_dic + "/" + cub
            os.system(f"spiceinit from={repr(cub)[1:-1]} ")
        except Exception as e:
            print(e)

    return f"{ncubes} cubos transformados"

if __name__ == "__main__":
    print(level2_cub(input("input directory: ")))


