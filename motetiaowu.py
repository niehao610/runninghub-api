

##这个api 实现对应的 流程 一多图像多主体可控性图像生成UNO ， 就是把几张图片的内容进行融合，生成一张新的图片
##https://www.runninghub.ai/workflow/1921433877150121985?source=workspace

import http.client
import json
import os
from upload import UploadFile , UploadVideoFile
from runninghub_task import  CreateTask

workflow_id = "1921790312258404354"

def NewTask(api_key, video_path, image_path, times=4):

    ##file is exist
    if not os.path.exists(video_path):
        print(video_path, " is not exist")
        return

    if not os.path.exists(image_path):
        print(image_path, " is not exist")
        return


    """创建任务"""
    conn = http.client.HTTPSConnection("www.runninghub.cn")
    fileId1 = UploadFile(video_path, api_key)
    print(fileId1)
    fileId2 = UploadFile(image_path, api_key)
    print(fileId2)


    nodeInfoList =  [
          {
             "nodeId": "60",
             "fieldName": "video",
             "fieldValue": fileId1
          },
           {
               "nodeId": "1616",
               "fieldName": "image",
               "fieldValue": fileId2
           },
            {
                "nodeId": "1683",
                "fieldName": "value",
                "fieldValue": times
            }
       ]

    CreateTask(api_key, workflow_id , nodeInfoList)
