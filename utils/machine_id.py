import hashlib
import subprocess
from functools import partial

import machineid

subprocess.Popen = partial((subprocess.Popen), encoding="utf-8")
import execjs
from execjs._runner_sources import Node


def get_machine_id(cmd):
    runtime = execjs.ExternalRuntime(
        name="Node.js (V8)", command=[cmd], encoding="UTF-8", runner_source=Node
    )
    machine_id = (
        str.lower(machineid.id())
        + "."
        + runtime.eval("require('os').totalmem()+'.'+require('os').cpus()[0].model")
    )
    return hashlib.sha256(machine_id.encode("utf-8")).hexdigest()
