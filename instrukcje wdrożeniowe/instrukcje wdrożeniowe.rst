INSTRUKCJA WDROŻENIOWA

1. Umieszczenie aplikacji  na serwerze:
	- skopiowanie kodu Systemu z github'a:
	  git clone https://github.com/piesu/IO-3.2
	- konfiguracja pliku /etc/nginx/sites-avaliable/systemIO.conf
	- umieszczenie dowiązania symbolicznego do wyżej wymienionego pliku
	  w katalogu /etc/nginx/sites-enabled/:
	  cd /etc/nginx/sites-enabled/
	  ln -s ../sites-avaliable/systemIO.conf
	- restart daemon'a nginx:
	  service nginx restart
	- uruchomienie aplikacji systemowej:
	  python ./manage.py runfcgi host=127.0.0.1 port=<port>
	  (plik systemIO.conf w obecnej wersji jest do stosowany do portu 8099,
	   wykupiona domena to kikraszak.tk)
	- system można przetestować pod adresem:
	  http://kikraszak.tk:8098

