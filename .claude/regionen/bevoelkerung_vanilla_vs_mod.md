# Bevölkerung zum Spielstart: Vanilla gegen Victorian Azeroth

Erzeugt 2026-11-12 von Claude aus `common/history/pops` (Vanilla 1.15, Start 1836, und Mod-Repo). Nur Startbevölkerung, keine Gebäude.
„States“ = State Regions, in denen das Land Pops hat (geteilte States zählen bei jedem Besitzer). Kulturanteile je Land, Sklaven = `pop_type = slaves`.
Neu erzeugen: `python -I .claude/tools/va_pop_report.py "<Vanilla game-Ordner>" . .claude/regionen/bevoelkerung_vanilla_vs_mod.md`.

## Quel'Thalas (Mod) zum Vergleich

- Bevölkerung gesamt: **16.777.060**
- Länder mit Pops: 10; States mit Pops (State Regions): 21
- Ø je Land: 1.677.706; Median je Land: 1.060.000; Ø je State Region: 798.907
- Sklaven: 1.124.350 (6.7 %)
- Kulturen: 13; größte: sin_dorei 7.681.980, banshee 2.805.150, forest_troll 2.745.620, zombie 1.153.850, quel_dorei 989.520, warmwater_murloc 764.000, dire_troll 421.650, forsaken 89.760
- Länder nach Größe: unter 100.000: 1, 100.000–500.000: 2, 0,5–1 Mio.: 2, 1–5 Mio.: 4, 5–20 Mio.: 1

| # | Tag | Name | Pops | States | Ø je State | Sklaven | Hauptkulturen (Anteil) |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | SILVERMOON |  | 5.362.200 | 11 | 487.472 | – | sin_dorei 90 %, quel_dorei 8 %, dalaranian 1 % |
| 2 | DEATHHOLME |  | 3.959.000 | 5 | 791.800 | – | banshee 71 %, zombie 29 % |
| 3 | AMANI_TRIBE | Zul'Jarra | 2.581.620 | 2 | 1.290.810 | 37 % | forest_troll 49 %, sin_dorei 30 %, dire_troll 15 % |
| 4 | WRETCHED_BLOODELFES |  | 1.640.000 | 3 | 546.666 | – | sin_dorei 98 %, quel_dorei 2 % |
| 5 | SHADOWPINE_TRIBE |  | 1.060.000 | 3 | 353.333 | 16 % | forest_troll 79 %, sin_dorei 16 %, dire_troll 4 % |
| 6 | GRIMSCALE_MURLOCS |  | 764.000 | 3 | 254.666 | – | warmwater_murloc 100 % |
| 7 | MOSSFLAYER_TROLLS |  | 650.000 | 1 | 650.000 | – | forest_troll 100 % |
| 8 | HIGHVALE_HIGHELFES |  | 370.000 | 1 | 370.000 | – | quel_dorei 100 % |
| 9 | TRANQUILLIEN |  | 355.380 | 2 | 177.690 | – | sin_dorei 83 %, forsaken 17 % |
| 10 | DARNASSUS_OUTPOST_EK |  | 34.860 | 1 | 34.860 | – | kal_dorei 100 % |

## Vanilla 1836 – alle Länder

- Bevölkerung gesamt: **1.021.666.179**
- Länder mit Pops: 449; States mit Pops (State Regions): 676
- Ø je Land: 2.275.425; Median je Land: 240.000; Ø je State Region: 1.511.340
- Sklaven: 14.115.829 (1.4 %)
- Kulturen: 309; größte: han 298.396.368, bengali 39.119.034, japanese 32.439.361, russian 28.451.637, hindustani 25.045.149, north_german 20.520.769, yue 19.584.359, french 19.207.006
- Länder nach Größe: unter 100.000: 144, 100.000–500.000: 161, 0,5–1 Mio.: 60, 1–5 Mio.: 61, 5–20 Mio.: 16, über 20 Mio.: 7

