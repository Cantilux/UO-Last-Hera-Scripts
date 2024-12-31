# buff.py

Questo script lancia le spell di **buff di magery**.

- **Bless** per aumento delle statistiche
- **Protection** per aumentare il valore di armatura
- **Reactive Armor** per danno riflesso con colpi subiti

Le spell vengono lanciate solo se il personaggio li ha già presenti.

Quando viene usata la spell **Bless**, aumentano anche gli hitpoint massimi. In questo caso lo script lancia la magia di **Heal** per riportare git hitpoint correnti al valore massimo.

Alla fine dello script vengono riequipaggiate le armi e usata la skill meditation.

# heal_magery.py

Questo script lancia la spell **heal** per curare il personaggio.

Vengono rimosse le armi, lanciata la spell, riequipaggiate le armi e reimpostato il last attack sull'ultimo bersaglio prima della spell.

# two_weapon.py

Questo script permette l'interscambio tra un'arma primaria e una secondaria. Al momento è impostato per scimitarra e scudo come primaria e alabarda come secondaria.

Lo script darà sempre priorità all'arma primaria. Se si è disarmati, si ha solo lo scudo o solo l'arma, andrà ad equipaggiare arma e scudo, mentre nel caso si avrà arma e scudo in mano equipaggerà l'arma secondaria.

Un esempio di utilizzo è per la classe arciere che può passare da kryss e scudo ad arco.

**Importante:** definire il seriale delle armi nelle prime righe.
