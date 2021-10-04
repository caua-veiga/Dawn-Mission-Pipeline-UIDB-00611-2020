import os
import pvl

# Import the "gdal" and "gdal_array" submodules from within the "osgeo" module
from osgeo import gdal
from osgeo import gdal_array

# Import the NumPy module
import numpy as np

# We transferred the irradiance values from the .TAB file to a .txt file because it is easier to manipulate in python
# We stored the irradiance values for each band in the following list so that you don't have to open the .txt file to run this script
irradiance = [701.09772,
 688.44055,
 673.94202,
 661.51331,
 647.09552,
 630.34851,
 615.91522,
 600.35834,
 585.0022,
 579.47711,
 570.99005,
 559.76251,
 549.18988,
 540.87408,
 533.48358,
 521.62585,
 513.05872,
 502.90271,
 494.0437,
 483.92422,
 477.55356,
 473.79971,
 465.97736,
 457.94589,
 450.17047,
 442.36816,
 434.58661,
 423.75317,
 413.78543,
 412.80328,
 406.57578,
 398.81732,
 393.2879,
 386.91647,
 381.62662,
 375.19556,
 368.3779,
 362.50143,
 357.59863,
 352.71283,
 346.41458,
 340.04807,
 333.43024,
 326.7706,
 322.52551,
 317.05414,
 312.71957,
 308.05945,
 302.20493,
 297.26648,
 293.63342,
 286.81931,
 285.15369,
 282.67117,
 278.72299,
 274.72144,
 270.05927,
 265.49048,
 259.70245,
 252.99014,
 247.96658,
 247.31619,
 243.55789,
 239.20251,
 238.28923,
 231.80467,
 226.49948,
 225.91519,
 222.16122,
 214.99457,
 209.26117,
 209.34814,
 205.57635,
 201.03435,
 196.84467,
 190.11534,
 185.30179,
 185.20869,
 183.16412,
 180.11159,
 176.51584,
 173.70815,
 170.53114,
 166.76659,
 160.37392,
 158.45204,
 157.61191,
 154.2836,
 151.74527,
 148.00252,
 141.33215,
 140.06775,
 139.3862,
 137.83997,
 136.8744,
 134.46349,
 131.20007,
 127.06413,
 123.25457,
 124.53945,
 122.62711,
 120.44386,
 118.72644,
 117.00896,
 115.53932,
 113.88994,
 111.29474,
 109.06796,
 107.73661,
 106.26601,
 104.05219,
 102.4911,
 100.92661,
 98.987541,
 97.546234,
 96.314507,
 94.46936,
 93.074036,
 91.800179,
 90.383537,
 88.427475,
 84.799164,
 84.829025,
 84.281128,
 83.395805,
 81.894722,
 80.616501,
 79.627052,
 78.402954,
 77.095169,
 75.842339,
 74.618752,
 73.657227,
 72.399498,
 71.187286,
 69.857559,
 69.180138,
 67.880547,
 66.376877,
 65.714264,
 64.960121,
 63.433113,
 62.830555,
 61.818951,
 60.498665,
 59.905304,
 59.421127,
 58.206501,
 57.179749,
 56.705879,
 55.892887,
 54.673,
 54.040356,
 53.513351,
 52.487419,
 51.694229,
 51.396141,
 50.701946,
 49.902,
 49.443054,
 48.688007,
 47.785252,
 47.196205,
 46.597111,
 46.132729,
 45.256706,
 44.694901,
 44.333145,
 43.735901,
 42.436245,
 41.527428,
 41.691029,
 41.311207,
 40.743797,
 40.121189,
 39.825397,
 39.482544,
 38.980988,
 38.491768,
 37.984238,
 37.500137,
 37.046867,
 36.591621,
 35.990284,
 35.346527,
 35.111282,
 34.719761,
 34.376133,
 33.941021,
 33.514378,
 33.103939,
 32.697365,
 32.272842,
 31.843859,
 31.466272,
 30.955935,
 30.430977,
 30.286755,
 29.966034,
 29.601398,
 29.2502,
 28.828657,
 28.494402,
 28.16898,
 27.84,
 27.54933,
 27.234074,
 26.901222,
 26.566425,
 26.194675,
 25.936451,
 25.622292,
 25.286303,
 24.744522,
 24.524549,
 24.423752,
 24.131622,
 23.875357,
 23.581594,
 23.31456,
 23.058718,
 22.705452,
 22.463297,
 22.281425,
 22.046055,
 21.727436,
 21.517149,
 21.256088,
 21.043247,
 20.830824,
 20.59024,
 20.363441,
 20.138712,
 19.922518,
 19.675516,
 19.444431,
 19.261808,
 19.032484,
 18.824284,
 18.583763,
 18.243439,
 18.001474,
 17.968836,
 17.679176,
 17.601439,
 17.4209,
 17.226883,
 17.064974,
 16.844793,
 16.671139,
 16.514357,
 16.259148,
 16.077644,
 15.96014,
 15.821804,
 15.678665,
 15.533805,
 15.371497,
 15.202774,
 15.023167,
 14.875574,
 14.726713,
 14.583426,
 14.443509,
 14.292397,
 14.145844,
 13.971935,
 13.85462,
 13.691045,
 13.554542,
 13.411316,
 13.297916,
 13.162704,
 13.035462,
 12.925385,
 12.804173,
 12.662223,
 12.510267,
 12.344601,
 12.216961,
 12.122327,
 11.957555,
 11.853046,
 11.641988,
 11.544901,
 11.500111,
 11.420848,
 11.16671,
 10.983994,
 11.011701,
 10.978021,
 10.862952,
 10.771315,
 10.663865,
 10.572686,
 10.474023,
 10.398017,
 10.306902,
 10.205541,
 10.123122,
 10.006224,
 9.9028559,
 9.8258972,
 9.7221413,
 9.638092,
 9.5622492,
 9.4816027,
 9.3952017,
 9.3047752,
 9.20928,
 9.0943041,
 9.0243835,
 8.9532242,
 8.8516655,
 8.7421293,
 8.6776743,
 8.6109638,
 8.5178194,
 8.473546,
 8.3856812,
 8.2201023,
 8.1552849,
 8.1472254,
 8.1055861,
 8.0296535,
 7.9667153,
 7.904695,
 7.8296714,
 7.7711701,
 7.6942811,
 7.6171041,
 7.5467606,
 7.495295,
 7.4186268,
 7.3516593,
 7.2883034,
 7.1962981,
 7.1330528,
 7.1115313,
 7.0644464,
 6.9963179,
 6.9245791,
 6.8745036,
 6.8182564,
 6.7640786,
 6.6847034,
 6.5135188,
 6.4054227,
 6.3940535,
 6.3600144,
 6.3117728,
 6.2360191,
 6.0797839,
 5.9943371,
 5.9718194,
 5.944128,
 5.909338,
 5.834362,
 5.696372,
 5.628747,
 5.6218076,
 5.5992465,
 5.5645065,
 5.5164247,
 5.4174595,
 5.343297,
 5.3292918,
 5.3116226,
 5.2790003,
 5.2292829,
 5.1527638,
 5.0814815,
 5.0633621,
 5.0427361,
 5.017518,
 4.9746509,
 4.9243279,
 4.8499341,
 4.8175783,
 4.8050866,
 4.7777634,
 4.7519875,
 4.7207432,
 4.6546192,
 4.587564,
 4.5815592,
 4.5733609,
 4.5510397,
 4.5270514,
 4.4941959,
 4.4521098,
 4.4177942,
 4.3976092,
 4.367312,
 4.3364387,
 4.3050756,
 4.2672348,
 4.2251687,
 4.1949749,
 4.16642,
 4.1365299,
 4.1148286,
 4.0935397,
 4.0690289,
 4.0393705,
 4.0043759,
 3.9700632,
 3.93432,
 3.9086456,
 3.887547,
 3.8631036,
 3.8310547,
 3.7963946,
 3.7675819,
 3.7418461,
 3.7149496,
 3.6901364,
 3.667099,
 3.6423326,
 3.6133332,
 3.5846996,
 3.5562909,
 3.5303166,
 3.5095685,
 3.4902482,
 3.4720774,
 3.4471908,
 3.4201047,
 3.3934944,
 3.3659639,
 3.3400521,
 3.3147202]# Irradiance at each band

