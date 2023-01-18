import requests, os
import threading
import random
import time
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, Future, as_completed, wait
from multiprocessing import cpu_count

urls = [
    "https://dl3.downloadly.ir/Files/Elearning/Udemy_Video_Editing_Masterclass_Edit_Your_Videos_Like_a_Pro_2022-7.part1_Downlaodly.ir.rar",
    "https://dl3.downloadly.ir/Files/Elearning/Udemy_Video_Editing_Masterclass_Edit_Your_Videos_Like_a_Pro_2022-7.part2_Downlaodly.ir.rar",
    "https://dl3.downloadly.ir/Files/Elearning/Udemy_Video_Editing_Masterclass_Edit_Your_Videos_Like_a_Pro_2022-7.part3_Downlaodly.ir.rar",
    "https://dl3.downloadly.ir/Files/Elearning/Udemy_Video_Editing_Masterclass_Edit_Your_Videos_Like_a_Pro_2022-7.part4_Downlaodly.ir.rar",
    "https://dl3.downloadly.ir/Files/Elearning/Udemy_Video_Editing_Masterclass_Edit_Your_Videos_Like_a_Pro_2022-7.part5_Downlaodly.ir.rar",
]


def download_file(url):
    print("------", "Start download with urllib")
    name = url.split("/")[-1]
    resp = requests.get(url, stream=True)
    content_size = int(resp.headers['Content-Length']) / 1024  # 确定整个安装包的大小
    path = os.path.join(os.getcwd(), name)
    print("File path:%s, content_size:%s" % (path, content_size))
    with open(path, "wb") as file:
        print("\rFile %s, total size is: %s" % (name, content_size))
        for data in tqdm(iterable=resp.iter_content(1024), total=content_size, unit='k', desc=name):
            file.write(data)
    print("%s download ok" % name)


def test_tqdm():
    executor = ThreadPoolExecutor(max_workers=cpu_count())  # 线程池设置,最多同时跑8个线程
    for url in urls:
        args = [url, ]
        tasks = [executor.submit(lambda p: download_file(*p), args)]
    wait(tasks)


test_tqdm()