| # | Tag | Name | Pops | States | Ø je State | Sklaven | Hauptkulturen (Anteil) |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | CHI | China | 366.405.602 | 43 | 8.521.060 | – | han 81 %, yue 5 %, min 3 % |
| 2 | BIC | East India | 110.522.582 | 21 | 5.262.980 | 2 % | bengali 35 %, hindustani 22 %, bihari 13 % |
| 3 | RUS | Russia | 50.040.768 | 73 | 685.489 | – | russian 56 %, ukrainian 19 %, byelorussian 5 % |
| 4 | FRA | France | 34.586.675 | 29 | 1.192.643 | – | french 55 %, occitan 27 %, francoprovencal 5 % |
| 5 | JAP | Japan | 32.545.935 | 11 | 2.958.721 | – | japanese 100 %, ryukyuan 0 %, han 0 % |
| 6 | GBR | Great Britain | 25.951.647 | 26 | 998.140 | – | british 54 %, irish 27 %, scottish 10 % |
| 7 | AUS | Austria | 20.754.188 | 15 | 1.383.612 | – | south_german 26 %, north_italian 23 %, czech 18 % |
| 8 | TUR | Turkey | 19.196.112 | 30 | 639.870 | 1 % | turkish 39 %, greek 16 %, bulgarian 10 % |
| 9 | KOR | Korea | 16.202.232 | 5 | 3.240.446 | – | korean 100 %, japanese 0 % |
| 10 | USA | America | 15.681.769 | 39 | 402.096 | 13 % | yankee 57 %, dixie 23 %, afro_american 15 % |
| 11 | PRU | Prussia | 14.062.517 | 13 | 1.081.732 | – | north_german 85 %, polish 13 %, lithuanian 1 % |
| 12 | SPA | Spain | 11.905.901 | 15 | 793.726 | – | spanish 63 %, catalan 16 %, galician 12 % |
| 13 | HYD | Hyderabad | 10.855.454 | 2 | 5.427.727 | 4 % | marathi 34 %, telegu 32 %, deccani 23 % |
| 14 | DEI | East Indies | 9.512.372 | 11 | 864.761 | 2 % | javan 83 %, moluccan 10 %, sumatran 3 % |
| 15 | HUN | Hungary | 9.419.768 | 7 | 1.345.681 | – | hungarian 42 %, slovak 17 %, south_german 15 % |
| 16 | EGY | Egypt | 8.925.808 | 17 | 525.047 | 6 % | misri 44 %, mashriqi 18 %, sudanese 11 % |
| 17 | PAN | Punjab | 8.105.904 | 3 | 2.701.968 | – | panjabi 84 %, pashtun 11 %, pahari 2 % |
| 18 | SIC | Two Sicilies | 7.032.680 | 5 | 1.406.536 | – | south_italian 100 % |
| 19 | MEX | Mexico | 6.950.447 | 22 | 315.929 | – | mexican 57 %, nahua 18 %, mayan 7 % |
| 20 | PER | Persia | 6.618.409 | 12 | 551.534 | 1 % | persian 51 %, azerbaijani 14 %, mazanderani 13 % |
| 21 | DAI | Dai Nam | 6.570.909 | 4 | 1.642.727 | 2 % | vietnamese 89 %, miao 3 %, khmer 3 % |
| 22 | POR | Portugal | 6.308.640 | 19 | 332.033 | 0 % | portuguese 62 %, marathi 7 %, yue 6 % |
| 23 | SOK | Sokoto | 5.428.321 | 5 | 1.085.664 | 14 % | hausa 53 %, equatorial_bantu 20 %, fulbe 18 % |
| 24 | AWA | Awadh | 4.824.221 | 1 | 4.824.221 | – | avadhi 100 %, panjabi 0 % |
| 25 | POL | Poland | 4.747.982 | 4 | 1.186.995 | – | polish 75 %, ashkenazi 13 %, east_german 4 % |
| 26 | NEP | Nepal | 4.242.426 | 1 | 4.242.426 | – | nepali 66 %, tibetan 18 %, bihari 16 % |
| 27 | BAV | Bavaria | 4.175.788 | 3 | 1.391.929 | – | south_german 100 %, ashkenazi 0 % |
| 28 | BEL | Belgium | 4.147.468 | 3 | 1.382.489 | – | flemish 55 %, wallonian 40 %, dutch 4 % |
| 29 | BRZ | Brazil | 4.040.571 | 14 | 288.612 | 25 % | afro_brazilian 58 %, nordestino 18 %, brazilian 14 % |
| 30 | SIA | Siam | 3.866.645 | 6 | 644.440 | 3 % | thai 55 %, lao 18 %, malay 11 % |
| 31 | MYS | Mysore | 3.798.574 | 1 | 3.798.574 | – | kannada 91 %, deccani 8 %, tamil 1 % |
| 32 | SAR | Sardinia-Piedmont | 3.629.072 | 4 | 907.268 | – | north_italian 74 %, south_italian 14 %, francoprovencal 5 % |
| 33 | BUR | Burma | 3.473.474 | 4 | 868.368 | 4 % | burmese 68 %, shan 17 %, karen 7 % |
| 34 | MOR | Morocco | 3.244.592 | 4 | 811.148 | 5 % | maghrebi 67 %, berber 23 %, bambara 5 % |
| 35 | NAG | Nagpur | 3.148.803 | 1 | 3.148.803 | – | chhattisgarhi 34 %, marathi 27 %, gondi 17 % |
| 36 | TIB | Tibet | 2.860.146 | 3 | 953.382 | – | tibetan 93 %, han 5 %, kachin 2 % |
| 37 | SWE | Sweden | 2.797.184 | 5 | 559.436 | – | swedish 97 %, finnish 2 %, sami 1 % |
| 38 | NET | Netherlands | 2.772.765 | 6 | 462.127 | – | dutch 92 %, akan 2 %, ashkenazi 2 % |
| 39 | PAP | Rome | 2.594.064 | 3 | 864.688 | – | south_italian 69 %, north_italian 31 % |
| 40 | PHI | Philippines | 2.575.279 | 4 | 643.819 | – | visayan 41 %, tagalog 35 %, ilocano 19 % |
| 41 | IBO | Igbo | 2.346.000 | 1 | 2.346.000 | 6 % | ibo 49 %, equatorial_bantu 32 %, ibibio 19 % |
| 42 | WAL | Wallachia | 2.227.865 | 1 | 2.227.865 | 5 % | romanian 100 % |
| 43 | KAB | Kabul | 2.163.084 | 4 | 540.771 | 6 % | pashtun 65 %, tajik 15 %, panjabi 9 % |
| 44 | TRS | Transylvania | 2.062.404 | 2 | 1.031.202 | – | romanian 54 %, hungarian 21 %, south_german 12 % |
| 45 | MAS | Mascara | 2.009.192 | 2 | 1.004.596 | 2 % | maghrebi 57 %, berber 40 %, bambara 2 % |
| 46 | SWI | Switzerland | 1.966.164 | 2 | 983.082 | – | alemannic 70 %, francoprovencal 21 %, north_italian 10 % |
| 47 | SIN | Sindh | 1.960.004 | 1 | 1.960.004 | 2 % | sindi 98 %, lacustrine_bantu 2 % |
| 48 | MAD | Madagascar | 1.942.904 | 2 | 971.452 | 3 % | malagasy 100 % |
| 49 | HAN | Hanover | 1.846.996 | 3 | 615.665 | – | north_german 99 %, ashkenazi 0 %, dutch 0 % |
| 50 | JAI | Dhundhar | 1.821.010 | 1 | 1.821.010 | – | rajput 88 %, hindustani 6 %, gujarati 6 % |
| 51 | WUR | Württemberg | 1.719.750 | 1 | 1.719.750 | – | south_german 89 %, alemannic 11 % |
| 52 | UCA | Central America | 1.681.471 | 6 | 280.245 | – | central_american 80 %, mayan 19 %, miskito 0 % |
| 53 | BEN | Benin | 1.677.788 | 1 | 1.677.788 | 11 % | edo 29 %, tiv 22 %, ibo 19 % |
| 54 | SAX | Saxony | 1.671.500 | 1 | 1.671.500 | – | north_german 88 %, sorb 12 %, ashkenazi 0 % |
| 55 | TUS | Tuscany | 1.632.396 | 1 | 1.632.396 | – | north_italian 100 % |
| 56 | KOK | Kokand | 1.619.460 | 4 | 404.865 | 4 % | uzbek 45 %, kirgiz 26 %, tajik 18 % |
| 57 | CLM | Colombia | 1.618.606 | 6 | 269.767 | 5 % | north_andean 57 %, afro_caribeno 20 %, amazonian 6 % |
| 58 | UBD | United Baltic Provinces | 1.577.759 | 4 | 394.439 | – | latvian 46 %, estonian 37 %, east_german 7 % |
| 59 | OYO | Oyo | 1.576.004 | 1 | 1.576.004 | 2 % | yoruba 98 %, fon 2 % |
| 60 | OMA | Oman | 1.550.241 | 7 | 221.463 | 7 % | lacustrine_bantu 40 %, swahili 30 %, bedouin 14 % |
| 61 | CON | Constantine | 1.488.235 | 1 | 1.488.235 | 2 % | berber 81 %, maghrebi 17 %, bambara 2 % |
| 62 | BUK | Bukhara | 1.477.596 | 4 | 369.399 | 11 % | uzbek 56 %, tajik 21 %, persian 8 % |
| 63 | GWA | Gwalior | 1.450.619 | 2 | 725.309 | – | rajput 47 %, bundeli 36 %, marathi 17 % |
| 64 | FIN | Finland | 1.444.214 | 6 | 240.702 | – | finnish 85 %, swedish 14 %, sami 1 % |
| 65 | MOS | Mossi | 1.427.196 | 1 | 1.427.196 | 1 % | mossi 58 %, mande 30 %, fulbe 6 % |
| 66 | DEN | Denmark | 1.410.686 | 8 | 176.335 | – | danish 85 %, icelandic 4 %, afro_caribbean 3 % |
| 67 | BOL | Bolivia | 1.394.398 | 8 | 174.299 | – | quechua 35 %, aimara 33 %, south_andean 23 % |
| 68 | MOL | Moldavia | 1.358.409 | 1 | 1.358.409 | 9 % | romanian 100 % |
| 69 | TUN | Tunis | 1.315.008 | 1 | 1.315.008 | 2 % | maghrebi 89 %, berber 8 %, sephardic 1 % |
| 70 | BAD | Baden | 1.301.400 | 1 | 1.301.400 | – | south_german 89 %, alemannic 11 %, ashkenazi 0 % |
| 71 | KAS | Kashmir | 1.270.851 | 1 | 1.270.851 | – | kashmiri 93 %, panjabi 3 %, pashtun 3 % |
| 72 | JOD | Marwar | 1.252.870 | 1 | 1.252.870 | – | rajput 97 %, gujarati 3 % |
| 73 | MSN | Massina | 1.247.500 | 2 | 623.750 | 3 % | bambara 37 %, mande 36 %, songhai 13 % |
| 74 | NOR | Norway | 1.236.860 | 3 | 412.286 | – | norwegian 95 %, sami 3 %, finnish 2 % |
| 75 | ASM | Assam | 1.212.183 | 1 | 1.212.183 | 4 % | assamese 88 %, naga 12 % |
| 76 | BCE | Ceylon | 1.199.900 | 1 | 1.199.900 | 2 % | sinhala 77 %, tamil 18 %, mashriqi 3 % |
| 77 | CRO | Croatia | 1.194.220 | 2 | 597.110 | – | croat 71 %, serb 19 %, south_german 5 % |
| 78 | ASH | Ashanti | 1.188.308 | 2 | 594.154 | 7 % | akan 74 %, fon 11 %, ewe 10 % |
| 79 | GZA | Gaza | 1.134.443 | 2 | 567.221 | – | tonga 28 %, nguni 24 %, shona 22 % |
| 80 | BER | Baroda | 1.118.767 | 1 | 1.118.767 | – | gujarati 91 %, marathi 5 %, rajput 3 % |
| 81 | KAN | Kandahar | 1.088.284 | 6 | 181.380 | 5 % | pashtun 70 %, baluchi 9 %, tajik 7 % |
| 82 | TRA | Travancore | 1.055.033 | 1 | 1.055.033 | – | malayalam 96 %, tamil 4 % |
| 83 | KHI | Khiva | 1.043.388 | 3 | 347.796 | 24 % | uzbek 41 %, turkmen 30 %, persian 22 % |
| 84 | VNZ | Venezuela | 1.007.847 | 4 | 251.961 | 8 % | north_andean 75 %, afro_caribeno 21 %, amazonian 3 % |
| 85 | HAI | Haiti | 989.800 | 2 | 494.900 | – | afro_antillean 85 %, caribeno 11 %, afro_caribeno 3 % |
| 86 | ECU | Ecuador | 965.625 | 2 | 482.812 | 9 % | quechua 45 %, north_andean 34 %, afro_caribeno 16 % |
| 87 | CHL | Chile | 964.904 | 3 | 321.634 | – | south_andean 95 %, patagonian 5 %, afro_caribeno 0 % |
| 88 | ZAI | Azal | 947.800 | 1 | 947.800 | 3 % | yemenite 90 %, bedouin 5 %, sudanese 3 % |
| 89 | GRE | Greece | 939.992 | 3 | 313.330 | – | greek 100 % |
| 90 | HER | Herat | 932.107 | 2 | 466.053 | 5 % | persian 54 %, pashtun 22 %, tajik 13 % |
| 91 | CMI | Chiang Mai | 924.200 | 1 | 924.200 | 3 % | thai 57 %, shan 32 %, lao 10 % |
| 92 | MRV | Maravi | 923.300 | 2 | 461.650 | 1 % | yao 31 %, chewa 18 %, makua 18 % |
| 93 | CUB | Cuba | 904.778 | 3 | 301.592 | 45 % | afro_caribeno 57 %, caribeno 37 %, spanish 4 % |
| 94 | BAG | Rewah | 892.879 | 1 | 892.879 | – | bageli 77 %, avadhi 15 %, hindustani 8 % |
| 95 | GJM | Gojjam | 891.000 | 1 | 891.000 | 8 % | oromo 52 %, amhara 40 %, kikuyu 8 % |
| 96 | NPU | North Peru | 866.600 | 3 | 288.866 | 1 % | quechua 46 %, south_andean 41 %, amazonian 8 % |
| 97 | BOR | Bornu | 858.594 | 4 | 214.648 | 3 % | kanuri 63 %, hausa 15 %, fulbe 8 % |
| 98 | BAL | Bali | 837.892 | 1 | 837.892 | 2 % | balinese 76 %, moluccan 24 % |
| 99 | ARG | Argentina | 813.812 | 8 | 101.726 | 2 % | platinean 85 %, afro_caribeno 5 %, guarani 5 % |
| 100 | KON | Kongo | 809.882 | 2 | 404.941 | 6 % | bakongo 65 %, fluvian_bantu 25 %, kavango_bantu 10 % |
| 101 | KBA | Kuba | 804.000 | 1 | 804.000 | 10 % | fluvian_bantu 99 %, lunda 1 % |
| 102 | TRI | Tripolitania | 772.744 | 2 | 386.372 | 4 % | bedouin 46 %, maghrebi 40 %, berber 8 % |
| 103 | BUN | Orchha | 770.983 | 1 | 770.983 | – | bundeli 89 %, hindustani 11 % |
| 104 | BUG | Buganda | 767.188 | 1 | 767.188 | 3 % | lacustrine_bantu 62 %, baganda 38 % |
| 105 | PPU | Papua | 752.098 | 2 | 376.049 | – | melanesian 100 % |
| 106 | BGM | Begemder | 750.720 | 1 | 750.720 | 12 % | amhara 65 %, oromo 30 %, kikuyu 5 % |
| 107 | SAT | Satara | 742.713 | 1 | 742.713 | – | marathi 86 %, kannada 9 %, deccani 4 % |
| 108 | FNG | Fang | 730.792 | 2 | 365.396 | 10 % | fang 67 %, equatorial_bantu 33 % |
| 109 | HES | Hesse | 729.108 | 1 | 729.108 | – | north_german 99 %, ashkenazi 1 % |
| 110 | SER | Serbia | 719.909 | 2 | 359.954 | – | serb 89 %, romanian 10 %, albanian 0 % |
| 111 | CAM | Cambodia | 714.412 | 1 | 714.412 | 6 % | khmer 93 %, yue 3 %, champa 2 % |
| 112 | PTA | Patiala | 714.136 | 2 | 357.068 | – | panjabi 93 %, hindustani 7 % |
| 113 | SPC | Carlist Spain | 697.775 | 3 | 232.591 | – | spanish 47 %, basque 42 %, catalan 11 % |
| 114 | SPU | South Peru | 681.108 | 3 | 227.036 | 0 % | quechua 57 %, south_andean 22 %, aimara 17 % |
| 115 | DLA | Duala | 680.000 | 1 | 680.000 | 12 % | equatorial_bantu 100 % |
| 116 | SHW | Shewa | 676.898 | 1 | 676.898 | 3 % | oromo 60 %, amhara 37 %, kikuyu 3 % |
| 117 | CIR | Circassia | 660.809 | 2 | 330.404 | – | circassian 90 %, abkhazian 8 %, caucasian_turk 2 % |
| 118 | MEW | Mewar | 659.983 | 1 | 659.983 | – | rajput 90 %, gujarati 10 % |
| 119 | TGR | Tigray | 648.719 | 1 | 648.719 | 10 % | tigray 46 %, amhara 44 %, kikuyu 10 % |
| 120 | MOD | Modena | 648.400 | 1 | 648.400 | – | north_italian 100 % |
| 121 | HEK | Hesse-Kassel | 633.288 | 1 | 633.288 | – | north_german 99 %, ashkenazi 1 % |
| 122 | SHS | Shan | 627.800 | 1 | 627.800 | – | shan 89 %, karen 11 % |
| 123 | SAF | South Africa | 625.500 | 3 | 208.500 | – | khoisan 46 %, boer 19 %, british 15 % |
| 124 | BNG | Bangala | 625.200 | 1 | 625.200 | 5 % | mongo 100 % |
| 125 | LBA | Luba | 618.416 | 3 | 206.138 | 9 % | fluvian_bantu 60 %, luba 40 % |
| 126 | MAK | Makran | 589.507 | 2 | 294.753 | 6 % | baluchi 94 %, lacustrine_bantu 3 %, persian 1 % |
| 127 | NYM | Unyamwezi | 585.900 | 1 | 585.900 | 9 % | nyamwezi 54 %, lacustrine_bantu 34 %, luo 8 % |
| 128 | QWR | Qwara | 585.520 | 1 | 585.520 | 11 % | amhara 89 %, kikuyu 7 %, oromo 4 % |
| 129 | KZH | Kishi Zhuz | 584.122 | 6 | 97.353 | 0 % | kazak 65 %, russian 18 %, bashkir 11 % |
| 130 | IND | Indore | 578.753 | 2 | 289.376 | – | rajput 63 %, marathi 27 %, bundeli 10 % |
| 131 | KAL | Kalat | 577.392 | 1 | 577.392 | 5 % | baluchi 90 %, pashtun 6 %, lacustrine_bantu 4 % |
| 132 | SAK | Siak | 572.281 | 2 | 286.140 | 6 % | sumatran 88 %, batak 9 %, yue 3 % |
| 133 | QUE | Quebec | 555.200 | 1 | 555.200 | – | franco_canadian 99 %, anglo_canadian 1 %, cree 1 % |
| 134 | ALW | Alwar | 535.462 | 1 | 535.462 | – | rajput 90 %, hindustani 6 %, panjabi 4 % |
| 135 | BAS | Bastar | 534.735 | 1 | 534.735 | 9 % | gondi 91 %, chhattisgarhi 8 %, deccani 2 % |
| 136 | COC | Cochin | 530.451 | 1 | 530.451 | – | malayalam 96 %, tamil 4 % |
| 137 | HDJ | Hedjaz | 526.700 | 2 | 263.350 | 7 % | mashriqi 47 %, bedouin 30 %, yemenite 15 % |
| 138 | MDK | Mandinka | 518.709 | 3 | 172.903 | 2 % | mande 70 %, kissi 16 %, dyula 10 % |
| 139 | KHP | Kolhapur | 517.691 | 1 | 517.691 | – | marathi 84 %, kannada 10 %, deccani 6 % |
| 140 | MUG | Hindustan | 514.378 | 1 | 514.378 | – | hindustani 93 %, panjabi 7 % |
| 141 | RWD | Rwanda | 511.996 | 1 | 511.996 | 2 % | ruanda 100 % |
| 142 | GAR | Garhwal | 511.956 | 2 | 255.978 | – | pahari 92 %, hindustani 8 % |
| 143 | TRM | Turkmenia | 510.125 | 4 | 127.531 | 11 % | turkmen 82 %, persian 18 %, kazak 0 % |
| 144 | MND | Mindanao | 506.235 | 1 | 506.235 | – | lumad 89 %, moro 10 %, visayan 1 % |
| 145 | MEC | Mecklenburg | 493.998 | 1 | 493.998 | – | north_german 99 %, ashkenazi 1 % |
| 146 | HDY | Hadiya | 488.800 | 1 | 488.800 | – | oromo 66 %, amhara 34 % |
| 147 | SUR | Surguja | 482.410 | 1 | 482.410 | – | chhattisgarhi 61 %, avadhi 20 %, gondi 19 % |
| 148 | PAR | Parma | 472.004 | 1 | 472.004 | – | north_italian 100 % |
| 149 | BRD | Burundi | 468.004 | 1 | 468.004 | 3 % | rundi 100 % |
| 150 | KZM | Kazembe | 468.004 | 2 | 234.002 | 5 % | lunda 47 %, fluvian_bantu 46 %, chewa 7 % |
| 151 | MNB | Mangbetu | 468.000 | 1 | 468.000 | 7 % | fluvian_bantu 100 % |
| 152 | ZND | Azande | 461.512 | 2 | 230.756 | 7 % | azande 95 %, equatorial_bantu 5 % |
| 153 | ARB | Arabistan | 458.498 | 1 | 458.498 | 2 % | mashriqi 85 %, persian 7 %, luri 4 % |
| 154 | KFA | Kaffa | 450.656 | 1 | 450.656 | 4 % | oromo 71 %, amhara 13 %, sidama 11 % |
| 155 | SLW | Sulawesi | 449.196 | 1 | 449.196 | – | moluccan 100 % |
| 156 | LND | Lunda | 448.796 | 2 | 224.398 | 5 % | lunda 86 %, ovimbundu 9 %, kavango_bantu 5 % |
| 157 | KRU | Kru | 442.135 | 2 | 221.067 | 4 % | kru 98 %, bassa 2 % |
| 158 | JOH | Johore | 438.004 | 1 | 438.004 | 3 % | malay 94 %, yue 6 % |
| 159 | BRN | Borana | 432.604 | 1 | 432.604 | 3 % | oromo 79 %, sidama 18 %, kikuyu 3 % |
| 160 | FTJ | Futa Jallon | 421.360 | 1 | 421.360 | 6 % | fulbe 72 %, mande 28 % |
| 161 | OZH | Orta Zhuz | 412.122 | 4 | 103.030 | – | kazak 92 %, russian 5 %, tatar 1 % |
| 162 | ONT | Ontario | 410.796 | 1 | 410.796 | – | anglo_canadian 89 %, franco_canadian 6 %, cree 3 % |
| 163 | HOL | Holstein | 404.604 | 1 | 404.604 | – | north_german 95 %, danish 5 %, ashkenazi 0 % |
| 164 | WLG | Welega | 403.604 | 1 | 403.604 | 12 % | oromo 66 %, amhara 34 % |
| 165 | MNP | Manipur | 403.584 | 1 | 403.584 | – | manipuri 83 %, naga 10 %, lushai 7 % |
| 166 | DAH | Dahomey | 402.812 | 1 | 402.812 | 11 % | fon 71 %, yoruba 16 %, akan 9 % |
| 167 | NAS | Nassau | 402.404 | 1 | 402.404 | – | north_german 99 %, ashkenazi 1 % |
| 168 | HAU | Gobir | 400.137 | 1 | 400.137 | 7 % | hausa 42 %, equatorial_bantu 24 %, tuareg 12 % |
| 169 | OGD | Ogaden | 388.483 | 1 | 388.483 | – | somali 100 % |
| 170 | EWE | Ewe | 383.996 | 1 | 383.996 | 7 % | ewe 100 % |
| 171 | BIK | Bikaner | 377.748 | 1 | 377.748 | – | rajput 98 %, panjabi 2 % |
| 172 | LIB | Liberia | 377.210 | 1 | 377.210 | – | kru 61 %, bassa 30 %, mande 5 % |
| 173 | KNO | Kurnool | 367.135 | 1 | 367.135 | – | telegu 81 %, deccani 12 %, kannada 6 % |
| 174 | HHE | Hehe | 363.904 | 1 | 363.904 | 6 % | yao 60 %, makua 18 %, nyamwezi 16 % |
| 175 | MJT | Majerteen | 363.440 | 1 | 363.440 | 9 % | somali 84 %, swahili 13 %, oromo 2 % |
| 176 | HAR | Harar | 361.610 | 1 | 361.610 | 8 % | oromo 38 %, somali 35 %, amhara 28 % |
| 177 | LAD | Ladakh | 361.588 | 1 | 361.588 | – | tibetan 96 %, kashmiri 3 %, pahari 2 % |
| 178 | PRA | Grão-Pará | 356.583 | 2 | 178.291 | 19 % | afro_brazilian 41 %, amazonic 35 %, amazonian 23 % |
| 179 | ACE | Aceh | 354.107 | 1 | 354.107 | 3 % | sumatran 72 %, batak 25 %, yue 3 % |
| 180 | JHN | Jhansi | 353.646 | 1 | 353.646 | – | bundeli 89 %, hindustani 11 % |
| 181 | YKA | Yaka | 348.000 | 1 | 348.000 | 7 % | bakongo 52 %, lunda 48 % |
| 182 | KNG | Kong | 344.008 | 2 | 172.004 | 10 % | senufo 28 %, mande 27 %, dyula 24 % |
| 183 | DFT | Dar Fertit | 342.840 | 1 | 342.840 | 4 % | azande 64 %, luo 18 %, nilotic 14 % |
| 184 | JUN | Junagadh | 342.028 | 1 | 342.028 | – | gujarati 94 %, pathan 2 %, sindi 2 % |
| 185 | DNK | Dinka | 340.360 | 1 | 340.360 | 6 % | dinka 43 %, nilotic 25 %, luo 15 % |
| 186 | SSU | Susu | 340.000 | 1 | 340.000 | 5 % | mande 93 %, dyula 5 %, fulbe 2 % |
| 187 | SCH | Schleswig | 336.404 | 1 | 336.404 | – | north_german 59 %, danish 41 % |
| 188 | HMB | Hemba | 336.000 | 1 | 336.000 | 4 % | fluvian_bantu 100 % |
| 189 | MNC | Manica | 330.000 | 2 | 165.000 | 5 % | shona 78 %, lacustrine_bantu 13 %, sena 9 % |
| 190 | WAD | Wadai | 320.060 | 2 | 160.030 | 6 % | fur 44 %, equatorial_bantu 37 %, bedouin 18 % |
| 191 | PDI | Pedi | 320.000 | 1 | 320.000 | – | sotho 100 % |
| 192 | KOT | Kotah | 318.026 | 1 | 318.026 | – | rajput 95 %, gujarati 5 % |
| 193 | LUA | Luang Prabang | 315.473 | 1 | 315.473 | 5 % | lao 72 %, khmu 21 %, miao 7 % |
| 194 | BHO | Bhopal | 310.802 | 1 | 310.802 | – | bundeli 55 %, rajput 39 %, pashtun 7 % |
| 195 | CHC | Chechnya | 310.309 | 2 | 155.154 | – | dagestani 71 %, chechen 29 % |
| 196 | TID | Tidore | 310.179 | 3 | 103.393 | 12 % | moluccan 76 %, melanesian 24 % |
| 197 | KKY | Kikuyu | 308.304 | 1 | 308.304 | 7 % | kikuyu 49 %, lacustrine_bantu 46 %, maasai 5 % |
| 198 | MTB | Ndebele | 307.800 | 1 | 307.800 | – | sotho 51 %, tswana 22 %, nguni 18 % |
| 199 | DAK | Dar al Kuti | 303.400 | 1 | 303.400 | 5 % | equatorial_bantu 93 %, sara 4 %, fur 1 % |
| 200 | ZUL | Zulu | 301.900 | 1 | 301.900 | 5 % | zulu 89 %, xhosa 11 %, boer 1 % |
| 201 | BHV | Bhavnagar | 297.998 | 1 | 297.998 | – | gujarati 94 %, marathi 4 %, sindi 1 % |
| 202 | BOB | Bobangi | 296.212 | 2 | 148.106 | 5 % | mongo 85 %, fluvian_bantu 8 %, bakongo 7 % |
| 203 | PCO | Puerto Rico | 294.668 | 1 | 294.668 | 11 % | afro_caribeno 52 %, caribeno 46 %, spanish 2 % |
| 204 | MGD | Maguindanao | 292.135 | 1 | 292.135 | 3 % | moro 71 %, lumad 21 %, bornean 7 % |
| 205 | AIT | Ait Abbas | 289.848 | 1 | 289.848 | 3 % | berber 90 %, maghrebi 6 %, bambara 3 % |
| 206 | CHT | Chitral | 285.154 | 2 | 142.577 | 4 % | pashtun 53 %, kho 33 %, panjabi 8 % |
| 207 | SIL | Sierra Leone | 284.893 | 4 | 71.223 | – | mande 32 %, akan 30 %, fulbe 13 % |
| 208 | PRG | Paraguay | 280.586 | 2 | 140.293 | 4 % | platinean 46 %, guarani 43 %, afro_caribeno 10 % |
| 209 | NSW | New South Wales | 265.471 | 5 | 53.094 | – | australian 47 %, irish 30 %, aborigine 21 % |
| 210 | ARS | Arsiland | 265.200 | 1 | 265.200 | 7 % | oromo 93 %, kikuyu 7 % |
| 211 | KUT | Kutch | 265.073 | 1 | 265.073 | – | gujarati 92 %, sindi 4 %, marathi 3 % |
| 212 | HBC | Hudson’s Bay Company | 258.827 | 9 | 28.758 | – | metis 21 %, athabaskan 20 %, cree 18 % |
| 213 | OLD | Oldenburg | 257.696 | 1 | 257.696 | – | north_german 100 % |
| 214 | WLT | Wolaita | 248.600 | 1 | 248.600 | 3 % | sidama 97 %, kikuyu 3 % |
| 215 | BRG | Borgu | 247.088 | 2 | 123.544 | 3 % | mande 69 %, fulbe 20 %, songhai 11 % |
| 216 | BNY | Bunyoro | 246.000 | 1 | 246.000 | 5 % | baganda 85 %, lacustrine_bantu 15 % |
| 217 | HRO | Herero | 245.996 | 2 | 122.998 | 9 % | herero 81 %, khoisan 14 %, kavango_bantu 4 % |
| 218 | MYB | Mayurbhanj | 245.800 | 1 | 245.800 | – | oriya 72 %, chhattisgarhi 28 % |
| 219 | JEY | Jeypore | 244.520 | 1 | 244.520 | – | oriya 64 %, telegu 17 %, gondi 10 % |
| 220 | NUE | Nuer | 244.004 | 1 | 244.004 | 6 % | nuer 77 %, nuba 21 %, sudanese 2 % |
| 221 | COO | Cooch Behar | 243.388 | 1 | 243.388 | 9 % | bengali 100 % |
| 222 | ANK | Ankole | 242.000 | 1 | 242.000 | 4 % | baganda 74 %, lacustrine_bantu 26 % |
| 223 | PUD | Pudukottai | 241.668 | 1 | 241.668 | – | tamil 97 %, telegu 2 %, kannada 1 % |
| 224 | KRT | Kaarta | 240.000 | 1 | 240.000 | 6 % | fulbe 58 %, bambara 28 %, mande 13 % |
| 225 | LGA | Lega | 240.000 | 1 | 240.000 | 5 % | fluvian_bantu 100 % |
| 226 | SEL | Selangor | 238.000 | 1 | 238.000 | 3 % | malay 91 %, yue 9 % |
| 227 | SKM | Usukuma | 237.996 | 1 | 237.996 | 6 % | sukuma 94 %, nyamwezi 6 % |
| 228 | DFR | Darfur | 235.992 | 1 | 235.992 | 6 % | fur 84 %, dinka 12 %, bedouin 3 % |
| 229 | WEI | Saxe-Weimar | 233.840 | 1 | 233.840 | – | north_german 100 %, ashkenazi 0 % |
| 230 | NAW | Nawanagar | 233.775 | 1 | 233.775 | – | gujarati 98 %, marathi 1 %, sindi 1 % |
| 231 | IDA | Idar | 232.412 | 1 | 232.412 | – | gujarati 96 %, marathi 4 % |
| 232 | BHW | Bahawalpur | 229.287 | 1 | 229.287 | 5 % | panjabi 94 %, rajput 3 %, sindi 3 % |
| 233 | LNG | Loango | 228.400 | 2 | 114.200 | 12 % | equatorial_bantu 53 %, bakongo 30 %, fluvian_bantu 12 % |
| 234 | BRA | Brunswick | 224.400 | 1 | 224.400 | – | north_german 100 % |
| 235 | KRA | Krakow | 224.400 | 1 | 224.400 | – | polish 77 %, ashkenazi 14 %, ukrainian 7 % |
| 236 | GLD | Geledi | 222.280 | 1 | 222.280 | 9 % | somali 75 %, swahili 18 %, oromo 7 % |
| 237 | SGU | Segou | 220.000 | 1 | 220.000 | 51 % | mande 51 %, bambara 31 %, fulbe 18 % |
| 238 | MNL | Mingrelia | 216.000 | 1 | 216.000 | – | georgian 100 % |
| 239 | OVM | Ovimbundu | 215.996 | 1 | 215.996 | 3 % | ovimbundu 97 %, kavango_bantu 3 % |
| 240 | BRU | Brunei | 212.392 | 1 | 212.392 | 8 % | dayak 49 %, bornean 47 %, yue 3 % |
| 241 | BMB | Bemba | 211.344 | 2 | 105.672 | 6 % | lacustrine_bantu 64 %, lunda 17 %, nguni 9 % |
| 242 | ACH | Acholi | 208.800 | 1 | 208.800 | 3 % | luo 100 % |
| 243 | CHK | Chokwe | 208.200 | 1 | 208.200 | 5 % | kavango_bantu 48 %, ovimbundu 39 %, lunda 10 % |
| 244 | MSK | Maseko | 207.396 | 1 | 207.396 | 2 % | shona 53 %, lacustrine_bantu 31 %, nguni 11 % |
| 245 | BND | Bundu | 204.400 | 1 | 204.400 | 5 % | mande 47 %, wolof 32 %, bambara 22 % |
| 246 | TSW | Tswana | 204.004 | 2 | 102.002 | 10 % | tswana 94 %, herero 4 %, nguni 2 % |
| 247 | PNI | Piratini | 202.943 | 1 | 202.943 | 21 % | sulista 57 %, afro_brazilian 23 %, guarani 20 % |
| 248 | NVS | Nova Scotia | 201.572 | 1 | 201.572 | – | anglo_canadian 98 %, afro_american 2 %, algonquian 1 % |
| 249 | TRK | Turkana | 201.196 | 1 | 201.196 | 8 % | nilotic 84 %, kikuyu 16 % |
| 250 | MSH | Mashona | 200.000 | 1 | 200.000 | 8 % | shona 75 %, lacustrine_bantu 25 % |
| 251 | UZH | Uly Zhuz | 196.745 | 1 | 196.745 | – | kazak 86 %, kirgiz 11 %, uzbek 3 % |
| 252 | ANH | Anhalt | 196.008 | 1 | 196.008 | – | north_german 100 % |
| 253 | NEJ | Nejd | 195.836 | 2 | 97.918 | 6 % | bedouin 94 %, sudanese 5 %, circassian 0 % |
| 254 | MTP | Mutapa | 195.000 | 2 | 97.500 | 5 % | shona 78 %, lacustrine_bantu 15 %, sena 6 % |
| 255 | RYU | Ryukyu | 193.495 | 1 | 193.495 | – | ryukyuan 100 %, han 0 %, japanese 0 % |
| 256 | HAW | Hawaii | 192.104 | 1 | 192.104 | – | hawaiian 73 %, han 26 %, yankee 0 % |
| 257 | ION | Ionian Islands | 188.420 | 1 | 188.420 | – | greek 99 %, sephardic 1 %, british 0 % |
| 258 | FTR | Futa Toro | 180.400 | 2 | 90.200 | 13 % | fulbe 55 %, bidan 20 %, haratin 18 % |
| 259 | SUL | Sulu | 178.761 | 3 | 59.587 | 5 % | moro 53 %, lumad 20 %, bornean 14 % |
| 260 | LUX | Luxembourg | 176.770 | 1 | 176.770 | – | wallonian 59 %, north_german 41 %, ashkenazi 0 % |
| 261 | FZN | Fezzan | 174.000 | 2 | 87.000 | 6 % | bedouin 60 %, maghrebi 17 %, berber 17 % |
| 262 | PLY | Tahiti | 169.564 | 1 | 169.564 | – | polynesian 100 %, french 0 % |
| 263 | KTI | Kutai | 165.000 | 1 | 165.000 | 5 % | dayak 58 %, bornean 42 % |
| 264 | KSN | Kasanje | 164.196 | 1 | 164.196 | 8 % | ovimbundu 73 %, lunda 27 % |
| 265 | TBI | Tubu | 163.904 | 4 | 40.976 | 7 % | teda 84 %, bedouin 12 %, equatorial_bantu 4 % |
| 266 | SDM | Sidamo | 163.000 | 1 | 163.000 | 2 % | sidama 98 %, kikuyu 2 % |
| 267 | BLE | Baule | 162.196 | 2 | 81.098 | 7 % | akan 86 %, mande 14 % |
| 268 | BNJ | Banjar | 159.592 | 1 | 159.592 | 19 % | bornean 86 %, dayak 13 %, yue 1 % |
| 269 | COB | Saxe-Coburg-Gotha | 156.537 | 1 | 156.537 | – | north_german 100 %, ashkenazi 0 % |
| 270 | BHU | Bhutan | 156.400 | 1 | 156.400 | – | tibetan 90 %, nepali 10 % |
| 271 | XHO | Xhosa | 152.200 | 1 | 152.200 | – | xhosa 100 % |
| 272 | HAM | Hamburg | 150.404 | 1 | 150.404 | – | north_german 95 %, ashkenazi 5 % |
| 273 | PTN | Patna | 148.024 | 1 | 148.024 | – | oriya 80 %, chhattisgarhi 20 % |
| 274 | PLP | Palanpur | 147.520 | 1 | 147.520 | – | gujarati 95 %, pathan 5 % |
| 275 | PRK | Perak | 147.000 | 1 | 147.000 | 1 % | malay 94 %, yue 6 % |
| 276 | CHP | Champasak | 142.216 | 1 | 142.216 | 4 % | lao 64 %, miao 25 %, shan 10 % |
| 277 | BGI | Bagirmi | 139.992 | 1 | 139.992 | 6 % | sara 54 %, equatorial_bantu 23 %, baguirmi 23 % |
| 278 | URU | Uruguay | 139.866 | 1 | 139.866 | 6 % | platinean 68 %, afro_caribeno 21 %, brazilian 11 % |
| 279 | KUN | Kunduz | 139.270 | 1 | 139.270 | 3 % | tajik 59 %, uzbek 18 %, pashtun 9 % |
| 280 | OUA | Tagant | 135.521 | 3 | 45.173 | 12 % | bidan 63 %, haratin 24 %, mande 13 % |
| 281 | MEI | Saxe-Meiningen | 135.312 | 1 | 135.312 | – | north_german 100 %, ashkenazi 0 % |
| 282 | BST | Basutoland | 135.096 | 2 | 67.548 | 6 % | sotho 100 % |
| 283 | LZO | Barotse | 130.916 | 3 | 43.638 | 5 % | kavango_bantu 66 %, lunda 25 %, chewa 9 % |
| 284 | ISQ | Isaaq | 128.000 | 1 | 128.000 | 12 % | somali 97 %, oromo 3 % |
| 285 | TRZ | Trarza | 124.000 | 1 | 124.000 | 3 % | bidan 65 %, haratin 35 % |
| 286 | NGA | Naga | 123.919 | 1 | 123.919 | – | naga 100 % |
| 287 | KRG | Karagwe | 123.600 | 1 | 123.600 | 6 % | lacustrine_bantu 100 % |
| 288 | BMM | Bamum | 122.420 | 1 | 122.420 | 8 % | equatorial_bantu 90 %, fulbe 10 % |
| 289 | NBS | New Brunswick | 120.860 | 1 | 120.860 | – | anglo_canadian 55 %, franco_canadian 44 %, algonquian 1 % |
| 290 | MON | Montenegro | 120.396 | 1 | 120.396 | – | serb 95 %, bosniak 3 %, albanian 2 % |
| 291 | PON | Pontianak | 115.200 | 1 | 115.200 | 5 % | bornean 73 %, dayak 26 %, hakka 1 % |
| 292 | JLF | Jolof | 113.600 | 1 | 113.600 | 5 % | wolof 100 % |
| 293 | FRM | Frankfurt | 112.872 | 1 | 112.872 | – | north_german 96 %, ashkenazi 4 % |
| 294 | BLG | Bulungan | 112.300 | 2 | 56.150 | 7 % | dayak 69 %, bornean 31 % |
| 295 | SNG | Sangu | 112.000 | 1 | 112.000 | 4 % | lacustrine_bantu 100 % |
| 296 | SCW | Schwarzburg | 111.832 | 1 | 111.832 | – | north_german 100 %, ashkenazi 0 % |
| 297 | KBD | Kabadougou | 109.800 | 1 | 109.800 | 12 % | mande 71 %, dyula 29 % |
| 298 | DHA | Dharampur | 109.760 | 1 | 109.760 | – | gujarati 99 %, rajput 1 % |
| 299 | LUC | Lucca | 108.408 | 1 | 108.408 | – | north_italian 100 % |
| 300 | LUO | Luo | 108.404 | 1 | 108.404 | 6 % | luo 100 % |
| 301 | AIR | Kel Air | 106.200 | 1 | 106.200 | 7 % | tuareg 64 %, hausa 26 %, fulbe 9 % |
| 302 | BRE | Bremen | 106.004 | 1 | 106.004 | – | north_german 100 % |
| 303 | OMO | Omo | 106.000 | 1 | 106.000 | – | sidama 100 % |
| 304 | LKT | Lakota | 106.000 | 6 | 17.666 | – | dakota 91 %, siouan 9 % |
| 305 | PAT | Mapuche | 100.000 | 3 | 33.333 | – | patagonian 78 %, platinean 22 % |
| 306 | AWS | Aussa | 95.554 | 2 | 47.777 | 10 % | afar 63 %, tigray 13 %, somali 13 % |
| 307 | JMB | Jambi | 92.985 | 1 | 92.985 | 6 % | sumatran 89 %, batak 10 %, yue 1 % |
| 308 | SRR | Serer | 92.400 | 1 | 92.400 | 9 % | mande 100 % |
| 309 | GGO | Gogo | 92.000 | 1 | 92.000 | 8 % | lacustrine_bantu 100 % |
| 310 | VNT | Vanuatu | 92.000 | 1 | 92.000 | – | melanesian 100 % |
| 311 | ORG | Oregon | 91.744 | 4 | 22.936 | – | salish 49 %, nez_perce 15 %, paiute 12 % |
| 312 | WSG | Warsangali | 90.676 | 1 | 90.676 | 8 % | somali 100 % |
| 313 | CAY | Cayor | 90.000 | 1 | 90.000 | 9 % | wolof 100 % |
| 314 | MJK | Mijikenda | 90.000 | 1 | 90.000 | – | lacustrine_bantu 100 % |
| 315 | VND | Venda | 89.000 | 1 | 89.000 | – | shona 75 %, sotho 25 % |
| 316 | AYI | Anyi | 88.000 | 1 | 88.000 | 10 % | akan 100 % |
| 317 | KKI | Kuki | 87.491 | 3 | 29.163 | – | lushai 100 % |
| 318 | KBU | Kaabu | 85.862 | 2 | 42.931 | 14 % | mande 100 % |
| 319 | ATB | Athabaska | 85.700 | 3 | 28.566 | – | athabaskan 81 %, inuit 19 % |
| 320 | MST | Mecklenburg-Strelitz | 85.002 | 1 | 85.002 | – | north_german 100 % |
| 321 | LUB | Lübeck | 84.396 | 1 | 84.396 | – | north_german 100 % |
| 322 | SIK | Sikkim | 84.392 | 1 | 84.392 | – | tibetan 71 %, nepali 29 % |
| 323 | FJI | Fiji | 82.000 | 1 | 82.000 | – | melanesian 100 % |
| 324 | ANU | Anuak | 80.200 | 1 | 80.200 | – | luo 100 % |
| 325 | TPS | Toposa | 80.000 | 1 | 80.000 | 5 % | nilotic 100 % |
| 326 | SMB | Sambas | 79.000 | 1 | 79.000 | 8 % | bornean 84 %, dayak 15 %, hakka 1 % |
| 327 | ABK | Abkhazia | 78.000 | 1 | 78.000 | – | abkhazian 85 %, georgian 15 % |
| 328 | LIP | Lippe | 77.546 | 1 | 77.546 | – | north_german 100 % |
| 329 | OVB | Ovambo | 77.540 | 2 | 38.770 | – | kavango_bantu 97 %, lunda 3 % |
| 330 | NAM | Nama | 76.300 | 2 | 38.150 | 5 % | khoisan 90 %, tswana 10 % |
| 331 | LAH | Lahej | 74.100 | 1 | 74.100 | 11 % | yemenite 70 %, bedouin 16 %, sudanese 11 % |
| 332 | MSI | Masai | 73.900 | 2 | 36.950 | – | maasai 100 % |
| 333 | LAN | Lanfang | 73.700 | 1 | 73.700 | – | bornean 43 %, hakka 35 %, dayak 21 % |
| 334 | TEK | Tekna | 71.141 | 3 | 23.713 | 9 % | bidan 61 %, berber 30 %, haratin 9 % |
| 335 | IRC | Iron Confederacy | 68.004 | 3 | 22.668 | – | cree 71 %, siouan 29 % |
| 336 | ADG | Kel Adagh | 66.396 | 2 | 33.198 | 5 % | tuareg 73 %, fulbe 18 %, songhai 9 % |
| 337 | SWZ | Swaziland | 64.396 | 1 | 64.396 | – | nguni 100 % |
| 338 | WBL | Griqualand | 64.000 | 1 | 64.000 | – | tswana 69 %, griqua 27 %, khoisan 5 % |
| 339 | NTU | Ngāi Tahu | 64.000 | 1 | 64.000 | – | maori 100 % |
| 340 | MGH | Khasi | 62.201 | 1 | 62.201 | – | naga 100 % |
| 341 | SEQ | Indian Territory | 62.000 | 1 | 62.000 | 2 % | cherokee 82 %, caddoan 13 %, siouan 3 % |
| 342 | MKT | Miskitia | 62.000 | 1 | 62.000 | 2 % | miskito 65 %, afro_caribbean 32 %, afro_caribeno 2 % |
| 343 | HOH | Hohenzollern | 61.334 | 1 | 61.334 | – | south_german 100 % |
| 344 | MAI | Maimana | 60.613 | 1 | 60.613 | 7 % | uzbek 51 %, turkmen 25 %, pashtun 11 % |
| 345 | TRN | Transvaal | 60.192 | 1 | 60.192 | 17 % | nguni 50 %, khoisan 33 %, boer 17 % |
| 346 | ABU | Trucial States | 60.120 | 1 | 60.120 | 5 % | bedouin 91 %, sudanese 5 %, persian 3 % |
| 347 | YOG | Yogyakarta | 58.311 | 1 | 58.311 | 9 % | javan 98 %, yue 2 % |
| 348 | TMN | Temne | 56.624 | 1 | 56.624 | – | kissi 80 %, fulbe 13 %, mande 7 % |
| 349 | BTN | Buton | 56.567 | 1 | 56.567 | 15 % | moluccan 100 % |
| 350 | TEX | Texas | 56.264 | 1 | 56.264 | 11 % | dixie 75 %, afro_american 11 %, caddoan 7 % |
| 351 | KNK | Kanak | 56.004 | 1 | 56.004 | – | melanesian 100 % |
| 352 | TKI | Tarki | 56.000 | 1 | 56.000 | – | caucasian_turk 54 %, dagestani 43 %, persian 4 % |
| 353 | MLD | Maldives | 55.992 | 1 | 55.992 | 4 % | sinhala 95 %, lacustrine_bantu 4 %, bedouin 1 % |
| 354 | WLD | Waldeck | 55.447 | 1 | 55.447 | – | north_german 100 % |
| 355 | IQU | Iquicha | 55.000 | 1 | 55.000 | – | quechua 100 % |
| 356 | DGR | Degar | 55.000 | 1 | 55.000 | – | champa 91 %, khmer 9 % |
| 357 | UNT | United Tribes | 55.000 | 1 | 55.000 | – | maori 100 % |
| 358 | THL | Tehuelche | 53.300 | 2 | 26.650 | – | patagonian 100 % |
| 359 | BKH | Bukey Orda | 52.400 | 1 | 52.400 | – | kazak 98 %, tatar 2 % |
| 360 | BLA | Bilua | 52.400 | 1 | 52.400 | – | melanesian 100 % |
| 361 | DIO | Diola | 51.554 | 1 | 51.554 | – | fulbe 94 %, mande 6 % |
| 362 | KAU | Kaurna | 51.300 | 1 | 51.300 | – | aborigine 99 %, australian 1 % |
| 363 | NAR | Narsinghpur | 49.351 | 1 | 49.351 | – | oriya 75 %, chhattisgarhi 25 % |
| 364 | JAS | Jaisalmer | 48.813 | 1 | 48.813 | – | rajput 87 %, sindi 13 % |
| 365 | MCR | Micronesia | 48.448 | 2 | 24.224 | – | micronesian 98 %, polynesian 1 %, spanish 0 % |
| 366 | ZWY | Zuwayya | 48.000 | 3 | 16.000 | – | bedouin 90 %, berber 10 % |
| 367 | HLA | Halia | 48.000 | 1 | 48.000 | – | melanesian 100 % |
| 368 | STG | Sintang | 47.500 | 1 | 47.500 | 7 % | dayak 55 %, bornean 45 % |
| 369 | WDJ | Wiradjuri | 47.121 | 2 | 23.560 | – | aborigine 100 % |
| 370 | COM | Comanche | 47.000 | 4 | 11.750 | – | siouan 53 %, comanche 38 %, apache 9 % |
| 371 | TUG | Touggourt | 46.400 | 1 | 46.400 | – | berber 65 %, maghrebi 35 %, sephardic 1 % |
| 372 | JAB | Jabal Shammar | 45.896 | 1 | 45.896 | 5 % | bedouin 95 %, sudanese 5 %, circassian 0 % |
| 373 | RGB | Reguibat | 45.616 | 4 | 11.404 | 9 % | bidan 88 %, haratin 7 %, berber 3 % |
| 374 | TIP | Tipperah | 45.102 | 1 | 45.102 | – | lushai 100 % |
| 375 | KLO | Khmer Loeu | 45.000 | 1 | 45.000 | – | khmer 73 %, lao 16 %, champa 11 % |
| 376 | NTO | Ngāti Toa | 44.428 | 2 | 22.214 | – | maori 99 %, australian 1 % |
| 377 | TKE | Teke | 44.000 | 1 | 44.000 | 11 % | bakongo 73 %, fluvian_bantu 27 % |
| 378 | KAT | Kathiri | 43.900 | 1 | 43.900 | 11 % | bedouin 89 %, sudanese 11 % |
| 379 | SRK | Surakarta | 43.431 | 1 | 43.431 | 8 % | javan 99 %, yue 1 % |
| 380 | ORA | Oranje | 43.220 | 1 | 43.220 | 23 % | nguni 46 %, sotho 35 %, boer 19 % |
| 381 | SAS | South Australia | 42.203 | 1 | 42.203 | – | aborigine 76 %, australian 15 %, irish 8 % |
| 382 | AJR | Ajuran | 42.000 | 1 | 42.000 | – | somali 100 % |
| 383 | NVJ | Navajo | 42.000 | 3 | 14.000 | – | navajo 81 %, paiute 19 % |
| 384 | TAS | Tasmania | 41.400 | 1 | 41.400 | – | australian 100 %, aborigine 0 % |
| 385 | DLM | Delim | 40.771 | 2 | 20.385 | 17 % | bidan 75 %, haratin 17 %, berber 8 % |
| 386 | NZP | Nimíipuu | 40.000 | 1 | 40.000 | – | nez_perce 100 % |
| 387 | SCT | Sip Song Chau Tai | 40.000 | 2 | 20.000 | – | lao 100 % |
| 388 | TNG | Tonga | 40.000 | 1 | 40.000 | – | polynesian 100 % |
| 389 | BNN | Pannakwati | 38.000 | 3 | 12.666 | – | paiute 100 % |
| 390 | AUL | Aulihan | 37.000 | 1 | 37.000 | – | somali 100 % |
| 391 | SAN | San | 37.000 | 4 | 9.250 | – | khoisan 100 % |
| 392 | AGC | Angoche | 36.836 | 1 | 36.836 | 11 % | swahili 80 %, makua 20 % |
| 393 | BHN | Bahrain | 36.538 | 2 | 18.269 | 7 % | bedouin 73 %, persian 20 %, sudanese 7 % |
| 394 | ADR | Adrar | 36.430 | 3 | 12.143 | 15 % | bidan 84 %, haratin 12 %, mande 3 % |
| 395 | ARH | Arnhem | 36.430 | 1 | 36.430 | – | aborigine 100 % |
| 396 | MAH | Mahra | 36.200 | 1 | 36.200 | 9 % | bedouin 91 %, sudanese 9 % |
| 397 | SKY | Sakuye | 36.000 | 1 | 36.000 | – | oromo 78 %, lacustrine_bantu 22 % |
| 398 | ABS | Absaroka | 34.500 | 2 | 17.250 | – | siouan 100 % |
| 399 | BLF | Niitsitapi | 34.400 | 2 | 17.200 | – | siouan 85 %, metis 15 % |
| 400 | EZO | Ezochi | 31.871 | 2 | 15.935 | – | ainu 94 %, japanese 6 % |
| 401 | PHL | Philippolis | 31.280 | 1 | 31.280 | – | griqua 39 %, sotho 38 %, tswana 19 % |
| 402 | MBS | Mombasa | 30.001 | 1 | 30.001 | 8 % | swahili 75 %, bedouin 17 %, lacustrine_bantu 8 % |
| 403 | GNI | Guarani | 29.430 | 3 | 9.810 | – | guarani 95 %, platinean 3 %, quechua 1 % |
| 404 | AHG | Kel Ahaggar | 29.004 | 1 | 29.004 | 8 % | tuareg 86 %, berber 14 % |
| 405 | AJJ | Kel Ajjer | 28.000 | 3 | 9.333 | 4 % | tuareg 100 % |
| 406 | WTI | Anangu | 27.804 | 3 | 9.268 | – | aborigine 100 % |
| 407 | KLN | Kulin | 26.956 | 3 | 8.985 | – | aborigine 100 % |
| 408 | KAF | Kafiristan | 26.748 | 1 | 26.748 | 7 % | kho 84 %, pashtun 16 % |
| 409 | PMA | Pama | 25.710 | 1 | 25.710 | – | aborigine 100 % |
| 410 | TGI | Tungi | 24.996 | 1 | 24.996 | 12 % | swahili 80 %, makua 20 % |
| 411 | CMB | Chaamba | 24.300 | 2 | 12.150 | – | bedouin 79 %, berber 21 % |
| 412 | APC | Apache | 24.000 | 2 | 12.000 | – | apache 92 %, pueblo 8 % |
| 413 | SVN | Svaneti | 24.000 | 1 | 24.000 | – | georgian 100 % |
| 414 | SCM | Schaumburg-Lippe | 23.820 | 1 | 23.820 | – | north_german 100 % |
| 415 | WRR | Worrorra | 23.100 | 2 | 11.550 | – | aborigine 100 % |
| 416 | WAS | Western Australia | 22.502 | 1 | 22.502 | – | australian 52 %, irish 28 %, aborigine 18 % |
| 417 | NNG | Noongar | 21.100 | 1 | 21.100 | – | aborigine 100 % |
| 418 | DIN | Kel Dinnik | 21.000 | 1 | 21.000 | 5 % | tuareg 48 %, hausa 29 %, fulbe 24 % |
| 419 | ORM | Orma | 21.000 | 1 | 21.000 | – | oromo 100 % |
| 420 | MRA | Mara | 20.315 | 1 | 20.315 | – | aborigine 100 % |
| 421 | PWN | Pawnee | 20.000 | 2 | 10.000 | – | caddoan 90 %, siouan 10 % |
| 422 | UTE | Ute | 19.000 | 2 | 9.500 | – | paiute 79 %, apache 21 % |
| 423 | WTU | Witu | 18.500 | 1 | 18.500 | – | swahili 50 %, somali 38 %, oromo 12 % |
| 424 | GRW | Garawa | 16.750 | 2 | 8.375 | – | aborigine 100 % |
| 425 | LRR | Larrakia | 15.600 | 1 | 15.600 | – | aborigine 100 % |
| 426 | ATR | Kel Ataram | 15.000 | 1 | 15.000 | 7 % | tuareg 67 %, songhai 20 %, fulbe 13 % |
| 427 | ARR | Arrernte | 14.840 | 2 | 7.420 | – | aborigine 100 % |
| 428 | ALK | Alaska | 14.821 | 2 | 7.410 | – | athabaskan 75 %, inuit 14 %, russian 8 % |
| 429 | SLS | Séliš | 14.200 | 2 | 7.100 | – | salish 100 % |
| 430 | ARP | Arapaho | 14.000 | 2 | 7.000 | – | siouan 100 % |
| 431 | KYN | Pilbara | 13.500 | 1 | 13.500 | – | aborigine 100 % |
| 432 | WKB | Waka-Gabi | 13.400 | 1 | 13.400 | – | aborigine 100 % |
| 433 | BRK | Brakna | 12.510 | 1 | 12.510 | – | haratin 100 % |
| 434 | MRN | Mirning | 12.500 | 2 | 6.250 | – | aborigine 100 % |
| 435 | TUA | Tuat | 12.000 | 1 | 12.000 | – | berber 100 % |
| 436 | SLK | Selk’nam | 12.000 | 1 | 12.000 | – | patagonian 100 % |
| 437 | KRI | Douriango | 11.431 | 2 | 5.715 | – | aborigine 100 % |
| 438 | MZB | Mzab | 10.991 | 1 | 10.991 | – | berber 100 % |
| 439 | YUR | Yura | 10.766 | 2 | 5.383 | – | aborigine 100 % |
| 440 | KNC | Karna | 10.643 | 4 | 2.660 | – | aborigine 100 % |
| 441 | KTU | Kartu | 10.500 | 1 | 10.500 | – | aborigine 100 % |
| 442 | NYP | Ngumpin-Yapa | 10.500 | 2 | 5.250 | – | aborigine 100 % |
| 443 | YGU | Yolngu | 10.200 | 1 | 10.200 | – | aborigine 100 % |
| 444 | PAA | Paakintyi | 10.080 | 3 | 3.360 | – | aborigine 100 % |
| 445 | SML | Yat’siminoli | 10.000 | 1 | 10.000 | – | muskogean 100 % |
| 446 | AIN | Ainu Mosir | 7.281 | 1 | 7.281 | – | ainu 90 %, evenki 10 % |
| 447 | SKH | Evenki | 5.193 | 1 | 5.193 | – | evenki 100 % |
| 448 | ULT | Ulta | 4.242 | 1 | 4.242 | – | evenki 87 %, ainu 13 % |
| 449 | NRU | Nauru | 1.251 | 1 | 1.251 | – | melanesian 100 % |

