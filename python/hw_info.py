from ast import dump
import platform
import psutil
import json
import os
from pathlib import Path
import time

hw_file = 'C:\\Users\\deanejst\\Documents\\code\\python\\hw_info.json'
my_file_path = Path(
    "C:\\Users\\deanejst\\Documents\\code\\python\\hw_info.json")


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


temps = psutil.sensors_temperatures()


def get_cpu_temp():
    cpu_temp = temps.get('k10temp')[0].current
    return int(cpu_temp)


def get_gpu_temp():
    gpu_temp = temps.get('amdgpu')[0].current
    return int(gpu_temp)

# print("="*40, "System Information", "="*40)
# uname = platform.uname()
# print(f"System: {uname.system}")
# print(f"Node Name: {uname.node}")
# print(f"Release: {uname.release}")
# print(f"Version: {uname.version}")
# print(f"Machine: {uname.machine}")
# print(f"Processor: {uname.processor}")
# print(" ")

# # let's print CPU information
# print("="*40, "CPU Info", "="*40)
# # number of cores
# print("Physical cores:", psutil.cpu_count(logical=False))
# print("Total cores:", psutil.cpu_count(logical=True))
# # CPU frequencies
# cpufreq = psutil.cpu_freq()
# print(f"Max Frequency: {cpufreq.max/1000:.2f}Ghz")
# print(f"Min Frequency: {cpufreq.min/1000:.2f}Ghz")
# print(f"Current Frequency: {cpufreq.current/1000:.2f}Ghz")
# # CPU usage
# # print("CPU Usage Per Core:")
# # for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
# # print(f"Core {i}: {percentage}%")
# print(f"Total CPU Usage: {psutil.cpu_percent()}%")
# print(" ")

# # Memory Information
# print("="*40, "Memory Information", "="*40)
# # get the memory details
# svmem = psutil.virtual_memory()
# print(f"Total: {get_size(svmem.total)}")
# print(f"Available: {get_size(svmem.available)}")
# print(f"Used: {get_size(svmem.used)}")
# print(f"Percentage: {svmem.percent}%")
# print(" ")


count = 0
while count < 20:
    degree_sign = u'\N{DEGREE SIGN}'  # or '\xb0'
    temps = psutil.sensors_temperatures()
    gpu_temp = temps.get('amdgpu')[0].current
    cpu_temp = temps.get('k10temp')[0].current

    print(f"CPU: {get_cpu_temp()}{degree_sign}C")
    print(f"GPU: {gpu_temp:.0f}{degree_sign}C")
    count += 1
    time.sleep(1)
