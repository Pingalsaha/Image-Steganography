from PIL import Image
import pandas as pd
import numpy as np

class ImagSteg:

  def __fillMSB(self, inp):
    '''
    0b01100 -> [0,0,0,0,1,1,0,0]
    '''
    #print(inp)
    inp = inp.split("b")[-1]
    #print(inp)
    #print(len(inp))
    inp = '0'*(7-len(inp))+inp #7
    #print(inp)
    return [int(x) for x in inp]

  def __decrypt_pixels(self, pixels):
    '''
    Given list of 7 pixel values -> Determine 0/1 -> Join 7 0/1s to form binary -> integer -> character
    '''
    #print(pixels)
 
    pixels = [str(x%2) for x in pixels]
    #print(pixels)
    bin_repr = "".join(pixels)
    return chr(int(bin_repr,2))

  def encrypt_text_in_image(self, image_path, msg, target_path=""):
    #print(image_path)
    img = np.array(Image.open(image_path))
    #print(img)
    imgArr = img.flatten()
    #print(imgArr)
    msg += "<-END->"
    msgArr = [self.__fillMSB(bin(ord(ch))) for ch in msg]#h01101000
    #print(msgArr)
    #print(imgArr[100])
    idx = 0
    for char in msgArr:#[1, 1, 0, 1, 0, 0, 0]
      for bit in char:#1   
        if bit==1:
          if imgArr[idx]==0:
            imgArr[idx] = 1
          else:
            imgArr[idx] = imgArr[idx] if imgArr[idx]%2==1 else imgArr[idx]-1
        else: 
          if imgArr[idx]==255:
            imgArr[idx] = 254
          else:
            imgArr[idx] = imgArr[idx] if imgArr[idx]%2==0 else imgArr[idx]+1   
        idx += 1
    #x=image_path.split("\\")[-1]  
    #savePath = target_path+ x.split(".")[0] + "_encrypted.png"
    savePath = target_path+ image_path.split(".")[0] + "_encrypted.png"

    resImg = Image.fromarray(np.reshape(imgArr, img.shape))
    resImg.save(savePath)
    return 

  def decrypt_text_in_image(self, image_path,target_path=""):
    '''
    Read image -> Extract Text -> RetuC:/Users/souma/AppData/Local/Programs/Python/Python310/rn
    Read image -> Extract Text -> RetuC:/Users/souma/AppData/Local/Programs/Python/Python310/rn
    '''
    img = np.array(Image.open(image_path))
    imgArr = np.array(img).flatten()
    #print(imgArr)
    
    decrypted_message = ""
    for i in range(7,len(imgArr),7):
      decrypted_char = self.__decrypt_pixels(imgArr[i-7:i])
      decrypted_message += decrypted_char

      if len(decrypted_message)>10 and decrypted_message[-7:] == "<-END->":
        break

    return decrypted_message[:-7]