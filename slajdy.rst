1.
Zarys prezentacji
  * "e-księgowość" - opis naszego systemu
  * główne funkcjonalności naszego systemu
  * zastosowana technologia, czyli słów kilka o Django
  * problemy jakie napotkaliśmy i rozwiązania, które zastosowaliśmy

2.
"e-księgowość" - charakterystyka
  Jest to system dedykowany ludziom prowadzącym indywidualną działalność
  gospodarczą jak i większym firmom, wspierający działanie księgowości.

3.
"e-księgowość" - charakterystyka
  Głównym zadaniem naszego systemu jest optymalizacja procesów finansowych
  przedsiębiorstwa, do której zaliczymy ułatiwenie pracy księgowości oraz
  skrócenie czasu pracy potrzebnego na przeprowadzenie tychże procesów.

4.
"e-księgowość" - charakterystyka
  Niezwykle ważnym aspektem "eksięgowości" jest fakt, iż jest to aplikacja
  "webowa" - nie wymagająca instalacji aplikacji na naszym komputerze.

5.
"e-księgowość" - funkcjonalności
  Na kolejnych slajdach znajdą się główne funkcjonalności dostarczane przez
  nasz produkt wraz z ich krótki opisem. Funkcjonalności są przedstawione w
  kolejności występowania w kolejnych iteracjach.

6.
"e-księgowość" - funkcjonalności - 1. iteracja
  * Podstawowe zarządzanie użytkownikami
    Pod tym hasłem kryje się umożliwienie rejestracji nowego użytkownika oraz
    logowania, bez którego użytkownik nie ma dostępu do pozostałych
    funkcjonalności systemu.

7.
"e-księgowość" - funkcjonalności - 1. iteracja
  * Księgowanie faktur sprzedaży:
    Aplikacja daje możliwość zaksięgowania faktury sprzedaży. Dodatkowo
    wprowadza automatyczne generowanie numeru faktury (numer ten wygląda tak:
    <data wprowadzenia faktury do systemu>/<liczba faktur wprowadzonych tego
    dnia>)

8.
"e-księgowość" - funkcjonalności - 1. iteracja
  * Księgowanie faktur zakupu:
    Skoro jest możliwośc księgowania faktur sprzedaży, nie mogłoby zabraknąć
    księgowania faktur zakupu.

9.
"e-księgowość" - funkcjonalności - 1. iteracja
  * Bilans otwarcia:
    Nasza aplikacja umozliwia wprowadzenie uproszczonego bilansu otwarcia,
    koniecznego do poprawnego funkcjonowania każdej działalności gospodarczej.
  
10.
"e-księgowość" - funkcjonalności - 1. iteracja
  * Księga Przychodów i Rozchodów:
    Uproszczona księga Przychodów i Rozchodów zawiera listę zaksięgowanych
    faktur sprzedaży i zakupu oraz pozycję "bilans otwarcia". Ponadto, widoczne
    jest podsumowanie przychodów i wydatków (rozchodów) firmy.

11.
"e-księgowość" - funkcjonalności - 1. iteracja
  * Księga Przychodów i Rozchodów - cdn.:
    Z poziomu "księgi PR" udostępniony jest dostęp do szczegółowego widoku
    dowolnej faktury.

12.
"e-księgowość" - funkcjonalności - 2. iteracja
  * Rozliczenie ZUS dla "idn":
    W drugiej iteracji pojawia się możliwość rozliczenia się z ZUS dla
    przedsiębiorców prowadzących indywidualną działalność gospodarczą.

13.
"e-księgowość" - funkcjonalności - 2. iteracja
  * VAT7:
    "e-księgowość" daje możliwość wypełnienia deklaracji dla podatku od towarów
    i usług - VAT7.

14.
"e-księgowość" - funkcjonalności - 2. iteracja
  * PIT-36L:
    Kolejną funkcjonalnością jest możliwość wypełnienia zeznania o wysokości
    osiągniętego dochodu (poniesionej straty) w roku podatkowym - PIT-36L.

15.
"e-księgowość" - funkcjonalności - 2. iteracja
  * Podstawowe wsparcie dla "e-Deklaracji":
    Pojawia się możliwość wysłania formularzy VAT7 oraz PIT-36L poprzez system
    "e-Deklaracje".

