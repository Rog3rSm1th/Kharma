from importlib.metadata import version

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣴⣶⣶⣶⣤⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⡀⠀
# ⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢻⣿⡿⢿⣿⣿⣿⣿⣿⣿⣴⡇⠀
# ⠀⠀⠀⠀⠀⢰⡿⣿⢿⣿⣿⡿⠋⠹⠋⠀⠀⠀⠁⠀⣸⣿⣿⣿⣿⣿⣿⣿⣷⣄
# ⠀⠀⠀⠀⠀⢠⠃⠈⠀⠹⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠛
# ⠀⠀⠀⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⠀
# ⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⡟⠀
# ⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠟⠀⠀
# ⠀⠀⠀⠀⢠⣿⣿⣿⠶⠦⠀⠀⢴⣶⣾⣿⣿⣷⣆⠀⠀⠀⢰⣿⣿⠟⠁⠀⠀⠀
# ⠀⠀⢀⣀⣉⣉⣇⣀⣀⣀⡀⢀⣀⣀⣀⣀⣈⣙⣛⣃⣀⠤⠛⠋⠁⠀⠀⠀⠀⠀
# ⠀⠀⢾⡯⠭⠭⣭⡭⠭⢽⣧⣼⣏⣉⣉⣉⣉⣉⣉⣹⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠸⣏⣉⣉⣉⣉⣉⣩⡇⠸⣏⣉⣉⣉⣉⣉⣉⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠈⡅⠀⠀⠀⠀⠉⠉⠉⡝⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⢡⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀／⠀￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⡇⠀⠀／⠀ psssssst...⠀⠀⠀⠀⠀⠀⠀  |
# ⠀⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⠀⠀⠀⢸⠀⠀＜⠀⠀⠀ Give the project    |
# ⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⠀⠀⢀⣀⣦⠀⠀⠀＼⠀⠀⠀ a star ;)          |
# ⠀⠀⠀⠀⠀⠀⠀⠉⢙⠺⠉⠩⠤⠜⡹⠀⠀⠀⠀＼⠀⠀⠀⠀⠀⠀⠀⠀⠀           |
# ⠀⠀⠀⠀⠀⠀⠀⣀⣸⣶⠆⠀⠀⣠⣷⠀⠀⠀⠀⠀￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⢀⣴⣶⣿⣿⣿⣿⣿⠯⣼⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⣀⠤⠾⣿⣿⡿⠿⠿⣿⣿⣾⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

# Automatically retrieves the current version number
__version__ = version("kharma")

__author__ = "Rog3rSm1th"
__email__ = "r0g3r5@protonmail.com"
__git__ = "https://github.com/Rog3rSm1th"
__twitter__ = "https://twitter.com/Rog3rSm1th"