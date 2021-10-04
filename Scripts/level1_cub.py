import os


def level1_cub(input_dic,output_dic):
    """"
    Transform all Dawn VIR PDS3 files of an directory into level 1 ISIS cubes using dawnvir2isis tool
    input_dic: Path of the directory that contains the PDS3 files
    output_dic: Path of the directory in which the ISIS cubes will be stored
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

    # To make sure that the output directory exist
    key2 = False
    while not key2:
        try:
            ls2 = os.listdir(repr(output_dic)[1:-1])
            key2 = True
        except Exception as e:
            print(e)
            output_dic = input("Enter a valid output directory: ")


    # List of ours .lbl files
    labels = []
    for file in ls:
        # Make sure that we only append the labels
        if file[-4:].lower() == ".lbl" and file[-9:-5] != "_QQ_" and file[-9:-5] != "_HK_":
            labels.append(file)

    ncubes = 0
    # Convert files into isiscube
    for lbl in labels:
        ncubes += 1
        lbl = input_dic + "/" + lbl
        image = lbl[:-4] + ".QUB"
        hk = lbl[:-6] + "_HK_" + lbl[-5:]
        to = output_dic + "/" + lbl[len(input_dic)+1:-4]

        os.system(f"dawnvir2isis from={repr(lbl)[1:-1]} image={repr(image)[1:-1]} hkfrom={repr(hk)[1:-1]} to={repr(to)[1:-1]}")

    return f"{ncubes} cubos criados"

if __name__ == "__main__":
    print(level1_cub(input("input directory: "),input("output directory: ")))


