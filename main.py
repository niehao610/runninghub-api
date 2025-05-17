from upload import UploadFile
from dotenv import load_dotenv
load_dotenv()
import duotuxiangduozhuti
import motetiaowu
import genhuanbeijing
import os
import runninghub_task
from moviepy.editor import VideoFileClip


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
    work_dir = "/Users/share/Desktop/running_hub"
    image_dir = os.path.join(work_dir, "images")
    video_dir = os.path.join(work_dir, "videos")

    image_files = os.listdir(image_dir)

    files = {}
    for image_file in image_files:
        image_path = os.path.join(image_dir, image_file)
        ##获取文件大小
        file_size = os.path.getsize(image_path)
        if file_size > 1024 * 1024 * 10:
            print("!!!!!! image ", image_file, " is too big")
            continue

        #viddeo 跟 image 命名一样, 就是后缀不一样 是 mp4
        video_path = os.path.join(video_dir, image_file.replace(".png", ".mp4"))
        if not os.path.exists(video_path):
            print("！！！！video", video_path, " is not exist")
            continue

        ##视频文件的播放时长
        clip = VideoFileClip(video_path)
        duration = clip.duration
        print("视频时长:", duration)
        raw_video_path = video_path.replace(".mp4", "_raw.mp4")
        os.rename(video_path, raw_video_path)

        if duration > 18:
            print("视频时长大于18秒，截取3-18秒")
            ## 使用ffmpeg 提取前15秒
            os.system(f"/usr/local/bin/ffmpeg -ss 3  -i {raw_video_path}  -t  15 -c copy  -avoid_negative_ts 1  {video_path}")
        else:
            os.system(f"/usr/local/bin/ffmpeg -ss 3  -i {raw_video_path}  -t 15  -c copy  -avoid_negative_ts 1  {video_path}")

        print("\n\n")
        print(image_path)
        print(video_path)
        print("\n\n")
        motetiaowu.NewTask(api_key, video_path, image_path, 4)
