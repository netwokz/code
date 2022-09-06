from ast import dump
import platform
import psutil
import cpuinfo
import wmi
import json
import os
from pathlib import Path

hw_file = 'C:\\Users\\deanejst\\Documents\\code\\python\\hw_info.json'
my_file_path = Path("C:\\Users\\deanejst\\Documents\\code\\python\\hw_info.json")

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

# global my_info
# if my_file_path.is_file():
#     with open(hw_file, "r") as json_file:
#         my_info = json.load(json_file)
# else:
#     my_info = cpuinfo.get_cpu_info()
#     with open(hw_file, "w") as file:
#         json.dump(my_info,file)
    
# print(f"Architecture: {platform.architecture()}")
# print(f"Name: {platform.node()}")
# print(f"OS: {platform.platform()}")
# print(f"Processor Cores: {my_info['count']}")

# print(f"Full CPU: {my_info['brand_raw']}")

print("="*40, "System Information", "="*40)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")
print(" ")

# let's print CPU information
print("="*40, "CPU Info", "="*40)
# number of cores
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))
# CPU frequencies
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
# CPU usage
# print("CPU Usage Per Core:")
# for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    # print(f"Core {i}: {percentage}%")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")
print(" ")

# Memory Information
print("="*40, "Memory Information", "="*40)
# get the memory details
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)}")
print(f"Available: {get_size(svmem.available)}")
print(f"Used: {get_size(svmem.used)}")
print(f"Percentage: {svmem.percent}%")
print(" ")

# print("="*20, "SWAP", "="*20)
# get the swap memory details (if exists)
# swap = psutil.swap_memory()
# print(f"Total: {get_size(swap.total)}")
# print(f"Free: {get_size(swap.free)}")
# print(f"Used: {get_size(swap.used)}")
# print(f"Percentage: {swap.percent}%")