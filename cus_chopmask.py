import numpy as np
import cv2
import torch
class chopmask:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image1": ("IMAGE",),
                "image2": ("IMAGE",)
            }
        }
 
    CATEGORY = "essentials/cus_chopmask"
    OUTPUT_NODE = True
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "example_func"
 
    def example_func(self,image1,image2):
        print("image2",image2,image2.shape)
        image1=image1.squeeze(0)
        image2=image2.squeeze(0)
        image1=image1.numpy()
        array = image2.numpy()
 
        
        gray_image2 = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)
        if gray_image2.dtype != np.uint8:
            gray_image2 = (gray_image2 * 255).astype(np.uint8)
        # 二值化图像
        _, binary_image2 = cv2.threshold(gray_image2, 127, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(binary_image2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
     
        # 计算所有轮廓的最小外接矩形
        x, y, w, h = cv2.boundingRect(np.concatenate(contours))
        print("pass")
        # 根据最小外接矩形裁剪原图
        cropped_image_cv = image1[y:y+h, x:x+w]

            # 使用 OpenCV 的函数处理图像
        # 例如：将两张图像相加

        # 将处理后的图像转换回 ComfyUI 的格式
        cropped_image = torch.tensor(cropped_image_cv).unsqueeze(0)
        return (cropped_image,)
 
