import requests
import os
import hashlib


def cache_decorator(func):
    def wrapper(url):
        # 生成缓存文件名
        cache_filename = hashlib.md5(url.encode()).hexdigest() + ".html"

        # 检查缓存文件是否存在且不为空
        if os.path.exists(cache_filename) and os.path.getsize(cache_filename) > 0:
            print(f"Reading from cache: {cache_filename}")
            with open(cache_filename, 'r', encoding='utf-8') as cache_file:
                return cache_file.read()

        # 如果缓存文件不存在或为空，下载网页内容
        print(f"Downloading from {url}")
        content = func(url)

        # 将下载的内容保存到缓存文件
        with open(cache_filename, 'w', encoding='utf-8') as cache_file:
            cache_file.write(content)

        return content

    return wrapper


@cache_decorator
def download_webpage(url):
    response = requests.get(url)
    response.raise_for_status()  # 检查请求是否成功
    return response.text


def main():
    # 让用户输入 URL
    url = input("请输入要下载的网页 URL: ")

    # 下载网页内容
    content = download_webpage(url)

    # 输出网页内容
    print(content)


if __name__ == "__main__":
    main()