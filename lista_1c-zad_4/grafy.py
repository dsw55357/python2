"""4. Stwórz moduł grafy.py , który zawiera funkcje do
tworzenia, analizowania i wizualizowania prostych grafów
(np. wyszukiwanie ścieżek, obliczanie stopnia wierzchołków, rysowanie grafów).
Zaimportuj ten moduł do innego programu i użyj go do analizy przykładowych grafów."""

class Wezel:
  def __init__(self, nazwa):
    self.nazwa = nazwa
    self.polaczenia = []

class Graf:
  def __init__(self):
    self.wezly = []

  def dodaj_wezel(self, wezel):
    self.wezly.append(wezel)

  def dodaj_krawedz(self, wezel1, wezel2):
    if wezel1 not in self.wezly:
      self.dodaj_wezel(wezel1)
    if wezel2 not in self.wezly:
      self.dodaj_wezel(wezel2)
    wezel1.polaczenia.append(wezel2)
    wezel2.polaczenia.append(wezel1)

# wezeł posiada stopień, oznaczający liczbę sąsiadujących z nim krawędzi
  def stopien_wierzcholka(self, wezel):
    stopien = 0
    for polaczenie in wezel.polaczenia:
      stopien += 1
    return stopien

  def wyswietl_graf(self):
    print(f"\n>> Wyswietl graf:")
    for wezel in self.wezly:
      print(wezel.nazwa, ":", end=" ")
      for polaczenie in wezel.polaczenia:
        print(polaczenie.nazwa, end=" ")
      print()

  def znajdz_sciezke(self, start, koniec):
    sciezka = []
    odwiedzone = set()

    def _znajdz_sciezke(wezel):
        if wezel == koniec:
            sciezka.append(wezel)
            return True
        if wezel in odwiedzone:
            return False

        odwiedzone.add(wezel)
        for polaczenie in wezel.polaczenia:
            if _znajdz_sciezke(polaczenie):
                sciezka.append(wezel)
                return True
        return False

    _znajdz_sciezke(start)

    sciezka.reverse()
    return sciezka

  def znajdz_sciezke2(self, start, koniec):
    sciezka = []
    odwiedzone = set()
    stack = [(start, [start])]

    while stack:
        (wezel, path) = stack.pop()
        if wezel == koniec:
            sciezka = path
            break
        if wezel not in odwiedzone:
            odwiedzone.add(wezel)
            for polaczenie in wezel.polaczenia:
                stack.append((polaczenie, path + [polaczenie]))

    #sciezka.reverse()
    for w in sciezka:
      print(f"- {w.nazwa} -", end="")

    return sciezka