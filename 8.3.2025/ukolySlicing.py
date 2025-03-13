pohyby = [1200, -250, -800, 540, 721, -613, -222]

print(pohyby[2])

print(pohyby[2:])



print(len(pohyby))


print(min(pohyby))
print(max(pohyby))
 
print(sum(pohyby))


# Vypište v pořadí třetí pohyb z uvedeného seznamu.
# Vypište všechny pohyby kromě prvních dvou.
# Vypište kolik je všech pohybů dohromady.
# Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
# Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný.


# Mějme proměnnou s, ve které předpokládáme uložený nějaký seznam. 
# Sestavte v výraz (vzoreček), který spočítá průměrnou hodnotu v takovém seznamu. 
# Otestujte jej na seznamech různých délek.

s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
v = sum(s)/len(s)
print(v)


# Postupujte obdobně jako v úložce Průměr, 
# ale tentokrát sestavte výraz pro výpočet rozpětí, 
# tedy rozdílu mezi minimální a maximální hodnotou.

rozdil =  max(s) - min(s) 

print(rozdil)