16.
"e-księgowość" - funkcjonalności - 2. iteracja
  * Ewidencja VAT:
    Kolejną funkcjonalnością wprowadzoną w drugiej iteracji naszego systemu jest
    możliwość prowadzenia ewidencji VAT.

17.
"e-księgowość" - funkcjonalności - 3. iteracja
  Funkcjonalności z kolejnych dwóch iteracji przedstawimy skrótowo:
  * integracja z kontem bankowym - tzw. "pełna księgowość"
  * rozliczenia ZUS dla pracowników
  * przetrzymywanie informacji o zatrudnionych pracownikach

18.
"e-księgowość" - funkcjonalności - 4. iteracja
  * zarządzanie użytkownikami - rozwinięcie 1. iteracji
  * zarządzanie uprawnieniami użytkowników
  * system płatności za nasz produkt

...



Moje slajdy o problemach na jakie się natknąłem:
Myślę, że sekcję problemów możemy zacząć od tych slajdów, potem już dowolna
kolejność:


x.
"e-księgowość" - problemy vs rozwiązania
  Głównym problemem jaki stanął na naszej drodze to ...

x+1.
"e-księgowość" - problemy vs rozwiązania
  ... nieznajomość niezwykle obszernej i trudnej dla laika dziedziny jaką jest
  prowadzenie księgowości.
  
x+2.
"e-księgowość" - problemy vs rozwiązania
  Jak można było przypuszczać, praktycznie "zerowe" doświadczenie naszego
  zespołu w prowadzeniu księgowości przysporzyło nam sporo problemów, które
  zaczęły się już w najwcześniejszych fazach (tworzenie diagramów m.in.
  przypadków użycia) i ciągną się do dnia dzisiejszego, czyli do fazy
  implementacji.

x+3.
"e-księgowość" - problemy vs rozwiązania
  Co zatem zrobiliśmy z tym problemem?
  Niestety nie udało nam się znaleźć jakiegoś genialnego tutoriala pt.
  "jak przyswoić wiedzę o księgowości w 24h", a także nie było nas stać na
  wynajęcie konsultanta.

x+4.
"e-księgowość" - problemy vs rozwiązania
  Nie pozostało nam zatem nic innego jak przebijanie się przez wikipedię,
  analizę podobnych systemów dostępnych na rynku oraz atakowanie pytaniami
  Grześka:)


A teraz moje slajdy:

y.
"e-księgowość" - problemy vs rozwiązania
  Kolejnym problemem technicznym, na który się natknęliśmy to jak umożliwić
  użytkownikowi wygodne dodawanie faktur zakupu. 

y+1.
"e-księgowość" - problemy vs rozwiązania
  Precyzyjniej, problem sprowadza się do wypełnienia kilkunastu pól formularza
  faktury (np. nazwa sprzedawcy, data wystawienia itd.), a następnie dodanie za
  pomocą kolejnego formularza pozycji do tejże faktury, z czego liczba pozycji
  powinna  być większa od zera i jednocześnie nieograniczona z góry.

y+2.
"e-księgowość" - problemy vs rozwiązania
  W przypadku, gdy chcemy dodać więcej pozycji niż jest na to miejsce w
  formularzu powinna być możliwość dostawienia kolejnej pozycji.

y+3.
"e-księgowość" - problemy vs rozwiązania
  Rozwiązanie jakie zastosowaliśmy polega na podzieleniu tworzenia faktury
  zakupu na dwa etapy: w pierwszym widoku użytkownik dostaje do uzupełnienia
  wszelkie pola faktury poza pozycjami i następnie może się przenieść do
  drugiego widoku, umożliwiającego dostawienie pozycji do faktury. W drugim
  widoku pojawia się klawisz "Dodaj kolejną pozycję" dostawiający pola dla
  dodatkowej pozycji i klawisz "Zaksięguj fakturę" - bez komentarza.

y+2.
"e-księgowość" - problemy vs rozwiązania
  Alternatywnym rozwiązaniem wartym rozważenia, ale wymagającym nieco większej
  znajomości technologii jest zastosowanie mechanizmu formset-ów udostępnianego
  przez Django. W skrócie umożliwia on dodawanie więcej niż jednego formularza
  do pojedynczego widoku. Po szczegóły odsyłamy do dokumentacji.

