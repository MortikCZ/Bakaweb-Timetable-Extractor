import requests
from bs4 import BeautifulSoup
import json
import re
from collections import defaultdict

def login_to_bakalari(username, password, login_url):
    session = requests.Session()
    login_page = session.get(login_url)
    if login_page.status_code != 200:
        print(f"Chyba při načítání přihlašovací stránky: {login_page.status_code}")
        return None

    soup = BeautifulSoup(login_page.text, "html.parser")
    csrf_token = soup.find("input", {"name": "__RequestVerificationToken"})
    csrf_token_value = csrf_token["value"] if csrf_token else None

    login_data = {
        "username": username,
        "password": password,
        "returnUrl": "",
    }
    if csrf_token_value:
        login_data["__RequestVerificationToken"] = csrf_token_value

    response = session.post(login_url, data=login_data)
    if "Přihlásit" in response.text:
        print("Přihlášení selhalo. Zkontrolujte své přihlašovací údaje.")
        return None

    print("Přihlášení proběhlo úspěšně.")
    return session

def download_timetable(session, timetable_url):
    response = session.get(timetable_url)
    if response.status_code != 200:
        print(f"Chyba při načítání rozvrhu: {response.status_code}")
        return None

    return response.text

def extract_timetable_data(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    timetable_table = soup.find("div", id="main", class_="bk-timetable-main")

    if timetable_table:
        data_details = []
        for item in timetable_table.find_all("div", class_="day-item-hover"):
            data_detail = item.get("data-detail")
            if data_detail:
                data_details.append(json.loads(data_detail))
        return data_details
    else:
        print("Tabulka rozvrhu nebyla nalezena v HTML obsahu.")
        return []

def filter_data(data_details):
    filtered_data = defaultdict(list)
    for entry in data_details:
        subjecttext = entry.get("subjecttext", "")
        print(f"Debug: Processing subjecttext: {subjecttext}")  

        match = re.match(r"(.+?) \| (.+?) \| (.+)", subjecttext)
        if match:
            subject, date, hour = match.groups()
            print(f"Debug: Matched subject: {subject}, date: {date}, hour: {hour}")  
            filtered_data[date].append({
                "subject": subject,
                "hour": hour,
                "room": entry.get("room", ""),
                "group": entry.get("group", ""),
                "changeinfo": entry.get("changeinfo", ""),
                "removedinfo": entry.get("removedinfo", ""),
                "type": entry.get("type", ""),
                "absentinfo": entry.get("absentinfo", ""),
                "InfoAbsentName": entry.get("InfoAbsentName", "")
            })
        else:
            match = re.match(r"(.+?) \| (.+)", subjecttext)
            if match:
                date, hour = match.groups()
                print(f"Debug: Matched date: {date}, hour: {hour}")  
                filtered_data[date].append({
                    "subject": "",
                    "hour": hour,
                    "room": entry.get("room", ""),
                    "group": entry.get("group", ""),
                    "changeinfo": entry.get("changeinfo", ""),
                    "removedinfo": entry.get("removedinfo", ""),
                    "type": entry.get("type", ""),
                    "absentinfo": entry.get("absentinfo", ""),
                    "InfoAbsentName": entry.get("InfoAbsentName", "")
                })
            else:
                print(f"Debug: No match for subjecttext: {subjecttext}")
                filtered_data["unknown"].append(entry)

    return json.dumps(filtered_data, ensure_ascii=False, indent=4)

def get_timetable(login_url, timetable_url, username, password):
    session = login_to_bakalari(username, password, login_url)
    if session:
        html_content = download_timetable(session, timetable_url)
        if html_content:
            data_details = extract_timetable_data(html_content)
            return filter_data(data_details)
    return None

def get_substitutions(login_url, timetable_url, username, password):
    session = login_to_bakalari(username, password, login_url)
    if session:
        html_content = download_timetable(session, timetable_url)
        if html_content:
            data_details = extract_timetable_data(html_content)
            substitutions = [entry for entry in data_details if entry.get("changeinfo") or entry.get("removedinfo") or entry.get("type") == "absent"]
            return filter_data(substitutions)
    return None
