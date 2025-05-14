

##这个api 实现对应的 流程 一多图像多主体可控性图像生成UNO ， 就是把几张图片的内容进行融合，生成一张新的图片
##https://www.runninghub.ai/workflow/1921433877150121985?source=workspace

import http.client
import json
import os
from upload import UploadFile
from runninghub_task import  CreateTaskToLuban

workflow_id = "1922531884117671938"

def NewTask(api_key, image_path):

    ##file is exist
    if not os.path.exists(image_path):
        print(image_path, " is not exist")
        return


    """创建任务"""
    fileId2 = UploadFile(image_path, api_key)
    print(fileId2)

    nodeInfoList =  [
           {
               "nodeId": "3",
               "fieldName": "image",
               "fieldValue": fileId2
           }
       ]
    user_name = os.getenv("RUNNING_HUB_USER")
    CreateTaskToLuban(api_key, workflow_id , nodeInfoList, "利用提示词去除背景并添加纯色背景-"+user_name)
