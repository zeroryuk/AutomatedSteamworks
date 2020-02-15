from cx_Freeze import setup, Executable

target = Executable(
    script="AutomatedSteamworks.py",
    icon="steamworksLogo.ico"
    )

setup(
    name="AutomatedSteamworks",
    version="4.2",
    description="Bot for automating steamworks in MHW",
    author="zeroryuk",
    executables=[target]
    )