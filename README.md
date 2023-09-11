# Copilot Activator

Copilot Activator 是一款 Github Copilot 远程授权工具。该工具未对 Copilot 以及其他相关软件做任何修改，非破解软件。该工具仅供学习交流使用，如有侵权请联系删除。

## 特点

使用简单的授权密钥激活 Copilot 插件。
支持多种版本的 Copilot 插件。
授权密钥会与机器绑定，确保合法使用。

## 免责声明

请在使用本工具前，详细阅读并理解以下声明：

> Copilot Activator 是一个用于学习交流的工具，不得用于非法用途。请确保你拥有合法的 Copilot 授权，以便合法使用该工具。

## 配置文件

Copilot Activator 使用一个配置文件来管理参数。配置文件默认名为 config.ini ，可参考 config_template.ini 配置。以下是一个示例配置文件的内容：

```
[General]
version = 0.6.1
```

根据需要修改配置文件中的参数。确保配置文件中的敏感信息（如服务器地址和授权密钥）得到妥善保护，以防止泄露。

## Git LFS 下载大文件
存在大文件需要下载，请确保已安装 Git LFS。可以使用以下命令来安装 Git LFS：

```bash
sudo apt-get install git-lfs
```

然后，使用以下命令来拉取 Git 仓库，并下载大文件：


```bash
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
git lfs pull
```

这将下载仓库中由 Git LFS 管理的大文件。

## 使用

1. 确保配置文件配置和 git-lfs 下载大文件
2. 在项目根目录下创建虚拟环境（可选），并激活虚拟环境：

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate  # 在 Windows 上使用 `.venv\Scripts\activate`
    ```

3. 安装依赖包

    ```bash
    pip install -r requirements.txt
    ```

4. 执行main.py

    ```bash
    python main.py
    ```

## 说明

本仓 fork 于 [ashdjashd/copilot_activator](https://github.com/ashdjashd/copilot_activator) ，但fork的公共仓分支无法使用 git-lfs ，因此取消了 fork 联系。