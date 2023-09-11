import configparser

from rich.console import Console
from rich.markdown import Markdown

from activator.activate import activate

# 创建配置解析器对象
config = configparser.ConfigParser()

# 读取配置文件
config.read("config.ini")

# 获取版本号
VERSION = config["General"]["version"]

console = Console()

DECLARE = "\n    > Copilot Activator 是一款 Github Copilot [bold blue]远程授权工具[/bold blue]\n    > 该工具未对 Copilot 以及其他相关软件做任何修改，[bold blue]非破解软件[/bold blue]\n    > 该工具仅供学习交流使用，如有侵权请联系删除\n"
TIPS = "\n    > 使用授权需要联网，请确保网络连接正常，尽量不要开启科学上网工具\n    > 使用本工具之前请先下载Copilot插件，并关闭要激活的IDE，否则可能会授权失败\n    > 输入授权密钥后，授权密钥会和机器绑定，如需授权多台机器，请另外购买\n    > 使用中遇到问题请联系客服\n"
if __name__ == "__main__":
    try:
        try:
            console.print(Markdown("# Copilot Activator v%s.beta" % VERSION))
            console.print(Markdown("> ***声明***"))
            console.print(DECLARE)
            console.print(Markdown("> ***注意事项***"))
            console.print(TIPS)
            key = input("请输入授权密钥: ")
            activate(key, VERSION)
        except Exception as e:
            console.print(e)
            console.print("\n遇到未知错误 请联系客服\n", style="bold red")

    finally:
        input("按任意键退出")
