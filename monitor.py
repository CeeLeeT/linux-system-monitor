#!/usr/bin/env python3
import os, platform, shutil, time

def memory():
    d={}
    with open("/proc/meminfo",encoding="utf-8") as f:
        for line in f:
            k,v=line.split(":",1); d[k]=int(v.strip().split()[0])
    return d["MemTotal"],d["MemTotal"]-d["MemAvailable"]

def uptime():
    with open("/proc/uptime",encoding="utf-8") as f:s=int(float(f.read().split()[0]))
    return f"{s//86400}d {(s%86400)//3600}h {(s%3600)//60}m"

if platform.system()!="Linux": raise SystemExit("Linux only.")
total,used=memory(); disk=shutil.disk_usage("/"); load=os.getloadavg()
print("="*50,"\nLinux System Monitor\n"+"="*50)
print("Host       :",platform.node())
print("Kernel     :",platform.release())
print("Uptime     :",uptime())
print("Load avg   :"," ".join(f"{x:.2f}" for x in load))
print(f"Memory     : {used/1024/1024:.2f} / {total/1024/1024:.2f} GiB")
print(f"Disk /     : {disk.used/1024**3:.2f} / {disk.total/1024**3:.2f} GiB")
print("Checked    :",time.strftime("%Y-%m-%d %H:%M:%S"))
