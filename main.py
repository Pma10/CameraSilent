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
adb_path = os.path.abspath(os.path.join("adb", "platform-tools", "adb.exe"))
# Kill server first to ensure fresh state
subprocess.run([adb_path, "kill-server"], shell=True)
subprocess.run([adb_path, "start-server"], shell=True)
print(msg["server_started"])

print(msg["select_connection"])
while True:
    conn_choice = input("Enter choice (1/2): ")
    if conn_choice == "1":
        print(msg["connect_phone"])
        print(msg["press_enter"])
        input()
        break
    elif conn_choice == "2":
        print(msg["wireless_desc"])
        ip_port = input(msg["enter_ip_port"]).strip()
        pair_code = input(msg["enter_pair_code"]).strip()
        
        print(msg["pairing"])
        # Use argument list for more robust execution
        pair_result = subprocess.run([adb_path, "pair", ip_port, pair_code], capture_output=True, text=True, shell=True)
        
        if pair_result.returncode != 0 or "Successfully paired" not in pair_result.stdout:
            print(msg["pair_fail"])
            print(f"Error Detail: {pair_result.stdout} {pair_result.stderr}")
            print("\n[Tip] 만약 'protocol fault' 에러가 발생한다면:")
            print("1. 휴대폰에서 무선 디버깅을 껐다가 다시 켜보세요.")
            print("2. '페어링 코드로 기기 페어링' 팝업에 떠있는 IP와 포트가 맞는지 다시 확인하세요.")
            print("3. 컴퓨터와 휴대폰이 정말로 '같은' 와이파이에 있는지 확인하세요.")
            continue
        
        # After pairing, wireless debugging usually shows a different port for connection
        print("\n" + msg["device_connected"])
        print("이제 '페어링' 창을 닫고, 무선 디버깅 메인 화면에 크게 적힌 'IP 주소 및 포트'를 확인하세요.")
        conn_ip_port = input(msg["enter_ip_port"]).strip()
        
        print(msg["connecting"])
        connect_result = subprocess.run([adb_path, "connect", conn_ip_port], capture_output=True, text=True, shell=True)
        if "connected to" not in connect_result.stdout:
            print(msg["connect_fail"])
            print(connect_result.stdout)
            continue
        break
    else:
        print("Invalid choice.")

print(msg["check_device"])
while True:
    result = subprocess.run([adb_path, "devices"], capture_output=True, text=True, shell=True)
    output = result.stdout
    print()
    if len(output.splitlines()) > 2 and "unauthorized" not in output:
        print(msg["device_connected"])
        break
    else:
        print(msg["device_not_connected"])
        print(msg["press_enter"])
        input()

subprocess.run([adb_path, "shell", "settings", "put", "system", "csc_pref_camera_forced_shuttersound_key", "0"], shell=True)
print(msg["camera_silent"])
subprocess.run(r"adb\platform-tools\adb.exe kill-server", shell=True)
