from upload import UploadFile
from dotenv import load_dotenv
load_dotenv()
import duotuxiangduozhuti
import os
import runninghub_task
from upload import UploadFile
if __name__ == "__main__":
    # 运行测试
    api_key = os.getenv("RUNNING_HUB_APPKEY")
    print(api_key)
    #UploadFile("C:\\Users\\Admin\\Pictures\\cloth\\3.png", api_key)
    duotuxiangduozhuti.NewTask(api_key, "C:\\Users\\Admin\\Pictures\\cloth\\3.png","C:\\Users\\Admin\\Pictures\\cloth\\5.png","C:\\Users\\Admin\\Pictures\\cloth\\gun.jpg", "Woman wearing green long dress holding a pistol in her hand")
    #runninghub_task.QueryTask(api_key, "1921453618497511425")
