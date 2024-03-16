from PIL import Image
import os
from io import BytesIO
def resizeImg(imgSource: str, newWidth:int, newHeight:int):
    path = "TienNuAdmin/SongIMG/"
    path = os.path.join(path,imgSource)
    path = os.path.abspath(path)
    image = Image.open(path)
    resized = image.resize((newWidth,newHeight))
    
    with BytesIO() as buffer:
        resized.save(buffer, format="PNG")
        buffer.seek(0)
        byte_image = buffer.getvalue()
        
    return byte_image



