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
            'camera_silent' : 'Camera set to silent mode',
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
            'camera_silent' : '카메라가 무음 모드로 설정되었습니다',
        }
    }
    return messages