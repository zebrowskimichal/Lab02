# CZ 1
#Ile ciagow znakow to palindromy + wypisz do drugiego pliku
# zad 1
def czyPalindrom(tekst):
    k = len(tekst) - 1
    p = 0
    while p < k:
        if tekst[p] != tekst[k]:
            return False
        p += 1
        k -= 1
    return True

# zad 2
#ile par ciagow znakow w pliku to anagramy + wypisz je (z indeksami) do drugiego pliku
def czyAnagramy(t1, t2):
    n1 = len(t1)
    n2 = len(t2)
    if n1 != n2:
        return False
    kontrolna = [0 for i in range(128)]
    for znak in t1:
        kontrolna[ord(znak)] += 1
    for znak in t2:
        kontrolna[ord(znak)] -= 1
    for i in range(65, 91, 1):
        if kontrolna[i] + kontrolna[i + 32] != 0:
            return False
    return True

#wczytaj tekst zadany, poprzez odbicie lustrzane zakoduj tekst i zdekoduj
# zad 3
def szyfrOdbicie(tekst):
    nowy = ""
    i = len(tekst) - 1
    while i > -1:
        nowy += tekst[i]
        i -= 1
    return nowy

#Szyfr Cezara- zmienia znaki o +3 w kodzie ASCII
# zad 4
def szyfrCezarProsty(tekst):
    nowy = ""
    for znak in tekst:
        nowy += chr(3 + ord(znak))
    return nowy

#Algorytm, ktory wskaze czy szukany ciag znakow wystepuje w przegladanym
# zad 5
def wyszukiwanieBF(t, p):
    m = len(p)
    n = len(t)
    i = 0
    while i < n - m + 1:
        j = 0
        while j < m:
            if p[j] != t[i + j]:
                break
            j += 1
        if j == m:
            return True
        i += 1
    return False

#Algorytm sprawdza czy w ciagu znakow istnieje i jaki jest najdluzszy palindrom
# zad 6
def najdluzszyPalindrom(tekst):
    for i in range(0, len(tekst) - 2):
        dl = len(tekst) - i
        for j in range(0, i + 1):
            if czyPalindrom(tekst[j:j + dl]):
                return tekst[j:j + dl]
    return None

#Algorytm Boyera-Moore'a
# zad 7
def pobierzSlownik(tekst):
    tmp = [0 for i in range(128)]
    for znak in tekst:
        tmp[ord(znak)] = 1
    sl = ""
    for i in range(128):
        if tmp[i] > 0:
            sl += chr(i)
    return sl

def bisekcja(znak, slownik):
    lb = 0
    ub = len(slownik) - 1
    while lb <= ub:
        mid = (lb + ub) // 2
        if slownik[mid] == znak:
            return mid
        elif slownik[mid] > znak:
            ub = mid - 1
        else:
            lb = mid + 1
    return -1


def uproszczonyBM(t, p):
    slownik = pobierzSlownik(p)
    m = len(p)
    n = len(t)
    i = 0
    while i < n - m + 1:
        j = m - 1
        while j > -1:
            if p[j] != t[j + i]:
                if bisekcja(t[i + j], slownik) == -1:
                    i += j
                break
            j -= 1
        if j == -1:
            return i
        i += 1
    return None

#Zmiana liczby dziesietnej na dowolny system (Dec2Any)
# zad 8
def generujMaske():
    maska = ""
    for i in range(48, 58):
        maska += chr(i)
    for i in range(65, 91):
        maska += chr(i)
    return maska


def dec2Any(liczba, system):
    maska = generujMaske()
    tmp = ""
    while liczba > 0:
        tmp += maska[liczba % system]
        liczba //= system
    return szyfrOdbicie(tmp)


#Dowolny system na dziesietny Any2Dec
def naWielka(znak):
    if ord(znak) >= 97 and ord(znak) <= 122:
        return chr(ord(znak) - 32)
    return znak


def any2Dec(liczba, system):
    maska = generujMaske()
    tmp = 0
    for znak in liczba:
        tmp *= system
        tmp += bisekcja(naWielka(znak), maska)
    return tmp

def main():
    print(any2Dec("11111100111", 2))  # 2023
    print(any2Dec("3747", 8))  # 2023
    print(any2Dec("7E7", 16))  # 2023
    print(any2Dec("3IM", 23))  # 2023

main()