# Code review

## 1. Print används för information och fel

**Observation:**  
Programmet använder `print()` för att visa information om programmets körning, till exempel när programmet startar, hur många rader som har lästs in och när filer har sparats. `print()` används också för att visa fel.

**Konsekvens:**  
Det blir svårt att skilja mellan vanlig information, varningar och fel. Det blir också svårare att styra hur mycket information som ska visas när programmet körs.

**Förslag:**  
Använd Pythons `logging` för information om programmets körning. Då kan olika loggnivåer som `info`, `warning` och `error` användas beroende på vilken typ av information som ska visas.


## 2. Felhanteringen är för generell och ger otydliga felmeddelanden

**Observation:**  
Nästan hela programmet ligger i ett stort `try`-block och alla fel fångas med `except Exception`. Om obligatoriska kolumner saknas skapas dessutom bara felet `"Fel data"`.

**Konsekvens:**  
Det blir svårt att förstå vad som faktiskt har gått fel. Exempelvis framgår det inte om filen saknas, om en obligatorisk kolumn saknas eller om något annat fel har inträffat.

**Förslag:**  
Hantera förväntade fel mer specifikt och ge tydligare felmeddelanden. Om en obligatorisk kolumn saknas bör felmeddelandet exempelvis tala om vilken kolumn som saknas.


## 3. Programmet har för många ansvarsområden i samma fil

**Observation:**  
Samma fil ansvarar för att läsa CSV-filen, validera data, bearbeta data, göra beräkningar, skapa rapporter och spara resultat.

**Konsekvens:**  
Programmet blir svårare att läsa, underhålla och testa. Det är exempelvis svårt att testa en beräkning separat utan att även involvera andra delar av programmet.

**Förslag:**  
Dela upp programmet i moduler och funktioner med tydliga ansvarsområden, exempelvis för datainläsning och validering, bearbetning och rapportskapande.


## 4. Det finns duplicerad kod i rapportskapandet

**Observation:**  
Rapporterna per produktkategori och region skapas med nästan samma kod. Båda grupperar data, beräknar antal order, försäljning och returer samt räknar ut `return_rate`.

**Konsekvens:**  
Samma logik behöver underhållas på flera ställen. Om beräkningen ska ändras finns det risk att den ändras på ett ställe men inte på det andra.

**Förslag:**  
Skapa en återanvändbar funktion för sammanställningen där kolumnen som ska grupperas på skickas in som argument. Funktionen kan då användas både för produktkategori och region.


## 5. Vissa variabelnamn är otydliga

**Observation:**  
Variablerna `result1` och `result2` beskriver inte vad resultaten innehåller.

**Konsekvens:**  
Det blir svårare att förstå koden eftersom man behöver läsa flera rader för att ta reda på vad variablerna representerar.

**Förslag:**  
Använd mer beskrivande namn, exempelvis `sales_by_category` och `sales_by_region`.


## 6. Programmet saknar en tydlig startpunkt

**Observation:**  
Programkoden körs direkt från filen och det finns ingen `main()`-funktion eller kontroll med `if __name__ == "__main__"`.

**Konsekvens:**  
Om filen importeras från en annan modul eller från ett test kommer programmet att börja läsa data och skapa rapporter direkt. Det ger oönskade sidoeffekter och gör koden svårare att återanvända och testa.

**Förslag:**  
Skapa en `main()`-funktion som styr programmets huvudflöde och anropa den endast när programmet körs direkt.


## 7. Sökvägarna är hårdkodade och beroende av var programmet startas

**Observation:**  
Sökvägarna `"data/orders.csv"` och `"output"` anges direkt som globala strängar i programmet.

**Konsekvens:**  
De relativa sökvägarna gör att programmet kan få problem att hitta filerna om det startas från en annan arbetskatalog. Konfigurationen är dessutom blandad med programmets övriga logik.

**Förslag:**  
Hantera sökvägarna tydligare, exempelvis med `pathlib.Path`, och samla programmets konfiguration på ett ställe. En `dataclass` kan senare användas för att representera programmets konfiguration.