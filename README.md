<div align="center">

  <h1>Bakaweb Timetable Extractor</h1>

  ![GitHub License](https://img.shields.io/github/license/MortikCZ/Bakaweb-Timetable-Extractor)
  ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/MortikCZ/Bakaweb-Timetable-Extractor)
  ![GitHub last commit](https://img.shields.io/github/last-commit/MortikCZ/Bakaweb-Timetable-Extractor)

  <p>Jednoduchý nástroj pro extrakci rozvrhu z modulu Timetable Bakawebu. Data jsou získavána v HTML formátu a následně zpracována do JSON formátu.</p>
  
</div>
<h2 align = "center">Použití</h2>

**Je zapotřebí předávat funkcím vždy i přihlašovací údaje do IS Bakaláři, v některých situacích může totiž nastat to, že pokud není program přihlášen na stránce s rozvrhem, nebude mu poskytnut kompletní rozvrh včetně změn v rozvrhu ale pouze stálý rozvrh.**

### Funkce 
`get_timetable` - vrátí kompletní rozvrh v JSON formátu.

`get_substitutions` - vrátí pouze změny v rozvrhu v JSON formátu.
- parametry
  - `login_url` - přihlašovací stránka do IS Bakaláři. (např. https://bakalari.skola.cz/bakaweb/login)
  - `timetable_url` - URL rozvrhu (např. https://bakalari.skola.cz/bakaweb/Timetable/Public/Next/Class/4U)
  - `username` - přihlašovací jméno
  - `password` - přihlašovací heslo 

### Příklad použití
```python
import extractor

login_url = "https://bakalari.skola.cz/bakaweb/login"
timetable_url = "https://bakalari.skola.cz/bakaweb/Timetable/Public/Next/Class/4U"
username = "user"
password = "user"

output = app.get_substitutions(login_url, timetable_url, username, password)

print(output)
```

### Výstup
```json
{
    "po 25.11.": [
        {
            "subject": "Anglický jazyk",
            "hour": "1 (8:00 - 8:45)",
            "room": "205",
            "group": "sk_2",
            "changeinfo": "",
            "removedinfo": "",
            "type": "atom",
            "absentinfo": "",
            "InfoAbsentName": ""
        },
```







