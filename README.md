# Order Report Project

## Om projektet

Programmet läser in orderdata från en CSV-fil, kontrollerar och bearbetar datan och skapar ett antal rapporter.

Programmet:
- kontrollerar att indata innehåller de kolumner som behövs,
- hanterar saknade, felaktiga och orimliga värden,
- beräknar ordervärde och försäljning efter rabatt,
- sammanställer försäljning per produktkategori och region,
- sammanställer returer per produktkategori,
- skapar en övergripande sammanställning av orderdatan,
- sparar de färdiga rapporterna som CSV-filer i mappen `output`.

Programmet använder även logging för att visa information och varningar under körningen.

## Installation och beroenden

Projektet är utvecklat och testat med Python 3.14.

För att köra programmet behövs:
- pandas

För att köra testerna behövs även:
- pytest

Installera projektet från projektets rotmapp:

```bash
python -m pip install -e .
```

## Kör programmet

Programmet körs från projektets rotmapp med:

```bash
python -m order_report.main
```

De färdiga rapporterna sparas i mappen `output`.

## Kör testerna

De automatiska testerna körs med:

```bash
python -m pytest
```

## Projektstruktur

```text
order_report_project/
├── data/
│   └── orders.csv
├── output/
├── src/
│   └── order_report/
│       ├── __init__.py
│       ├── config.py
│       ├── main.py
│       ├── processing.py
│       └── reporting.py
├── tests/
│   ├── test_processing.py
│   └── test_reporting.py
├── code_review.md
├── pyproject.toml
└── README.md
```

`main.py` är programmets startpunkt. `processing.py` ansvarar för inläsning, validering, datarensning och beräkningar. `reporting.py` skapar och sparar rapporterna. `config.py` innehåller programmets konfiguration.

