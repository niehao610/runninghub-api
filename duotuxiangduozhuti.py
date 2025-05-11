

##这个api 实现对应的 流程 一多图像多主体可控性图像生成UNO ， 就是把几张图片的内容进行融合，生成一张新的图片
##https://www.runninghub.ai/workflow/1921433877150121985?source=workspace

import http.client
import json
import os
from upload import UploadFile
from runninghub_task import  CreateTask

workflow_id = "1921433877150121985"

def NewTask(api_key, image1_path, image2_path, image3_path , prompt):

    ##file is exist
    if not os.path.exists(image1_path):
        print(image1_path, " is not exist")
        return

    if not os.path.exists(image2_path):
        print(image2_path, " is not exist")
        return

    if not os.path.exists(image3_path):
        print(image3_path, " is not exist")
        return


    """创建任务"""
    conn = http.client.HTTPSConnection("www.runninghub.cn")
    fileId1 = UploadFile(image1_path, api_key)
    print(fileId1)
    fileId2 = UploadFile(image2_path, api_key)
    print(fileId2)
    fileId3 = UploadFile(image3_path, api_key)
    print(fileId3)

    nodeInfoList =  [
          {
             "nodeId": "9",
             "fieldName": "image",
             "fieldValue": fileId1
          },
           {
               "nodeId": "40",
               "fieldName": "image",
               "fieldValue": fileId2
           },
           {
               "nodeId": "41",
               "fieldName": "image",
               "fieldValue": fileId3
           },
           {
               "nodeId": "54",
               "fieldName": "text",
               "fieldValue": prompt
           }
       ]

    CreateTask(api_key, workflow_id , nodeInfoList)
