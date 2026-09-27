## Reflektion

### 1. Vilka var de viktigaste problemen i originalkoden?

De viktigaste problemen var att nästan all logik låg i samma fil och att programmet hade flera olika ansvarsområden på samma ställe. Det användes `print()` för både information och fel, felhanteringen var generell och delar av rapportlogiken var duplicerad. Det saknades också en tydlig startpunkt och automatiska tester.

### 2. Vilka förändringar tycker du förbättrade programmet mest?

Uppdelningen i mindre funktioner och moduler förbättrade programmet mest. Det gjorde koden tydligare och gjorde det möjligt att testa olika delar separat. Logging och tydligare validering gjorde det också lättare att förstå vad som händer när programmet körs och när något går fel.

### 3. Varför valde du den projektstruktur du använde?

Jag ville separera olika ansvarsområden utan att skapa onödigt många filer. Databehandling och validering ligger därför i `processing.py`, rapportskapandet i `reporting.py`, konfigurationen i `config.py` och programmets huvudflöde i `main.py`. Testerna ligger separat i mappen `tests`.

### 4. Var använde du OOP/dataclass och varför passade det där?

Jag använde en dataclass, `ReportConfig`, för programmets konfiguration. Den innehåller sökvägar till indata och output samt filnamnen för rapporterna. Det passade bra eftersom dessa inställningar hör ihop och kan samlas i ett objekt i stället för att vara utspridda i programmet. `frozen=True` används eftersom konfigurationen inte ska ändras under programmets körning.

### 5. Vilka viktiga beteenden skyddar dina automatiska tester, och vilken nytta ger testerna om programmet förändras i framtiden?

Testerna kontrollerar bland annat att ordervärde och värde efter rabatt beräknas korrekt, att försäljningssammanställningar ger förväntat resultat, att saknade obligatoriska kolumner upptäcks och att rader med orimliga värden tas bort. Om programmet ändras i framtiden kan testerna upptäcka om en förändring av misstag påverkar dessa beteenden.

### 6. Vad var svårast?

Det svåraste var att avgöra hur programmet skulle delas upp och vilken logik som skulle ligga i vilken modul. Det var också en utmaning att bestämma hur felaktiga och orimliga värden skulle hanteras utan att göra valideringen onödigt komplicerad.

### 7. Vad hade du velat förbättra ytterligare om du haft mer tid?

Jag hade velat lägga till fler tester för olika typer av felaktig data och fler edge cases. Jag hade också kunnat utveckla valideringen ytterligare, exempelvis för situationer där en hel numerisk kolumn innehåller ogiltiga värden.