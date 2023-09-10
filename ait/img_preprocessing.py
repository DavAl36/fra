from PIL import Image,ImageFilter
import glob
import os

def img_preprocessing(path_in,path_out,threshold):
    idx = 1
    file_list = sorted(glob.glob(path_in + '*'))#,key=os.path.getmtime)
    #print(file_list)

    fn = lambda x : 255 if x > threshold else 0

    for f in file_list:
        img = Image.open(f)
        img = img.rotate(270, expand=True)
        #img = img.filter(filter = ImageFilter.BLUR)
        #img = img.resize((3000, 4000))
        #img = img.resize((2000, 2000))
        img = img.resize((2500, 2500))
        #print(img.size)
        img = img.convert('L').point(fn, mode='1')
        img.save(path_out + str(idx) +'-image' + '_bw.png')
        os.chmod(path_out + str(idx) +'-image' + '_bw.png',0o777)
        idx = idx + 1
