import os
import platform
import subprocess
from functools import partial

from rich.console import Console
from rich.markdown import Markdown

import activator.auth as auth
import utils.machine_id as machine_id
from activator.android_studio import AndroidStudio
from activator.jetbrains import JetBrains
from activator.vs import VisualStudio
from activator.vscode import VSCode
from frozen_dir import app_path

subprocess.Popen = partial((subprocess.Popen), encoding="utf-8")
console = Console()
APP_PATH = app_path()


def activate(key, version):
    nodeCmd = "node"
    if platform.system() == "Darwin":
        nodeCmd = os.path.join(APP_PATH, "node", "bin", "node")
    else:
        if platform.system() == "Windows":
            nodeCmd = os.path.join(APP_PATH, "node", "node")
        else:
            if platform.system() == "Linux":
                nodeCmd = os.path.join(APP_PATH, "node", "bin", "node")
    _machine_id = machine_id.get_machine_id(nodeCmd)
    is_valid, response = auth.auth_copilot(key, _machine_id, version)
    if not is_valid:
        console.print("授权失败", style="bold red")
        console.print("错误信息：" + response)
        if "machine num exceeded" in response:
            console.print(
                "绑定机器数超过限制，如果您使用的是同一台电脑，可能由于某些原因您电脑的机器码发生了变化，请联系客服解绑\n另外，请前往网盘检查您的activator是否是最新版本，如果不是，请解绑后使用最新版本授权激活",
                style="bold yellow",
            )
        else:
            if "too old version" in response:
                console.print("您的activator版本过旧，请前往网盘下载最新版本", style="bold yellow")
                console.print("下载链接: https://wwa.lanzoub.com/b04wcnlqj")
                console.print("提取密码: dxke")
        return
    while True:
        console.print(Markdown("1. 激活VSCode (激活前请先升级到最新版本)"))
        console.print(Markdown("2. 激活JetBrains全家桶"))
        console.print(Markdown("3. 激活Android Studio"))
        console.print(Markdown("4. 激活VisualStudio (支持Windows2022以上版本)"))
        console.print(Markdown("5. 退出"))
        choice = input("\n请选择要进行的操作（输入对应数字按回车即可）：")
        if choice == "1":
            activator = VSCode()
        else:
            if choice == "2":
                activator = JetBrains()
            else:
                if choice == "3":
                    activator = AndroidStudio()
                else:
                    if choice == "4":
                        if platform.system() == "Windows":
                            activator = VisualStudio()
                        else:
                            console.print("\n只支持Windows激活VS\n", style="bold yellow")
                            continue
                    else:
                        if choice == "5":
                            break
                        else:
                            console.print("输入错误，请重新输入", style="yellow")
                            continue
        copilot_path = activator.get_path()
        if len(copilot_path) == 0:
            console.print("未检测到Copilot插件，请安装后使用", style="bold yellow")
        else:
            if choice == "1":
                activator.modify_extension(copilot_path, key)
            else:
                activator.modify_extension(copilot_path)
            console.print("\n激活成功，重启应用后生效\n", style="bold green")
        input("按回车键继续")
