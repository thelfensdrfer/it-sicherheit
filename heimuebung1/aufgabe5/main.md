## Aufgabe 5

1.

    Ja. Dazu muss sich der Angreifer zwei Tags ausgeben lassen, t_1 und t_2.
    
    * t_1 = MAC'_k(m_0 || x)
    * t_2 = MAC'_k(x || m_1)
    
    mit |x| = |m_0|. Nun wird die zweite Hälfte von t_1 mit der zweiten Hälfte von t_2 ausgetauscht. Der daraus resultierende Cyphertext enthält dann MAC'_k(m_0 || m_1).

2. Analog zu 1 nur mit einem Zusatzschritt, da die Reihenfolge hier nicht vertausch werden kann.