def create_spectral_grid(area, image, grid_):
    """
    Create a grid where each pixel represents the spectral value from an choosen cube ('image')

    For each pixel we will calculate the mean spectral value of a n by n square around it, the parameter 'area'
    represents the area of that square (in pixels).
    The parameter 'image' is the original hyperspectral cube from which the grid will be created
    """
    grid = grid_.copy()

    n = int(np.sqrt(area))


    for j in range(grid.shape[0]):  # represents the y-axis
        for i in range(grid.shape[1]):  # represents the x-axis
            # We use boolean conditions to check if our square will be outside of the image range

            if i < n:
                if j < n:
                    grid[j, i, :] = [np.mean(image[:2 * j, :2 * i, band]) for band in range(grid.shape[2])]
                else:
                    grid[j, i, :] = [np.mean(image[j - n:j + n, :2 * i, band]) for band in range(grid.shape[2])]

            elif i > grid.shape[1] - n:
                if j > grid.shape[0] - n:
                    grid[j, i, :] = [np.mean(image[j - n:, i - n:, band]) for band in range(grid.shape[2])]
                else:
                    grid[j, i, :] = [np.mean(image[j - n:j + n, i - n:, band]) for band in range(grid.shape[2])]

            elif j < n and i > n:
                grid[j, i, :] = [np.mean(image[:2 * j, i - n:i + n, band]) for band in range(grid.shape[2])]

            elif j > grid.shape[0] - n and i < grid.shape[1] - n:
                grid[j, i, :] = [np.mean(image[j - n:, i - n:i + n, band]) for band in range(grid.shape[2])]

            else:
                grid[j, i, :] = [np.mean(image[j - n:j + n, i - n:i + n, band]) for band in range(grid.shape[2])]

    return grid


