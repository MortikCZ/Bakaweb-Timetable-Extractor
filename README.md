<div align="center">

  <h1>Bakaweb Timetable Extractor</h1>

  ![GitHub License](https://img.shields.io/github/license/MortikCZ/Bakaweb-Timetable-Extractor)
  ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/MortikCZ/Bakaweb-Timetable-Extractor)
  ![GitHub last commit](https://img.shields.io/github/last-commit/MortikCZ/Bakaweb-Timetable-Extractor)

  <p>Jednoduchý nástroj pro extrakci rozvrhu z modulu Timetable Bakawebu. Data jsou získavána v HTML formátu a následně zpracována do JSON formátu.</p>
  
</div>
<h2 align = "center">Použití</h2>

<b>UPOZORNĚNÍ! Administrátor systému Bakaláři má možnost ve veřejném rozvrhu nastavit možnost zobrazení suplování, pouze v případě platného přihlášení. V takovém případě nástroj neumožňuje získávání informací o změnách v rozvrhu.</b>

Funkce `get_timetable` má dva povinné parametry:
- `url` - URL adresa rozvrhu
- `output_file` - název souboru, do kterého se uloží rozvrh.

Vrací rozvrh ve formátu JSON.

Funkce `get_substitutions` má dva povinné parametry:
- `url` - URL adresa rozvrhu
- `output_file` - název souboru, do kterého se uloží změny.

Vrací změny v rozvrhu ve formátu JSON.

### Příklad použití
```python
import extractor

url = "https://bakalari.skola.cz/bakaweb/Timetable/Public/Permanent/Class/4U"
output_file = "timetable.json"
extractor.get_timetable(url, output_file)
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







