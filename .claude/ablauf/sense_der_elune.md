# Ablauf: Sense der Elune – VA-007 (Nebenstrang)

Entwurf 2026-11-14 von Kono (aus dem Chat), von Claude gegen warcraft.wiki.gg („Scythe of Elune“, 2026-11-14) geprüft und mit dem Gilneas-Ablauf abgeglichen. Gehört zu `.claude/ablauf/gilneas.md` und zur späteren Undercity-Seite. „Lore“ = laut Wiki, „Vorschlag“ = Idee von Claude, „Kono“ = Vorgabe von Kono. Werte und Schwellen werden beim Scripten festgelegt.

Kono, 2026-11-14: Die Val'kyr sind im Modpack noch nicht bei Sylvanas.

## Lore-Kurzfassung (geprüft)

- **Herkunft:** Belysra Starbreeze und der Druide Ralaar Fangfire schufen die Sense, indem sie einen Fangzahn Goldrinns an Belysras Stab setzten. Ralaars Druiden des Rudels wurden dadurch zu den ersten Worgen. Malfurion verbannte sie in den Smaragdgrünen Traum (unter Daral'nir), und die Sense wurde Mel'Thandris anvertraut und vergessen. Wer sie trägt, heißt „Nahlen'do“ (Meister des Fangzahns).
- **Velinde Starsong**, Nichte von Mel'Thandris, betete nach dem Dritten Krieg um Hilfe gegen die Dämonen in Eschental und Teufelswald. Ein Buch, das Fandral Staghelm in Darnassus ausgelegt hatte, führte sie zum Schrein von Mel'Thandris, wo sie die Sense fand. Sie hielt sie für Elunes Antwort. *(Korrektur zum Chat-Entwurf: Die Sense wurde ihr nicht „geschickt“, sondern gefunden; Goldrinn steckt nachweislich darin.)*
- **Wirkung:** Die Sense schwächt die Grenzen von Zeit und Raum. Velinde konnte mit Worgen sprechen und rief 30 herbei. Danach wuchs ihre Zahl ohne ihr Zutun weiter. Die Sense ist Quelle des Fluchs, kann ihn aber auch aufheben (Legion: wilde Worgen in Val'sharah).
- **Verloren:** Velinde suchte Arugal, weil er ebenfalls Worgen beschworen hatte. In Duskwood griff Varkas sie in der Mine **Roland's Doom** an; eine Kiste Dynamit explodierte, Velinde starb, und die Sense war verschüttet. Später fand Jitters sie und ließ damit Worgen nach Duskwood frei. Velindes Geist wacht dort.
- **Suchende (Lore):** der gefallene Magier Morganth, die **Dunklen Reiter** vom Gebirgspass der Totenwinde und **Alpha Prime** (Ralaar). Er war einer der Worgen, die Arugal beschworen hatte, und gründete den **Wolfskult**, um mit der Sense die übrigen Worgen zu befreien und Darnassus anzugreifen.
- **Weg nach Gilneas (Lore):** Der Wolfskult fand die Sense zuerst. Revil Kost holte sie aus der Mine. **Brink (SI:7, Sturmwind)** gab sie an den Nachtelfen Valorn Stillbough weiter, der sie wenige Tage später in den Blackwald in Gilneas brachte. Die Forsaken stahlen sie dort kurzzeitig. Belysra versuchte, Alpha Prime und den Wolfskult damit in den Traum zurückzubannen. *(Korrektur: Im Chat-Entwurf hieß es, Sylvanas habe sie im Kataklysmus in Duskwood gesucht; laut Wiki stahlen die Forsaken sie in Gilneas.)*
- **Arugal hatte die Sense nie.** Seine Worgen kamen auf anderem Weg.

## Stand zum Spielstart (etwa 10 Jahre vor dem Kataklysmus)

- Die Sense liegt verschüttet in Roland's Doom, Duskwood. **Vermutlich `STATE_RAVEN_HILL`** (Besitzer `STORMWIND`); auf der Karte prüfen. `STATE_TAINTED_FOREST` gehört größtenteils `WORMTHORN_CORRUPTION`; `GILNEAS_EXPEDITION` besitzt dort nur sechs Provinzen.
- `alpha_pack` lebt bereits in Duskwood (`STATE_DARKSHIRE`, `STATE_TRANQUIL_GARDENS_CEMESTERY`). Die Sense liegt also mitten im Worgen-Gebiet.
- `GILNEAS_EXPEDITION` ist als Protektorat **der einzige Arm von Gilneas außerhalb der Mauer** (Vorschlag: genau darüber nimmt Gilneas am Wettrennen teil, trotz `va_law_greymane_wall`).
- Zu Beginn weiß niemand, wo die Sense genau liegt.

## Wer will die Sense?

| Partei | Warum | Was sie damit tun würde |
|---|---|---|
| **Undercity** (Sylvanas) | Eigenes Ziel ohne Garrosh. Ohne Val'kyr: Macht über die Worgen statt über Leichen (Vorschlag) | Worgen beherrschen und gegen Gilneas einsetzen; Grund für den Angriff, auch ohne Thralls Segen |
| **Gilneas** über `GILNEAS_EXPEDITION`, mit Hilfe der Nachtelfen | Nachtelfen fühlen sich verantwortlich (`je_gilneas_night_elves`) | Fluch eindämmen; Ritual von Tal'doren sicherer |
| **Sturmwind** (SI:7, Brink) | Lore: holte sie aus Duskwood und gab sie den Nachtelfen. Die Mine liegt vermutlich auf Sturmwinds Land | Übergabe an die Nachtelfen oder Gilneas; Anknüpfung an das Verteidigungsbündnis mit Sturmwind (Vorschlag) |
| **Arugal** / `SHADOWFANG_KEEP` | Kono: der Einzige, der die Worgen noch halbwegs kontrolliert, weil er sich ihnen ganz hingegeben hat. Mit der Sense könnte er die Kontrolle ganz übernehmen | Mehr `alpha_pack`, schnellerer Fluch in Gilneas; eigene Eventreihe für Shadowfang Keep |
| **Alpha Prime** / `BLOODFANG_PACK` | Lore: schuf die Worgen mit, gründete den Wolfskult | Keine eigene Partei (Kono). Siehe Anmerkung unten |
| **Morganth, Dunkle Reiter, Wolfskult** | Lore-Suchende in Duskwood | Störfaktor, Event-Gegner, keine eigene Partei |

**Entschieden (Kono, 2026-11-14):** Aktiv suchen nur **Undercity, Gilneas (über `GILNEAS_EXPEDITION`) und Arugal**. Die Nachtelfen laufen über die Gilneas-Seite, weil sie in V1 keine eigenen Ziele haben. Sturmwind kommt als Event-Partner vor. Wer Morganth und die Dunklen Reiter im Mod sind, ist noch auszuarbeiten.

**Anmerkung Claude zu Alpha Prime:** Laut Wiki stirbt er erst im Kataklysmus in Gilneas (durch den Geist von Arvell). Zum Spielstart wäre er nach der Lore also noch am Leben, und der Gilneas-Ablauf nennt ihn als Anführer der Bloodfang-Worgen. Das passt trotzdem zu Konos Entscheidung, weil `BLOODFANG_PACK` ein Protektorat von `SHADOWFANG_KEEP` ist: Alpha Prime läuft unter Arugal. **Entschieden (Kono, 2026-11-14):** Alpha Prime lebt zum Spielstart. Als erster und größter Worgen hat er sehr großen Einfluss, und `BLOODFANG_PACK` soll mit ihm spielbar sein (VA-073). Vorschlag: Spielt man Bloodfang, kann man sich selbst um die Sense bemühen und so mit Arugal um die Kontrolle über die Worgen ringen.

## Mechanik-Ideen

### `je_scythe_of_elune` (Vorschlag)

- Wettrennen um die Sense: Fortschrittsbalken je aktiver Partei, gefüllt durch Expeditionen nach Duskwood (Vorbild prüfen: Vanilla-Expeditionen bzw. ein Balken je Land wie `je_divided_monarchists`).
- Wiederkehrende Events: Hinweise aus Velindes Tagebuch, Begegnung mit ihrem Geist, Überfälle der Worgen, Dunkle Reiter, Wolfskult-Rituale in der Mine.
- Wer die Sense findet, bekommt den Modifier „Träger der Sense“.
- Zeitrahmen (Vorschlag): Das Rennen endet spätestens mit dem Mauerfall bzw. Kataklysmus; in der Lore kommt die Sense erst kurz davor nach Gilneas.
- **Entschieden (Kono):** Die Sense ist vorerst ortsgebunden. Man sucht sie über Events, und wer sie findet, bekommt nur einen Modifier. Später soll sie in das geplante Artefakt-System (eigener Tab mit Abenteurern, Dungeons, sammelbaren Artefakten mit landesweiten Modifiern, VA-054) wandern.
- **Entschieden (Kono):** Die Sense dämmt den Fluch nur ein und heilt ihn nicht.

### Folgen je nach Träger (Vorschlag)

- **Undercity:** Bonus beim Angriff auf Gilneas. „Teile von `alpha_pack` kämpfen für die Forsaken“ geht in Vic3 nicht direkt, weil fremde Pops nicht für ein anderes Land kämpfen. Stattdessen: Unruhe-Modifier in Gilneas-States je nach `alpha_pack`-Anteil oder Kampfbonus für Undercity. Spannung mit Orgrimmar steigt (Thrall billigt das nicht).
- **Gilneas mit Nachtelfen:** Fluch langsamer, Rituale sicherer, Paranoia sinkt. Keine Heilung (Kono).
- **Arugal:** volle Kontrolle über die Worgen, Fluch schneller, Ausgang „Das wilde Rudel“ wahrscheinlicher. Ausgestaltung als Eventreihe für Shadowfang Keep (Kono).
- **Niemand bis zum Kataklysmus:** Sylvanas sucht weiter; lore-nah.

## Verbindung zu Gilneas (VA-007)

- Grund für den Forsaken-Angriff ohne Garrosh: Sylvanas will die Sense oder hat sie schon (Vorschlag).
- Godfreys Verrat bleibt der zweite Weg: Er lädt die Forsaken ein, und Sylvanas muss Thrall nicht fragen.
- Belysra verbindet beide Abläufe: Sie hat die Sense einst mitgeschaffen.
- **Godfreys Erweckung** (Kono, 2026-11-14, entschieden): Der Lichkönig fällt im Mod erst nach 30–40 Jahren. Sylvanas kann über Expeditionen nach Northrend an einzelne abtrünnige Val'kyr kommen (nicht die Lore-Figuren); sonst erwecken die Apotheker Godfrey. Details in `gilneas.md` unter „Offen“. Vorschlag: Expeditionen um die Sense und um Val'kyr konkurrieren in Undercity um dieselben Mittel. Das macht Sylvanas' Wahl interessant: Worgen beherrschen oder neue Forsaken erwecken.

## Offen

- In welchem State genau liegt Roland's Doom? (Karte prüfen, vermutlich `STATE_RAVEN_HILL`)
- Wer sind Morganth und die Dunklen Reiter im Mod (Tag, Event-Gegner, Ort)?
- Entschieden (Kono): Velinde ist tot und erscheint nur als Geist bzw. Event-Figur, auf die Events zurückgreifen können.
- Logging: Jeder Besitzwechsel der Sense und jedes Sense-Event wird mit `debug_log` protokolliert (Vic3-Effekt, laut `effects.log` vorhanden; Format beim Scripten festlegen).
- Undercity-Ablauf als eigene Datei, sobald Sylvanas' Motive feststehen.
