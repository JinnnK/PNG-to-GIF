import os
from PIL import Image
from IPython.display import Image as Img
from IPython.display import display
def generate_gif(path):
    img_list = os.listdir(path)
    img_list = [path + '/' + str(x) + ".png" for x in range(len(img_list))]
    images = [Image.open(x) for x in img_list]
    
    im = images[0]
    im.save('out.gif', save_all=True, append_images=images[1:],loop=0xff, duration=500)
    # loop 반복 횟수
    # duration 프레임 전환 속도 (500 = 0.5초)
    return Img(url='out.gif')

gif = generate_gif('PNG_address')
display(gif)