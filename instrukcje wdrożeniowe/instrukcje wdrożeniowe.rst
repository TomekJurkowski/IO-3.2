INSTRUKCJA WDROŻENIOWA

1. Umieszczenie aplikacji  na serwerze:
	- zalogowanie na serwer: system@31.6.70.13
	- jeśli projekt nie znajduje się na serwerze - skopiowanie kodu Systemu z github'a: |br|
	  $ git clone https://github.com/piesu/IO-3.2
	- jeśli tam jest, to uaktualnienie: |br|
	  $ git pull
	- wejście to katalogu z systemem |br|
	  $ cd ./IO-3.2/
	- konfiguracja pliku /etc/nginx/sites-avaliable/systemIO.conf z poziomu administratora
	- umieszczenie dowiązania symbolicznego do wyżej wymienionego pliku |br|
	  w katalogu /etc/nginx/sites-enabled/: |br|
	  $cd /etc/nginx/sites-enabled/ |br|
	  $ln -s ../sites-avaliable/systemIO.conf |br|
	- restart daemon'a nginx z poziomu administratora: |br|
	  service nginx restart
	- skonfigurowanie pliku z ustawieniami: |br|
	  ./SystemKsiegowy/SystemKsiegowy/settings.py
	- aktywacja środowiska wirtualnego |br|
	  $ source ./srodowiskoIO/bin/activatesource ./srodowiskoIO/bin/activate
	- uruchomienie aplikacji systemowej: |br|
	  python ./SystemKsiegowy/SystemKsiegowy/manage.py runfcgi host=127.0.0.1 port=<port> |br|
	  [plik systemIO.conf w obecnej wersji jest do stosowany do portu 8098] |br|
	   wykupiona domena to kikraszak.tk)
	- system można przetestować pod adresem: |br|
	- jeśli projekt nie znajduje się na serwerze - skopiowanie kodu Systemu z github'a:
	  $ git clone https://github.com/piesu/IO-3.2
	- jeśli tam jest, to uaktualnienie:
	  $ git pull
	- wejście to katalogu z systemem
	  $ cd ./IO-3.2/
	- konfiguracja pliku /etc/nginx/sites-avaliable/systemIO.conf z poziomu administratora
	- umieszczenie dowiązania symbolicznego do wyżej wymienionego pliku
	  w katalogu /etc/nginx/sites-enabled/:
	  $cd /etc/nginx/sites-enabled/
	  $ln -s ../sites-avaliable/systemIO.conf
	- restart daemon'a nginx z poziomu administratora:
	  service nginx restart
	- skonfigurowanie pliku z ustawieniami:
	  ./SystemKsiegowy/SystemKsiegowy/settings.py
	- aktywacja środowiska wirtualnego
	  $ source ./srodowiskoIO/bin/activatesource ./srodowiskoIO/bin/activate
	- uruchomienie aplikacji systemowej:
	  python ./SystemKsiegowy/SystemKsiegowy/manage.py runfcgi host=127.0.0.1 port=<port>
	  [plik systemIO.conf w obecnej wersji jest do stosowany do portu 8098]
	   wykupiona domena to kikraszak.tk)
	- system można przetestować pod adresem:
	  http://kikraszak.tk:8099

