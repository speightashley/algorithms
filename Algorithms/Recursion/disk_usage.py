import os


def disk_usage(path="/home/ashleyspeight/Downloads/"):
    """Return number of bytes used by a file/folder and any descendents"""
    total = os.path.getsize(path)  # Account for direct usage
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)

    print(f"{total:<7} {path}")
    return total


disk_usage()
