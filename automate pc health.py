import shutil
import psutil


def check_disk_usage(disk):
    diskU=shutil.disk_usage(disk)
    free_usage=diskU.free/diskU.total * 100
    return free_usage > 20


def check_cpu_usage():
    cu=psutil.cpu_percent(1)
    return cu > 78


if not check_disk_usage("/") or not check_cpu_usage():
    print("Error, PC not healthy at ll")
    
else:
    print("PC successfully ok!,pls repair affected parts")
