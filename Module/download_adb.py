import requests, zipfile, os

def install_adb():
    with requests.get("https://dl.google.com/android/repository/platform-tools-latest-windows.zip") as r:
        with open("platform-tools-latest-windows.zip", "wb") as f:
            f.write(r.content)
        print("Downloaded platform-tools-latest-windows.zip")
        with zipfile.ZipFile("platform-tools-latest-windows.zip", "r") as zip_ref:
            zip_ref.extractall("adb")
            print("Extracted platform-tools-latest-windows.zip")
    os.remove("platform-tools-latest-windows.zip")

def get_message() :
    messages = {
        "en": {
            "title": "ADB Installer",
            "downloading": "Downloading ADB...",
            "adb_exists": "ADB already exists. Do you want to re-download it? (y/n): ",
            "start_server": "Starting ADB server...",
            "server_started": "ADB server started.",
            "connect_phone": "Connect your phone to the computer with a USB cable.",
            "press_enter": "Press Enter when ready.",
            "check_device": "Checking for connected devices...",
            "device_connected": "Device connected.",
            "device_not_connected": "Device not connected.",
            "camera_silent": "Camera set to silent mode",
            "select_connection": "Select connection method:\n1. USB Cable\n2. Wireless Debugging",
            "wireless_desc": "\n--- Wireless Debugging Instructions ---\n1. Phone: Settings > Developer options > Wireless debugging (Enable it).\n2. Phone: Tap 'Pair device with pairing code'.\n3. You will see 'IP address & Port' and 'Wi-Fi pairing code' on your phone screen.\n----------------------------------------",
            "enter_ip_port": "Enter the IP address and port shown on your phone (e.g., 192.168.0.5:45678): ",
            "enter_pair_code": "Enter the 6-digit pairing code: ",
            "pairing": "Pairing with device...",
            "connecting": "Connecting to device...",
            "pair_fail": "Pairing failed. Please check IP:Port or Pairing code.",
            "connect_fail": "Connection failed. Please check IP:Port.",
        },
        "ko": {
            "title": "ADB 다운로드",
            "downloading": "ADB 다운로드 중...",
            "adb_exists": "ADB가 이미 존재합니다. 다시 다운로드하시겠습니까? (y/n): ",
            "start_server": "ADB 서버 시작 중...",
            "server_started": "ADB 서버 시작됨.",
            "connect_phone": "휴대폰을 USB 케이블로 컴퓨터에 연결해주세요.",
            "press_enter": "준비되면 Enter를 누르세요.",
            "check_device": "연결된 장치 확인 중...",
            "device_connected": "장치가 연결됨.",
            "device_not_connected": "장치가 연결되지 않았습니다.",
            "camera_silent": "카메라가 무음 모드로 설정되었습니다",
            "select_connection": "연결 방식을 선택하세요:\n1. USB 케이블\n2. 무선 디버깅 (Wireless Debugging)",
            "wireless_desc": "\n--- 무선 디버깅 방법 ---\n1. 휴대폰: 설정 > 개발자 옵션 > 무선 디버깅 (기능 켜기).\n2. 휴대폰: '페어링 코드로 기기 페어링'을 누르세요.\n3. 휴대폰 화면에 나오는 'IP 주소 및 포트'와 '기기 페어링 코드'를 확인하세요.\n-----------------------",
            "enter_ip_port": "휴대폰 화면의 IP 주소와 포트를 입력하세요 (예: 192.168.0.5:45678): ",
            "enter_pair_code": "6자리 페어링 코드를 입력하세요: ",
            "pairing": "기기와 페어링 중...",
            "connecting": "기기에 연결 중...",
            "pair_fail": "페어링에 실패했습니다. IP:포트 또는 페어링 코드를 확인하세요.",
            "connect_fail": "연결에 실패했습니다. IP:포트를 확인하세요.",
        }
    }
    return messages