## Victorian Azeroth – alle Länder

- Bevölkerung gesamt: **416.810.760**
- Länder mit Pops: 324; States mit Pops (State Regions): 702
- Ø je Land: 1.286.452; Median je Land: 544.000; Ø je State Region: 593.747
- Sklaven: 1.974.350 (0.5 %)
- Kulturen: 82; größte: stormwindian 33.091.800, kal_dorei 28.961.060, orgrimmari 22.842.550, sin_dorei 19.977.380, nazjatar 19.031.000, lordorean 18.185.000, gorian_ogre 15.516.000, forsaken 14.689.960
- Länder nach Größe: unter 100.000: 11, 100.000–500.000: 113, 0,5–1 Mio.: 85, 1–5 Mio.: 99, 5–20 Mio.: 16

| # | Tag | Name | Pops | States | Ø je State | Sklaven | Hauptkulturen (Anteil) |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | STORMWIND |  | 15.161.000 | 19 | 797.947 | – | stormwindian 100 % |
| 2 | ORGRIMMAR |  | 15.150.000 | 23 | 658.695 | – | orgrimmari 100 % |
| 3 | NRTHRND |  | 14.245.000 | 132 | 107.916 | – | blue_dragon 14 %, stormwindian 10 %, sin_dorei 9 % |
| 4 | UNDERCITY |  | 13.518.000 | 18 | 751.000 | – | forsaken 96 %, alpha_pack 4 % |
| 5 | DARNASSUS |  | 12.320.000 | 19 | 648.421 | – | kal_dorei 100 % |
| 6 | VASHJ_IR |  | 11.000.000 | 11 | 1.000.000 | – | nazjatar 100 % |
| 7 | IRONFORGE |  | 10.780.000 | 10 | 1.078.000 | – | bronzebeard 100 % |
| 8 | GILNEAS |  | 8.008.000 | 7 | 1.144.000 | – | gilnean 70 %, alpha_pack 23 %, tal_dorens 7 % |
| 9 | TWILIGHTS_HAMMER |  | 7.848.000 | 7 | 1.121.142 | – | gorian_ogre 100 % |
| 10 | STEAMWHEEDLE_CARTEL |  | 6.775.000 | 11 | 615.909 | – | goblin 100 % |
| 11 | EXODAR |  | 6.490.000 | 11 | 590.000 | – | draenei 100 % |
| 12 | THUNDERBLUFF |  | 5.820.000 | 10 | 582.000 | – | tauren 100 % |
| 13 | SCARLET_CRUSADERS_WHITEMANE |  | 5.410.000 | 6 | 901.666 | – | lordorean 100 % |
| 14 | SILVERMOON |  | 5.362.200 | 11 | 487.472 | – | sin_dorei 90 %, quel_dorei 8 %, dalaranian 1 % |
| 15 | BLACKROCK_CLAN |  | 5.190.000 | 10 | 519.000 | – | mok_grondal 100 % |
| 16 | SCARLET_CRUSADERS_ONSLAUGHT |  | 5.180.000 | 3 | 1.726.666 | – | lordorean 100 % |
| 17 | ARGENT_CRUSADERS |  | 4.977.000 | 9 | 553.000 | – | lordorean 88 %, zombie 12 % |
| 18 | BURNING_BLADE |  | 4.830.000 | 6 | 805.000 | – | maghar_orc 100 % |
| 19 | GNOMEREGAN |  | 4.610.000 | 3 | 1.536.666 | – | gnome 100 % |
| 20 | THERAMORE |  | 4.160.000 | 8 | 520.000 | – | kul_tiran 100 % |
| 21 | DEATHHOLME |  | 3.959.000 | 5 | 791.800 | – | banshee 71 %, zombie 29 % |
| 22 | VILEBRANCH_TROLLS |  | 3.820.000 | 3 | 1.273.333 | – | forest_troll 100 % |
| 23 | GURUBASHI_TRIBE |  | 3.600.000 | 1 | 3.600.000 | – | jungle_troll 100 % |
| 24 | WILDHAMMER_CLAN_AZ |  | 3.300.000 | 5 | 660.000 | – | wildhammer 100 % |
| 25 | ILLIDARY |  | 3.295.200 | 2 | 1.647.600 | – | felorc 35 %, sin_dorei 34 %, krokul 16 % |
| 26 | SUNFURY |  | 3.188.800 | 5 | 637.760 | – | sin_dorei 83 %, mountain_giant 5 %, imp 5 % |
| 27 | GRIMMTOTEM |  | 3.160.000 | 5 | 632.000 | – | tauren 100 % |
| 28 | GUARDIANS_HYJAL |  | 3.160.000 | 6 | 526.666 | – | kal_dorei 100 % |
| 29 | PLAGUELAND_UNDEAD |  | 3.130.000 | 4 | 782.500 | – | zombie 92 %, banshee 8 % |
| 30 | CULT_OF_DAMNED |  | 3.030.000 | 5 | 606.000 | – | lordorean 68 %, zombie 32 % |
| 31 | SPITELASH_NAGA |  | 3.000.000 | 4 | 750.000 | – | nazjatar 100 % |
| 32 | SHATTERED_HAND_CLAN |  | 2.964.000 | 4 | 741.000 | – | felorc 87 %, orgrimmari 3 %, stormwindian 3 % |
| 33 | TWILIGHT_HAMMER_HYJAL |  | 2.830.000 | 4 | 707.500 | – | gorian_ogre 100 % |
| 34 | BURNING_LEGION_KILJADEN |  | 2.714.400 | 6 | 452.400 | – | imp 30 %, doom_guard 27 %, nathrezim 14 % |
| 35 | AMANI_TRIBE | Zul'Jarra | 2.581.620 | 2 | 1.290.810 | 37 % | forest_troll 49 %, sin_dorei 30 %, dire_troll 15 % |
| 36 | KNIGHTS_EBON_BLADE |  | 2.550.000 | 1 | 2.550.000 | 33 % | death_knight 67 %, lordorean 33 % |
| 37 | DARKSPEAR |  | 2.500.000 | 3 | 833.333 | – | jungle_troll 100 % |
| 38 | SOUTHSEE_FREEBOOTERS |  | 2.500.000 | 4 | 625.000 | – | kul_tiran 100 % |
| 39 | DEFIAS_BROTHERHOOD |  | 2.370.000 | 4 | 592.500 | – | stormwindian 100 % |
| 40 | BRISTLEBACK_QUILBOARS |  | 2.330.000 | 4 | 582.500 | – | quilboar 100 % |
| 41 | TWILIGHT_HAMMER_SILITHUS |  | 2.330.000 | 4 | 582.500 | – | gorian_ogre 100 % |
| 42 | SHA_TAR |  | 2.308.400 | 1 | 2.308.400 | – | stormwindian 19 %, draenei 18 %, sin_dorei 18 % |
| 43 | SYNDICATE |  | 2.260.000 | 5 | 452.000 | – | alteraci 100 % |
| 44 | THE_INFERNO |  | 2.160.000 | 4 | 540.000 | – | elemental_fire 100 % |
| 45 | DRAGONMAW_CLAN_AZ |  | 2.110.000 | 5 | 422.000 | – | nelghor_shomash 100 % |
| 46 | THRALLMAR |  | 2.036.000 | 5 | 407.200 | – | fungul_giant 28 %, orgrimmari 23 %, jungle_troll 22 % |
| 47 | CLIFFWALKER |  | 2.000.000 | 3 | 666.666 | – | tauren 100 % |
| 48 | NORTHWATCH_EXPEDITION |  | 2.000.000 | 3 | 666.666 | – | stormwindian 100 % |
| 49 | CENARION_CIRCLE |  | 2.000.000 | 2 | 1.000.000 | – | kal_dorei 100 % |
| 50 | BLACK_DRAGONFLIGHT_ONYXIA |  | 2.000.000 | 2 | 1.000.000 | – | black_dragon 100 % |
| 51 | WINTERFALL_WILD |  | 2.000.000 | 2 | 1.000.000 | – | kal_dorei 100 % |
| 52 | UNGORO_WILD |  | 2.000.000 | 3 | 666.666 | – | stormwindian 100 % |
| 53 | AHNQIRAJ |  | 2.000.000 | 2 | 1.000.000 | – | qiraji 100 % |
| 54 | COILFANG_TRIBE |  | 1.928.000 | 1 | 1.928.000 | – | lestharian 52 %, krokul 31 %, fungul_giant 5 % |
| 55 | INFECTED_WILDLIFE |  | 1.830.000 | 3 | 610.000 | – | moonkin 100 % |
| 56 | BURNING_LEGION_INVASION_NETHERSTORM |  | 1.689.600 | 5 | 337.920 | – | imp 38 %, mountain_giant 35 %, doom_guard 16 % |
| 57 | DARNASSUS_OUTPOST |  | 1.660.000 | 4 | 415.000 | – | kal_dorei 100 % |
| 58 | DRAGONMAW_CLAN |  | 1.643.200 | 1 | 1.643.200 | – | felorc 59 %, nether_dragon 22 %, krokul 15 % |
| 59 | WRETCHED_BLOODELFES |  | 1.640.000 | 3 | 546.666 | – | sin_dorei 98 %, quel_dorei 2 % |
| 60 | TWILIGHT_HAMMER_DARKSHORE |  | 1.500.000 | 3 | 500.000 | – | gorian_ogre 100 % |
| 61 | EMERALD_CIRCLE |  | 1.500.000 | 3 | 500.000 | – | kal_dorei 100 % |
| 62 | MARSHAL_EXPEDITION |  | 1.500.000 | 3 | 500.000 | – | stormwindian 100 % |
| 63 | ZANZIL_WITCHDOCTORS |  | 1.450.000 | 2 | 725.000 | – | jungle_troll 100 % |
| 64 | MENETHIL |  | 1.440.000 | 2 | 720.000 | – | stormwindian 100 % |
| 65 | DARK_IRON_CLAN |  | 1.430.000 | 4 | 357.500 | – | darkiron 100 % |
| 66 | ECLIPSE_POINT |  | 1.428.800 | 2 | 714.400 | – | sin_dorei 72 %, mountain_giant 26 %, felorc 1 % |
| 67 | RIVERPAW_PACK |  | 1.410.000 | 4 | 352.500 | – | mudmane 100 % |
| 68 | VENTURE_CO |  | 1.400.000 | 4 | 350.000 | – | goblin 100 % |
| 69 | BURNING_LEGION_FORGE_CAMPS |  | 1.344.400 | 5 | 268.880 | – | imp 50 %, doom_guard 23 %, felorc 8 % |
| 70 | FROSTMANES |  | 1.340.000 | 3 | 446.666 | – | frostmane_troll 100 % |
| 71 | RAZORFEN |  | 1.330.000 | 2 | 665.000 | – | quilboar 100 % |
| 72 | WRATHSCALE_NAGA |  | 1.330.000 | 2 | 665.000 | – | nazjatar 100 % |
| 73 | SENTINELS |  | 1.330.000 | 3 | 443.333 | – | kal_dorei 100 % |
| 74 | GORDUNNI_OGRE |  | 1.330.000 | 3 | 443.333 | – | gordunni_ogre 100 % |
| 75 | SANDFURY_TRIBE |  | 1.330.000 | 2 | 665.000 | – | sand_troll 100 % |
| 76 | PANDARIA |  | 1.240.000 | 124 | 10.000 | – | sin_dorei 100 % |
| 77 | THE_SCRYERS |  | 1.224.000 | 2 | 612.000 | – | sin_dorei 87 %, maghar_orc 9 %, draenei 2 % |
| 78 | HAMMERFALL |  | 1.210.000 | 2 | 605.000 | – | orgrimmari 100 % |
| 79 | SKETTIS |  | 1.205.600 | 2 | 602.800 | – | arakkoa 98 %, krokul 1 %, mountain_giant 1 % |
| 80 | MAGHAR |  | 1.191.200 | 5 | 238.240 | – | maghar_orc 86 %, orgrimmari 3 %, forsaken 2 % |
| 81 | CABAL |  | 1.186.400 | 3 | 395.466 | – | maghar_orc 60 %, krokul 11 %, gnome 6 % |
| 82 | HONOR_HOLD |  | 1.164.800 | 3 | 388.266 | – | stormwindian 44 %, draenei 17 %, bronzebeard 17 % |
| 83 | THE_ALDOR |  | 1.155.200 | 2 | 577.600 | – | draenei 100 % |
| 84 | BLOODSCALP_TRIBE |  | 1.150.000 | 2 | 575.000 | – | jungle_troll 100 % |
| 85 | GREENWARDENS_GROVE |  | 1.140.000 | 2 | 570.000 | – | kal_dorei 100 % |
| 86 | OBSIDIAN_DRAGONFLIGHT |  | 1.140.000 | 2 | 570.000 | – | black_dragon 100 % |
| 87 | BLOODSCALE_TRIBE |  | 1.129.600 | 2 | 564.800 | – | lestharian 55 %, krokul 27 %, mountain_ogre 11 % |
| 88 | ETHEREUM |  | 1.071.200 | 2 | 535.600 | – | ethereal 100 % |
| 89 | SHADOWPINE_TRIBE |  | 1.060.000 | 3 | 353.333 | 16 % | forest_troll 79 %, sin_dorei 16 %, dire_troll 4 % |
| 90 | MARSHTIDE_WATCH |  | 1.060.000 | 3 | 353.333 | – | stormwindian 100 % |
| 91 | BLADESPIRE_CLAN |  | 1.044.800 | 3 | 348.266 | – | mountain_ogre 95 %, magnaron 4 %, draenei 1 % |
| 92 | BLACKWIND_WYRMCULTISTS |  | 1.032.000 | 3 | 344.000 | – | black_dragon 31 %, draenei 21 %, orgrimmari 21 % |
| 93 | THORIUM_BROTHERHOOD |  | 1.008.000 | 4 | 252.000 | – | darkiron 100 % |
| 94 | THAL_DARAH |  | 1.000.000 | 2 | 500.000 | – | kal_dorei 100 % |
| 95 | SLUDGEWERKS |  | 1.000.000 | 1 | 1.000.000 | – | goblin 100 % |
| 96 | SLITHERBLADE_NAGA |  | 1.000.000 | 1 | 1.000.000 | – | nazjatar 100 % |
| 97 | MAROUDINE |  | 1.000.000 | 1 | 1.000.000 | – | centaur 100 % |
| 98 | BEAL_DUN |  | 1.000.000 | 1 | 1.000.000 | – | bronzebeard 100 % |
| 99 | SHADOWFANG_KEEP |  | 1.000.000 | 1 | 1.000.000 | – | alpha_pack 100 % |
| 100 | GNARLPINE_FURBOLG |  | 1.000.000 | 2 | 500.000 | – | furbolg 100 % |
| 101 | VERIDIAN_DRAGONFLIGHT |  | 1.000.000 | 1 | 1.000.000 | – | black_dragon 100 % |
| 102 | SUNHAWK |  | 1.000.000 | 2 | 500.000 | – | sin_dorei 100 % |
| 103 | SHATTERSPEAR |  | 1.000.000 | 2 | 500.000 | – | jungle_troll 100 % |
| 104 | DARKSCALE_NAGA |  | 1.000.000 | 2 | 500.000 | – | lestharian 100 % |
| 105 | WINTERFALL_FURBOLG |  | 1.000.000 | 2 | 500.000 | – | furbolg 100 % |
| 106 | BLOODVENOM_CORRUPTION |  | 1.000.000 | 1 | 1.000.000 | – | forsaken 100 % |
| 107 | JADEFIRE_CORRUPTION |  | 1.000.000 | 1 | 1.000.000 | – | fel_dorei 100 % |
| 108 | MANNOROTH_LEGION |  | 1.000.000 | 1 | 1.000.000 | – | doom_guard 100 % |
| 109 | MAGMATHAR_FIRE |  | 1.000.000 | 1 | 1.000.000 | – | elemental_fire 100 % |
| 110 | NORTHSPRING_HARPY |  | 1.000.000 | 1 | 1.000.000 | – | harpy 100 % |
| 111 | WOODPAW_GNOLL |  | 1.000.000 | 1 | 1.000.000 | – | mudmane 100 % |
| 112 | TWILIGHT_HAMMER_THOUSAND_NEEDLES |  | 1.000.000 | 1 | 1.000.000 | – | gorian_ogre 100 % |
| 113 | KEEPERS_OF_TIME |  | 1.000.000 | 1 | 1.000.000 | – | bronze_dragon 100 % |
| 114 | ULDUM_RUINS |  | 1.000.000 | 1 | 1.000.000 | – | sand_troll 100 % |
| 115 | HIVE_REGAL |  | 1.000.000 | 1 | 1.000.000 | – | aqir 100 % |
| 116 | AUCHENAI |  | 984.800 | 3 | 328.266 | – | draenei 71 %, stormwindian 29 % |
| 117 | ANGOROSH_TRIBE |  | 948.800 | 1 | 948.800 | – | jungle_ogre 77 %, krokul 22 %, warmwater_murloc 1 % |
| 118 | BLOODMAUL_CLAN |  | 945.600 | 3 | 315.200 | – | mountain_ogre 94 %, black_dragon 4 %, magnaron 3 % |
| 119 | SPOREGGAR |  | 934.400 | 3 | 311.466 | – | fungul_giant 62 %, sporeling 38 % |
| 120 | STONARD |  | 920.000 | 2 | 460.000 | – | orgrimmari 100 % |
| 121 | REVANTUSK_TROLLS |  | 900.000 | 2 | 450.000 | – | forest_troll 100 % |
| 122 | NETHERGARDE_KEEP |  | 900.000 | 2 | 450.000 | – | stormwindian 100 % |
| 123 | VERMILLON_DRAGONFLIGHT |  | 880.000 | 2 | 440.000 | – | green_dragon 100 % |
| 124 | SKULLSPLITTER_TRIBE |  | 870.000 | 1 | 870.000 | – | jungle_troll 100 % |
| 125 | BOULDERFIST_CLAN_AZ |  | 840.000 | 2 | 420.000 | – | hill_ogre 100 % |
| 126 | BLACKWING_OUTPOST |  | 832.000 | 3 | 277.333 | – | black_dragon 100 % |
| 127 | BLACKWING_DRAGONFLIGHT |  | 830.000 | 2 | 415.000 | – | black_dragon 100 % |
| 128 | PALEMANE_GNOLL |  | 830.000 | 2 | 415.000 | – | bluepelt 100 % |
| 129 | BLACKSILT_MURLOC |  | 830.000 | 2 | 415.000 | – | warmwater_murloc 100 % |
| 130 | BRISTLELIMB_FURBOLG |  | 830.000 | 2 | 415.000 | – | furbolg 100 % |
| 131 | GREYMIST_MURLOC |  | 830.000 | 2 | 415.000 | – | warmwater_murloc 100 % |
| 132 | BLACKWOOD_FURBOLG |  | 830.000 | 2 | 415.000 | – | furbolg 100 % |
| 133 | IRONTREE |  | 830.000 | 2 | 415.000 | – | goblin 100 % |
| 134 | DEADWOOD_FURBOLG |  | 830.000 | 2 | 415.000 | – | furbolg 100 % |
| 135 | XYLEM_OUTPOST |  | 830.000 | 2 | 415.000 | – | stormwindian 100 % |
| 136 | WRATHTAIL_NAGA |  | 830.000 | 2 | 415.000 | – | nazjatar 100 % |
| 137 | SHEN_DRALAR |  | 830.000 | 2 | 415.000 | – | shen_dralar 100 % |
| 138 | HIVE_ASHI |  | 830.000 | 2 | 415.000 | – | aqir 100 % |
| 139 | SHADOWFORGE |  | 810.000 | 2 | 405.000 | – | darkiron 100 % |
| 140 | DUSTBELCHER_CLAN |  | 780.000 | 2 | 390.000 | – | mountain_ogre 100 % |
| 141 | AREA_FIFTYTWO |  | 772.000 | 2 | 386.000 | – | goblin 59 %, mountain_giant 26 %, sin_dorei 7 % |
| 142 | GRIMSCALE_MURLOCS |  | 764.000 | 3 | 254.666 | – | warmwater_murloc 100 % |
| 143 | WORMTHORN_CORRUPTION |  | 760.000 | 1 | 760.000 | – | nathrezim 100 % |
| 144 | WARMAUL_CLAN |  | 733.600 | 2 | 366.800 | – | hill_ogre 76 %, krokul 5 %, maghar_orc 4 % |
| 145 | BURNING_LEGION_TWILIGHT_HOLD |  | 712.000 | 1 | 712.000 | – | felorc 37 %, imp 29 %, mountain_ogre 17 % |
| 146 | DREADMAUL_OGRES |  | 700.000 | 2 | 350.000 | – | mountain_ogre 100 % |
| 147 | DARKCREST_TRIBE |  | 676.800 | 2 | 338.400 | – | lestharian 69 %, krokul 31 % |
| 148 | DUN_GAROK |  | 670.000 | 1 | 670.000 | – | bronzebeard 100 % |
| 149 | XAVIAN_CORRUPTION |  | 660.000 | 2 | 330.000 | – | fel_dorei 100 % |
| 150 | SILVERWING_OUTPOST |  | 660.000 | 2 | 330.000 | – | orgrimmari 100 % |
| 151 | MOSSFLAYER_TROLLS |  | 650.000 | 1 | 650.000 | – | forest_troll 100 % |
| 152 | CRUSHRIDGE_OGRE |  | 620.000 | 2 | 310.000 | – | mountain_ogre 100 % |
| 153 | SHAFFAR |  | 606.200 | 2 | 303.100 | – | ethereal 97 %, mountain_giant 2 %, doom_guard 1 % |
| 154 | AZEROTH_DEFENDERS |  | 594.800 | 2 | 297.400 | – | stormwindian 34 %, bronzebeard 15 %, sin_dorei 15 % |
| 155 | BLEEDING_HOLLOW_CLAN |  | 586.400 | 1 | 586.400 | – | felorc 98 %, orgrimmari 2 % |
| 156 | KIRINTOR_EXPEDITION |  | 580.000 | 2 | 290.000 | – | dalaranian 100 % |
| 157 | MOSHOGG_OGRE |  | 580.000 | 2 | 290.000 | – | mountain_ogre 100 % |
| 158 | BURNING_LEGION_LEGIONS_HOLD |  | 576.800 | 2 | 288.400 | – | doom_guard 36 %, imp 23 %, eredar 19 % |
| 159 | BLUEGILL_MORLOCS |  | 550.000 | 2 | 275.000 | – | warmwater_murloc 100 % |
| 160 | NEW_KARGATH |  | 550.000 | 1 | 550.000 | – | orgrimmari 100 % |
| 161 | COILSCAR_POINT |  | 545.600 | 2 | 272.800 | – | lestharian 98 %, gnome 2 % |
| 162 | STONEBREAKER_HOLD |  | 544.000 | 2 | 272.000 | – | orgrimmari 62 %, jungle_troll 13 %, arakkoa 13 % |
| 163 | TOSHLEY_STATION |  | 519.200 | 1 | 519.200 | – | nether_dragon 51 %, gnome 49 % |
| 164 | EXPLORERS_LEAGUE |  | 517.000 | 2 | 258.500 | – | bronzebeard 100 % |
| 165 | DARK_CONCLAVE |  | 512.800 | 2 | 256.400 | – | arakkoa 100 % |
| 166 | BOULDERFIST_CLAN |  | 510.400 | 4 | 127.600 | – | hill_ogre 87 %, maghar_orc 8 %, goblin 3 % |
| 167 | NIGHTBANE_WORGEN |  | 510.000 | 2 | 255.000 | – | alpha_pack 100 % |
| 168 | BOULDERSLIDE_KOBOLD |  | 500.000 | 1 | 500.000 | – | kobold 100 % |
| 169 | WITCHWING_HARPIE |  | 500.000 | 1 | 500.000 | – | harpy 100 % |
| 170 | RAZORMANE |  | 500.000 | 1 | 500.000 | – | quilboar 100 % |
| 171 | DRUIDS_OF_FANG |  | 500.000 | 1 | 500.000 | – | kal_dorei 100 % |
| 172 | HATEFURY_SATYRS |  | 500.000 | 1 | 500.000 | – | fel_dorei 100 % |
| 173 | MAGRAM |  | 500.000 | 1 | 500.000 | – | centaur 100 % |
| 174 | GELKIS |  | 500.000 | 1 | 500.000 | – | centaur 100 % |
| 175 | SHADOWPREY |  | 500.000 | 1 | 500.000 | – | jungle_troll 100 % |
| 176 | HONOR_STAND |  | 500.000 | 1 | 500.000 | – | stormwindian 100 % |
| 177 | BLACKHOOF |  | 500.000 | 1 | 500.000 | – | tauren 100 % |
| 178 | BRACKENWALL |  | 500.000 | 1 | 500.000 | – | jungle_ogre 100 % |
| 179 | DIREHORN |  | 500.000 | 1 | 500.000 | – | tauren 100 % |
| 180 | BLOODFEATHER_HARPY |  | 500.000 | 1 | 500.000 | – | harpy 100 % |
| 181 | SILTFIN_MURLOC |  | 500.000 | 1 | 500.000 | – | warmwater_murloc 100 % |
| 182 | EVERLOOK |  | 500.000 | 1 | 500.000 | – | goblin 100 % |
| 183 | TIMBERMAW_FURBOLG |  | 500.000 | 1 | 500.000 | – | furbolg 100 % |
| 184 | JAEDENAR |  | 500.000 | 1 | 500.000 | – | nathrezim 100 % |
| 185 | WORMWING_HARPIES |  | 500.000 | 1 | 500.000 | – | harpy 100 % |
| 186 | BLACK_DRAGONFLIGHT_SABLE |  | 500.000 | 1 | 500.000 | – | black_dragon 100 % |
| 187 | BLACKMAW_FURBOLGS |  | 500.000 | 1 | 500.000 | – | furbolg 100 % |
| 188 | DARK_STRAND_CULT |  | 500.000 | 1 | 500.000 | – | orgrimmari 100 % |
| 189 | BATHRANS_HAUNT |  | 500.000 | 1 | 500.000 | – | banshee 100 % |
| 190 | BLOODWASH_NAGA |  | 500.000 | 2 | 250.000 | – | nazjatar 100 % |
| 191 | DRUIDS_OF_TALONS |  | 500.000 | 1 | 500.000 | – | kal_dorei 100 % |
| 192 | GREEN_DRAGONFLIGHT_FERALAS_GUARDIANS |  | 500.000 | 1 | 500.000 | – | green_dragon 100 % |
| 193 | HATECREST_NAGA |  | 500.000 | 1 | 500.000 | – | nazjatar 100 % |
| 194 | STEAM_RESORT |  | 500.000 | 1 | 500.000 | – | goblin 100 % |
| 195 | HIVE_ZUKKASH |  | 500.000 | 1 | 500.000 | – | aqir 100 % |
| 196 | CAMP_MOJACHE |  | 500.000 | 1 | 500.000 | – | tauren 100 % |
| 197 | GALAK_CENTAUR |  | 500.000 | 1 | 500.000 | – | centaur 100 % |
| 198 | HAZZALI_LAIR |  | 500.000 | 1 | 500.000 | – | aqir 100 % |
| 199 | GORISHI_LAIR |  | 500.000 | 1 | 500.000 | – | aqir 100 % |
| 200 | HIVE_ZORA |  | 500.000 | 1 | 500.000 | – | aqir 100 % |
| 201 | SHADOW_COUNCIL |  | 495.200 | 1 | 495.200 | – | orgrimmari 48 %, imp 28 %, krokul 8 % |
| 202 | BASHIR |  | 493.600 | 1 | 493.600 | – | ethereal 81 %, black_dragon 7 %, sin_dorei 5 % |
| 203 | SHADOWMOON_VILLAGE |  | 492.000 | 1 | 492.000 | – | orgrimmari 39 %, maghar_orc 29 %, felorc 18 % |
| 204 | WILDHAMMER_CLAN |  | 472.000 | 1 | 472.000 | – | wildhammer 84 %, gnome 5 %, draenei 3 % |
| 205 | STONESPLINTER_TRIBE |  | 460.000 | 2 | 230.000 | – | trogg 100 % |
| 206 | BAMBALA |  | 460.000 | 1 | 460.000 | – | jungle_troll 100 % |
| 207 | KURENAI |  | 447.200 | 1 | 447.200 | – | krokul 67 %, draenei 29 %, sin_dorei 3 % |
| 208 | ILLIDARY_POINT |  | 443.200 | 1 | 443.200 | – | fel_dorei 45 %, doom_guard 28 %, nathrezim 11 % |
| 209 | ALLERIAN_STRONGHOLD |  | 404.800 | 1 | 404.800 | – | stormwindian 55 %, quel_dorei 16 %, kal_dorei 11 % |
| 210 | SI7_HIGHLANDS |  | 382.000 | 2 | 191.000 | – | stormwindian 100 % |
| 211 | MUDSNOUT_GNOLLS |  | 380.000 | 1 | 380.000 | – | bluepelt 100 % |
| 212 | SPLINTERFIST_CLAN |  | 380.000 | 1 | 380.000 | – | hill_ogre 100 % |
| 213 | BLOODSAIL_PIRATES |  | 380.000 | 1 | 380.000 | – | kul_tiran 100 % |
| 214 | SHIENOR |  | 376.000 | 2 | 188.000 | – | arakkoa 83 %, kal_dorei 3 %, tauren 3 % |
| 215 | GRIKNIR_FROSTMANE |  | 370.000 | 1 | 370.000 | – | frostmane_troll 100 % |
| 216 | IRON_SUMMIT |  | 370.000 | 1 | 370.000 | – | darkiron 100 % |
| 217 | BLOODFANG_PACK |  | 370.000 | 1 | 370.000 | – | alpha_pack 100 % |
| 218 | HIGHVALE_HIGHELFES |  | 370.000 | 1 | 370.000 | – | quel_dorei 100 % |
| 219 | OMENAI_TEMPLE |  | 366.400 | 1 | 366.400 | – | draenei 63 %, mountain_giant 23 %, krokul 14 % |
| 220 | THE_RELIQUARY |  | 360.000 | 1 | 360.000 | – | sin_dorei 100 % |
| 221 | SUNVEIL_EXCURSION |  | 360.000 | 2 | 180.000 | – | sin_dorei 100 % |
| 222 | STRANGLETHRON_NAGA |  | 360.000 | 1 | 360.000 | – | nazjatar 100 % |
| 223 | TRANQUILLIEN |  | 355.380 | 2 | 177.690 | – | sin_dorei 83 %, forsaken 17 % |
| 224 | KARAZHAN |  | 345.000 | 1 | 345.000 | – | stormwindian 100 % |
| 225 | BLOODEYE_CLAN |  | 340.000 | 1 | 340.000 | – | mountain_ogre 100 % |
| 226 | REDGRIDGE_PACK |  | 340.000 | 1 | 340.000 | – | emberhide 100 % |
| 227 | GILNEAS_EXPEDITION |  | 340.000 | 1 | 340.000 | – | gilnean 100 % |
| 228 | DUSTWIND_HARPY |  | 330.000 | 1 | 330.000 | – | harpy 100 % |
| 229 | WINDFURY_HARPY |  | 330.000 | 1 | 330.000 | – | harpy 100 % |
| 230 | FRAZZLECRAZ |  | 330.000 | 1 | 330.000 | – | goblin 100 % |
| 231 | MIREFIN_MURLOC |  | 330.000 | 1 | 330.000 | – | warmwater_murloc 100 % |
| 232 | STRASHAZ |  | 330.000 | 1 | 330.000 | – | nazjatar 100 % |
| 233 | HIGHLAND_FROSTWOLFES |  | 330.000 | 1 | 330.000 | – | frostwolf 100 % |
| 234 | NAZZIVUS |  | 330.000 | 1 | 330.000 | – | fel_dorei 100 % |
| 235 | STILLPINE_FURBOLG |  | 330.000 | 1 | 330.000 | – | furbolg 100 % |
| 236 | CRAZED_WILDLIFE |  | 330.000 | 1 | 330.000 | – | owlkin 100 % |
| 237 | NESSTLEWOOD_OWLKIN |  | 330.000 | 1 | 330.000 | – | owlkin 100 % |
| 238 | SHADOW_RIDGE |  | 330.000 | 1 | 330.000 | – | sin_dorei 100 % |
| 239 | TALONBRANCH_GUARDIAN |  | 330.000 | 1 | 330.000 | – | tal_dorens 100 % |
| 240 | HYJAL_REBELLION |  | 330.000 | 1 | 330.000 | – | kal_dorei 100 % |
| 241 | LEGASH_CORRUPTION |  | 330.000 | 1 | 330.000 | – | fel_dorei 100 % |
| 242 | GREEN_DRAGONFLIGHT_ASHENVALE_GUARDIANS |  | 330.000 | 1 | 330.000 | – | green_dragon 100 % |
| 243 | FOULWEALD_FURBOLG |  | 330.000 | 1 | 330.000 | – | furbolg 100 % |
| 244 | BLOODWOOD_FURBOLG |  | 330.000 | 1 | 330.000 | – | furbolg 100 % |
| 245 | THISTLEFUR_FURBOLG |  | 330.000 | 1 | 330.000 | – | furbolg 100 % |
| 246 | BLACKROCK_NORTHSHIRE |  | 330.000 | 1 | 330.000 | – | mok_grondal 100 % |
| 247 | STONEMAUL_OGRE |  | 330.000 | 1 | 330.000 | – | mountain_ogre 100 % |
| 248 | SUMMIT_DEFENDERS |  | 330.000 | 1 | 330.000 | – | tauren 100 % |
| 249 | CENTIPAAR_LAIR |  | 330.000 | 1 | 330.000 | – | aqir 100 % |
| 250 | DUNEMAUL_OGRE |  | 330.000 | 1 | 330.000 | – | desert_ogre 100 % |
| 251 | CENARION_HOLD |  | 330.000 | 1 | 330.000 | – | kal_dorei 100 % |
| 252 | ANDORHAL |  | 325.000 | 1 | 325.000 | – | lordorean 100 % |
| 253 | MOKNATHAL |  | 319.200 | 1 | 319.200 | – | maghar_orc 100 % |
| 254 | SETHEKK |  | 316.000 | 1 | 316.000 | – | arakkoa 96 %, ethereal 4 % |
| 255 | CONSORTIUM |  | 314.100 | 3 | 104.700 | – | ethereal 59 %, goblin 20 %, sin_dorei 8 % |
| 256 | FALCON_WATCH |  | 313.600 | 1 | 313.600 | – | sin_dorei 91 %, forsaken 4 %, draenei 4 % |
| 257 | BONECHEWER_RUINS |  | 312.000 | 1 | 312.000 | – | felorc 100 % |
| 258 | GORDUNNI |  | 300.800 | 1 | 300.800 | – | gordunni_ogre 96 %, magnaron 4 % |
| 259 | HARDWRENCH_INDUSTRIES |  | 300.000 | 1 | 300.000 | – | goblin 100 % |
| 260 | PROTECTORATE |  | 292.000 | 1 | 292.000 | – | ethereal 99 %, nether_dragon 1 % |
| 261 | FIREWING_POINT |  | 288.800 | 1 | 288.800 | – | sin_dorei 78 %, kal_dorei 9 %, stormwindian 9 % |
| 262 | MURKBLOOD_TRIBE |  | 285.600 | 1 | 285.600 | – | krokul 100 % |
| 263 | CENARION_REFUGE |  | 284.000 | 3 | 94.666 | – | kal_dorei 50 %, tauren 35 %, krokul 5 % |
| 264 | VILEFIN_MURLOCS |  | 280.000 | 1 | 280.000 | – | warmwater_murloc 100 % |
| 265 | EMERALD_ENTRANCE_SERADANE |  | 280.000 | 1 | 280.000 | – | green_dragon 100 % |
| 266 | THUNDERLORD_STRONGHOLD |  | 279.200 | 1 | 279.200 | – | orgrimmari 68 %, tauren 14 %, jungle_troll 9 % |
| 267 | ZAXXIS |  | 277.600 | 1 | 277.600 | – | ethereal 77 %, mountain_giant 19 %, goblin 5 % |
| 268 | THE_EARTHEN_RING_AZ |  | 270.000 | 1 | 270.000 | – | orgrimmari 100 % |
| 269 | KURZEN_COMPOUND |  | 270.000 | 1 | 270.000 | – | stormwindian 100 % |
| 270 | GRISHNATH |  | 269.600 | 1 | 269.600 | – | arakkoa 82 %, mountain_ogre 18 % |
| 271 | VIR_AANI |  | 269.600 | 1 | 269.600 | – | ethereal 74 %, doom_guard 10 %, maghar_orc 7 % |
| 272 | TWILIGHT_CONVERT |  | 260.000 | 1 | 260.000 | – | darkiron 100 % |
| 273 | KIL_SORROW_CLAN |  | 257.600 | 1 | 257.600 | – | maghar_orc 95 %, mountain_ogre 5 % |
| 274 | RAZAANI |  | 256.800 | 1 | 256.800 | – | ethereal 89 %, mountain_ogre 11 % |
| 275 | CENARION_CIRCLE_OUTLAND |  | 255.200 | 1 | 255.200 | – | kal_dorei 51 %, tauren 18 %, black_dragon 16 % |
| 276 | AXEBITE_EXPEDITION |  | 250.000 | 1 | 250.000 | – | orgrimmari 100 % |
| 277 | HIGHBANK_EXPEDITION |  | 250.000 | 1 | 250.000 | – | stormwindian 100 % |
| 278 | REFUGE_POINT |  | 245.000 | 1 | 245.000 | – | stormwindian 100 % |
| 279 | HALAA |  | 240.800 | 1 | 240.800 | – | sin_dorei 48 %, draenei 36 %, stormwindian 11 % |
| 280 | TUUREM |  | 240.000 | 1 | 240.000 | – | krokul 98 %, sin_dorei 2 % |
| 281 | NETHERWING |  | 234.400 | 1 | 234.400 | – | nether_dragon 89 %, blue_dragon 5 %, stormwindian 5 % |
| 282 | GLOPGUT_CLAN |  | 230.000 | 1 | 230.000 | – | mountain_ogre 100 % |
| 283 | TORNFIN_MURLOCS |  | 230.000 | 1 | 230.000 | – | warmwater_murloc 100 % |
| 284 | DEADWIND_OGRE |  | 230.000 | 1 | 230.000 | – | mountain_ogre 100 % |
| 285 | ROCKJAW_TROGGS |  | 226.000 | 1 | 226.000 | – | trogg 100 % |
| 286 | UMBRAFEN_TRIBE |  | 221.600 | 1 | 221.600 | – | krokul 94 %, tauren 6 % |
| 287 | OGRILA |  | 220.000 | 1 | 220.000 | – | mountain_ogre 95 %, mountain_giant 5 % |
| 288 | SHATARI_SKYGUARD |  | 219.200 | 2 | 109.600 | – | stormwindian 46 %, sin_dorei 19 %, bronzebeard 15 % |
| 289 | REFUGEE_CAMP |  | 212.000 | 1 | 212.000 | – | krokul 30 %, draenei 24 %, arakkoa 18 % |
| 290 | LASHHAN |  | 204.800 | 1 | 204.800 | – | arakkoa 100 % |
| 291 | SHALASSI |  | 194.400 | 1 | 194.400 | – | arakkoa 65 %, draenei 35 % |
| 292 | BOOM |  | 192.000 | 1 | 192.000 | – | goblin 100 % |
| 293 | SYLVANNAR |  | 188.800 | 1 | 188.800 | – | kal_dorei 86 %, bronzebeard 14 % |
| 294 | MORGANS_VIGIL |  | 180.000 | 1 | 180.000 | – | stormwindian 100 % |
| 295 | WINDYREED_TRIBE |  | 180.000 | 1 | 180.000 | – | hill_ogre 67 %, krokul 33 % |
| 296 | RUUAN_OK |  | 172.800 | 1 | 172.800 | – | arakkoa 88 %, black_dragon 12 % |
| 297 | FERALFEN_TRIBE |  | 172.800 | 1 | 172.800 | – | krokul 100 % |
| 298 | DABYRIES_HUMANS |  | 170.000 | 1 | 170.000 | – | stormwindian 100 % |
| 299 | MARSHFIN_MURLOC |  | 170.000 | 1 | 170.000 | – | warmwater_murloc 100 % |
| 300 | SHA_TAR_OUTPOST |  | 169.600 | 1 | 169.600 | – | draenei 68 %, bronzebeard 32 % |
| 301 | VEKHNIR |  | 165.800 | 1 | 165.800 | – | arakkoa 71 %, mountain_ogre 29 % |
| 302 | SHA_TAR_ASSAULT |  | 163.400 | 1 | 163.400 | – | draenei 42 %, krokul 30 %, sin_dorei 20 % |
| 303 | WHITERBARK_TROLLS |  | 150.000 | 1 | 150.000 | – | forest_troll 100 % |
| 304 | GROMGOL_BASE |  | 150.000 | 1 | 150.000 | – | orgrimmari 100 % |
| 305 | HAALESH_TRIBE |  | 149.600 | 1 | 149.600 | – | arakkoa 89 %, bronzebeard 9 %, sin_dorei 3 % |
| 306 | NESINGWARY_EXPEDITION |  | 140.000 | 1 | 140.000 | – | bronzebeard 100 % |
| 307 | BLACKSCALE_NAGA |  | 130.000 | 1 | 130.000 | – | nazjatar 100 % |
| 308 | LOST_ONES |  | 130.000 | 1 | 130.000 | – | krokul 100 % |
| 309 | RHAZE |  | 128.000 | 1 | 128.000 | – | arakkoa 100 % |
| 310 | SKITH |  | 124.000 | 1 | 124.000 | – | arakkoa 87 %, stormwindian 13 % |
| 311 | MURKGILL_TRIBE |  | 120.000 | 1 | 120.000 | – | warmwater_murloc 100 % |
| 312 | ULDUM |  | 120.000 | 12 | 10.000 | – | sin_dorei 100 % |
| 313 | LITHIC |  | 108.000 | 1 | 108.000 | – | arakkoa 100 % |
| 314 | DRYWHISPER_KOBOLDS |  | 85.000 | 1 | 85.000 | – | kobold 100 % |
| 315 | CRUCIBLE_OF_CARNAGE_GLADIATOR |  | 72.000 | 1 | 72.000 | – | goblin 100 % |
| 316 | KIRIN_VAR |  | 64.000 | 1 | 64.000 | – | dalaranian 80 %, gnome 20 % |
| 317 | THE_EARTHEN_RING |  | 64.000 | 1 | 64.000 | – | maghar_orc 60 %, krokul 40 % |
| 318 | DARNASSUS_OUTPOST_EK |  | 34.860 | 1 | 34.860 | – | kal_dorei 100 % |
| 319 | KALIMDOR |  | 20.000 | 2 | 10.000 | – | sin_dorei 100 % |
| 320 | UNYIELDING_DEFENDER |  | 12.800 | 1 | 12.800 | – | stormwindian 100 % |
| 321 | DREANOR |  | 10.000 | 1 | 10.000 | – | sin_dorei 100 % |
| 322 | KULTIRAS |  | 10.000 | 1 | 10.000 | – | sin_dorei 100 % |
| 323 | LOSTISLES |  | 10.000 | 1 | 10.000 | – | sin_dorei 100 % |
| 324 | ZANDALAR |  | 10.000 | 1 | 10.000 | – | sin_dorei 100 % |
