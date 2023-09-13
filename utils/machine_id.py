import hashlib

import cpuinfo
import psutil

import machineid


def get_machine_id():
    total_mem = psutil.virtual_memory().total
    cpu_model = cpuinfo.get_cpu_info()["brand_raw"]
    machine_id = f"{str.lower(machineid.id())}.{total_mem}.{cpu_model}"
    return hashlib.sha256(machine_id.encode("utf-8")).hexdigest()


if __name__ == "__main__":
    machine_id = get_machine_id()
    print(machine_id)
