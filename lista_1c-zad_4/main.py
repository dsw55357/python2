"""Stwórz moduł grafy.py , który zawiera funkcje do tworzenia, analizowania i
wizualizowania prostych grafów (np. wyszukiwanie ścieżek, obliczanie stopnia
wierzchołków, rysowanie grafów). Zaimportuj ten moduł do innego programu i użyj
go do analizy przykładowych grafów."""

from grafy import Graf, Wezel

def main():
    # Przykład użycia
    graf = Graf()

    wezel_a = Wezel("A")
    wezel_b = Wezel("B")
    wezel_c = Wezel("C")
    wezel_d = Wezel("D")

    graf.dodaj_krawedz(wezel_a, wezel_b)
    graf.dodaj_krawedz(wezel_b, wezel_c)
    graf.dodaj_krawedz(wezel_c, wezel_d)
    graf.dodaj_krawedz(wezel_a, wezel_d)

    # rysowanie grafów
    graf.wyswietl_graf()

    # obliczanie stopnia wierzchołków
    print(f"\n>> Stopien wierzcholkow:")
    stopien_a = graf.stopien_wierzcholka(wezel_a)
    stopien_b = graf.stopien_wierzcholka(wezel_b)
    stopien_c = graf.stopien_wierzcholka(wezel_c)
    stopien_d = graf.stopien_wierzcholka(wezel_d)

    print(f"Stopien wierzcholka A: {stopien_a}")
    print(f"Stopien wierzcholka B: {stopien_b}")
    print(f"Stopien wierzcholka C: {stopien_c}")
    print(f"Stopien wierzcholka D: {stopien_d}")

    # wyszukiwanie ścieżek
    print(f"\n>> Sciezka z A do D:")
    sciezka = graf.znajdz_sciezke2(wezel_a, wezel_d)

    print(f"\n>> Sciezka z A do C:")
    sciezka = graf.znajdz_sciezke2(wezel_a, wezel_c)

    print(f"\n>> Sciezka z B do D:")
    sciezka = graf.znajdz_sciezke2(wezel_b, wezel_d)

# https://hector.tu.kielce.pl/przedmioty/aisd-wyk/AiSD_w06.pdf

if __name__ == "__main__":
    main()