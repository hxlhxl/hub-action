import os

# baidu auth code
# https://openapi.baidu.com/oauth/2.0/authorize?client_id=q8WE4EpCsau1oS0MplgMKNBn&response_type=code&redirect_uri=oob&scope=basic+netdisk

# python reference
# https://github.com/ochinchina/my-tools


def download_files():
    print("download files...")
    os.system("cd assets && wget -i links.txt")


def upload_files():
    print("upload files...")
    os.system("cat auth_code | bypy list")
    os.system("bypy syncup assets")


if __name__ == '__main__':
    download_files()
    upload_files()
