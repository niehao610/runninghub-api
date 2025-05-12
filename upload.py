import http.client
import mimetypes
from codecs import encode
import json
import ssl

##file_path : "文件路径 , D:\\temp\\ComfyUI_00743_uiqpt_1742470204.png"
def UploadFile(file_path, api_key):
   context = ssl.create_default_context()
   context.check_hostname = False
   context.verify_mode = ssl.CERT_NONE

   conn = http.client.HTTPSConnection("www.runninghub.cn", context=context)
   dataList = []
   boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
   dataList.append(encode('--' + boundary))
   dataList.append(encode('Content-Disposition: form-data; name=apiKey;'))

   dataList.append(encode('Content-Type: {}'.format('text/plain')))
   dataList.append(encode(''))

   dataList.append(encode(api_key))
   dataList.append(encode('--' + boundary))
   dataList.append(encode('Content-Disposition: form-data; name=file; filename={0}'.format('D:\\temp\\ComfyUI_00743_uiqpt_1742470204.png')))

   fileType = mimetypes.guess_type(file_path)[0] or 'application/octet-stream'
   dataList.append(encode('Content-Type: {}'.format(fileType)))
   dataList.append(encode(''))

   with open(file_path, 'rb') as f:
      dataList.append(f.read())
   dataList.append(encode('--' + boundary))
   dataList.append(encode('Content-Disposition: form-data; name=fileType;'))

   dataList.append(encode('Content-Type: {}'.format('text/plain')))
   dataList.append(encode(''))

   dataList.append(encode("image"))
   dataList.append(encode('--'+boundary+'--'))
   dataList.append(encode(''))
   body = b'\r\n'.join(dataList)
   payload = body
   headers = {
      'Host': 'www.runninghub.cn',
      'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
   }
   conn.request("POST", "/task/openapi/upload", payload, headers)
   res = conn.getresponse()
   data = res.read()
   result = json.loads(data.decode("utf-8"))
   print(data.decode("utf-8"))
   ##{"code":0,"msg":"success","data":{"fileName":"api/a61c3fdbe0cc78978f8262d1e5d68cc906984c9e03c38e91198307128a4bc352.png","fileType":"image"}}
   return result["data"]["fileName"]