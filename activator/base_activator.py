import os, glob, shutil, platform
from frozen_dir import app_path
from rich.console import Console

console = Console()
APP_PATH = app_path()


class BaseActivator:

    def __init__(self):
        self.search_path = ''
        self.path_suffix = ''

    def get_path(self):
        if self.search_path == '':
            return []
        else:
            matching_dirs = glob.glob((self.search_path), recursive=True)
            agent_paths = []
            for dir in matching_dirs:
                if os.path.exists(os.path.join(dir, self.path_suffix)):
                    agent_paths.append(os.path.join(dir, self.path_suffix))

            return agent_paths

    def modify_extension(self, paths):
        if not paths:
            paths = self.get_path()
        agent_bin_path = os.path.join(APP_PATH, 'bin')
        for file_path in paths:
            if os.path.exists(file_path):
                if os.path.exists(file_path):
                    try:
                        shutil.rmtree(file_path)
                    except Exception as e:
                        console.print('\n请关闭要授权的应用再试，如果关闭了还是不行，可能后台还有残留进程，重启电脑即可\n',
                                      style='bold red')
                        break

                os.mkdir(file_path)
                for file in os.listdir(agent_bin_path):
                    shutil.copy(os.path.join(agent_bin_path, file), file_path)

        user_home_dir = os.path.expanduser('~')
        if platform.system() == 'Darwin':
            hosts_file = os.path.join(user_home_dir, '.config', 'github-copilot', 'hosts.json')
            if os.path.exists(hosts_file):
                os.remove(hosts_file)
        elif platform.system() == 'Windows':
            hosts_file = os.path.join(user_home_dir, 'AppData', 'Local', 'github-copilot', 'hosts.json')
            if os.path.exists(hosts_file):
                os.remove(hosts_file)
