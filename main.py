try :
    import os, shutil, subprocess, zipfile, requests
except ImportError as e:
    print("Installing required modules...")
    os.system("pip install -r requirements.txt")
    import os, shutil, subprocess, zipfile, requests

from Module.download_adb import install_adb, get_message


def get_language():
    print("Select Language / 언어를 선택하세요")
    print("1. English")
    print("2. 한국어")
    while True:
        lang_choice = input("Enter choice (1/2): ")
        if lang_choice == "1":
            return "en"
        elif lang_choice == "2":
            return "ko"
        else:
            print("Invalid choice. Please try again. / 잘못된 선택입니다. 다시 시도하세요.")

lang = get_language()

messages = get_message()

msg = messages[lang]

print(msg["title"])
print(msg["downloading"])

if os.path.exists("adb"):
    while True:
        ip = input(msg["adb_exists"])
        if ip.lower() == "y":
            shutil.rmtree("adb")
            install_adb()
            break
        elif ip.lower() == "n":
            break
        else:
            continue
else:
    install_adb()

print(msg["start_server"])
subprocess.Popen(r"adb\platform-tools\adb.exe start-server", shell=True)
print(msg["server_started"])
print(msg["connect_phone"])
print(msg["press_enter"])
input()
print(msg["check_device"])
while True:
    result = subprocess.run(r"adb\platform-tools\adb.exe devices", capture_output=True, text=True, shell=True)
    output = result.stdout
    print()
    if len(output.splitlines()) > 2 and "unauthorized" not in output:
        print(msg["device_connected"])
        break
    else:
        print(msg["device_not_connected"])
        print(msg["press_enter"])
        input()

subprocess.run(r"adb\platform-tools\adb.exe shell settings put system csc_pref_camera_forced_shuttersound_key 0", shell=True)
print(msg["camera_silent"])
subprocess.run(r"adb\platform-tools\adb.exe kill-server", shell=True)
