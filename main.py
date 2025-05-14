from upload import UploadFile
from dotenv import load_dotenv
load_dotenv()
import duotuxiangduozhuti
import motetiaowu
import genhuanbeijing
import os
import runninghub_task
from upload import UploadFile


if __name__ == "__main_22_":
    api_key = os.getenv("RUNNING_HUB_APPKEY")
    print(api_key)
    image1_path = "D:\AI\ComfyUI_windows_portable\ComfyUI\output\sexy\ComfyUI_00037_.png"
    genhuanbeijing.NewTask(api_key, image1_path)
    image1_path = "D:\AI\ComfyUI_windows_portable\ComfyUI\output\sexy\ComfyUI_00036_.png"
    genhuanbeijing.NewTask(api_key, image1_path)


if __name__ == "__main__":
    # 运行测试
    api_key = os.getenv("RUNNING_HUB_APPKEY")
    print(api_key)
    work_dir = ""
    image_dir = os.path.join(work_dir, "images")
    video_dir = os.path.join(work_dir, "videos")

    image_files = os.listdir(image_dir)

    files = {}
    for image_file in image_files:
        image_path = os.path.join(image_dir, image_file)
        #viddeo 跟 image 命名一样, 就是后缀不一样 是 mp4
        video_path = os.path.join(video_dir, image_file.replace(".png", ".mp4"))
        print("\n\n")
        print(image_path)
        print(video_path)
        print("\n\n")
        motetiaowu.NewTask(api_key, video_path, image_path, 4)
