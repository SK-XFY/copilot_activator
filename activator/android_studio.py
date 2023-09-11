import os
import platform

from activator.base_activator import BaseActivator


class AndroidStudio(BaseActivator):
    def __init__(self):
        user_home_dir = os.path.expanduser("~")
        self.search_path = ""
        if platform.system() == "Darwin":
            self.search_path = os.path.join(
                user_home_dir,
                "Library",
                "Application Support",
                "Google",
                "**",
                "github-copilot-intellij",
            )
        else:
            if platform.system() == "Windows":
                self.search_path = os.path.join(
                    user_home_dir,
                    "AppData",
                    "Roaming",
                    "Google",
                    "**",
                    "github-copilot-intellij",
                )
        self.path_suffix = os.path.join("copilot-agent", "bin")
