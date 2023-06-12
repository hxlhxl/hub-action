
import os


def list_files(startpath):
    """
    递归列出目录中的所有文件和子目录
    """
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for file in files:
            print(f"{subindent}{file}")


# 列出 /home/user/documents 目录中的所有文件和子目录

if __name__ == '__main__':
    print("github acitons hello world ====================")
    list_files('./')
    print("github acitons hello world ====================")
