## Aufgabe 2

1. Verschlüsselungsverfahren mit 56 Bit Schlüssellänge (DES):
    1. Durchschnitt: `2^(56 - 1) = 2^55 = 36.028.797.018.963.968`
    2. Worst-Case: `2^56 = 72.057.594.037.927.936`
2. `10^7` DES-Verschlüsselungen bei 56 Bit Schlüssellänge pro Sekunde
    * `2^55 / (10^7 1/s) = 3,6028797018963968 × 10^9s =~ 41700 Tage = 114 Jahre und 89 Tage`
3. `35.000 / 700 = 50 => 50*10^7` DES-Verschlüsselungen bei 56 Bit Schlüssellänge pro Sekunde
    * `2^55 / (50 * 10^7 1/s) = 7.2057594037927936 × 10^7s =~ 834 Tage = 2 Jahre und 103 Tage`
4. `180 * 4 * 120 * 10^6` DES-Verschlüsselungen bei 56 Bit Schlüssellänge pro Sekunde
    * `2^55 / (180 * 4 * 120 * 10^6 1/s) = 417.000s =~ 4 Tage und 20 Stunden`