def reflectance(image, irradiance, D, grid_):
    """
    D: SPACECRAFT_SOLAR_DISTANCE in Km
    k: is the value of one astronomical unit expressed in km (149597870.7)
    """
    grid = grid_.copy()

    k = 149597870.7  # Km


    for j in range(grid.shape[0]):  # represents the y-axis
        for i in range(grid.shape[1]):  # represents the x-axis
            grid[j, i, :] = [(np.pi * image[j, i, band] * (D / k) ** 2) / (irradiance[band]) for band in
                             range(grid.shape[2])]

    return grid


def main(input_dic,output_dic):



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
        if output_dic == input_dic:
            equal = int(input("Your input and output directory are the same, your files will be overwrited! Do you wanna"
                          " continue or change the output directory?\n1 -Keep same directory\n0 -Enter new directory\n"))
            if equal == 1:
                key2 = True
            else:
                output_dic = input("Enter a new output directory: ")


        if output_dic != input_dic:
            try:
                ls2 = os.listdir(repr(output_dic)[1:-1])
                key2 = True
            except Exception as e:
                print(e)
                output_dic = input("Enter a valid output directory: ")



    # List of .cub files
    cubes = []
    labels = []
    for file in ls:
        # Make sure that we only append the cubes
        if file[-4:].lower() == ".cub":
            cubes.append(file)
            # append the labels so that we can access the SPACECRAFT_SOLAR_DISTANCE
            lbl = file[:-4] + ".LBL"
            labels.append(lbl)


    ncubes = 0
    # Convert files into level 2 isiscube
    for cub,label in zip(cubes,labels):
        try:
            ncubes += 1
            out_cub = output_dic + "/" + cub 
            cub = input_dic + "/" + cub
            label = input_dic + "/" + label

            # Open a GDAL dataset
            dataset = gdal.Open(repr(cub)[1:-1], gdal.GA_ReadOnly)

            # Allocate our array using the first band's datatype
            image_datatype = dataset.GetRasterBand(1).DataType  # we do that so we can define the numpy array dtype

            image = np.zeros((dataset.RasterYSize, dataset.RasterXSize, dataset.RasterCount),
                             # We will create a cube with our data
                             dtype=gdal_array.GDALTypeCodeToNumericTypeCode(image_datatype))

            # Loop over all bands in dataset
            for b in range(dataset.RasterCount):
                # Remember, GDAL index is on 1, but Python is on 0 -- so we add 1 for our GDAL calls
                band = dataset.GetRasterBand(b + 1)

                # Read in the band's data into the third dimension of our array
                image[:, :, b] = band.ReadAsArray()

            # Create a array of zeros in the same shape of the 3d cube
            grid_ = np.zeros((dataset.RasterYSize, dataset.RasterXSize, dataset.RasterCount),
                            dtype=gdal_array.GDALTypeCodeToNumericTypeCode(image_datatype))

            # Load the SPACECRAFT_SOLAR_DISTANCE and Band_center values from the cube label
            lbl = pvl.load(repr(label)[1:-1])
            center = lbl['QUBE']['BAND_BIN']['BAND_BIN_CENTER']  # Wavelength center at each band
            ssd = lbl['SPACECRAFT_SOLAR_DISTANCE'][0]

            # Transform the value of each pixel into the reflectance value
            reflec = reflectance(image, irradiance, ssd, grid_)

            # Calculate the mean value around each pixel (5X5 square)
            spectral_grid = create_spectral_grid(25, reflec, grid_)


            # Change the new values into the cube and save

            # Load the driver
            driver = gdal.GetDriverByName("ISIS3")
            src_ds = gdal.Open(repr(cub)[1:-1])
            # Create a copy of the original cube
            dst_ds = driver.CreateCopy(repr(out_cub)[1:-1], src_ds, strict=0)

            # Use the spectral_grid value for each band
            for band in range(dataset.RasterCount):
                dst_ds.GetRasterBand(band + 1).WriteArray(spectral_grid[:, :, band], 0, 0)

            # Once we're done, close properly the dataset
            dst_ds = None
            src_ds = None

        except Exception as e:
            print(e)

    return f"{ncubes} cubes transformed"

if __name__ == "__main__":
    print(main(input("input directory: "),input("output directory: ")))
