import http.client
import mimetypes
from codecs import encode
import json
import ssl
import requests
import certifi

##file_path : "文件路径 , D:\\temp\\ComfyUI_00743_uiqpt_1742470204.png"

def UploadFile(file_path, api_key):
   url = 'https://www.runninghub.cn/task/openapi/upload'

   files = {
      'file': open(file_path, 'rb')
   }

   fileType = "image"
   if file_path.endswith(".mp4"):
      fileType = "video"

   data = {
      'apiKey': api_key,
      'fileType': fileType
   }

   try:
      # 使用 certifi 提供的证书
      response = requests.post(url, files=files, data=data, verify=certifi.where())

      files['file'].close()
      result = response.json()
      print(result)
      ##{"code":0,"msg":"success","data":{"fileName":"api/a61c3fdbe0cc78978f8262d1e5d68cc906984c9e03c38e91198307128a4bc352.png","fileType":"image"}}
      return result["data"]["fileName"]
   except Exception as e:
      files['file'].close()
      raise e