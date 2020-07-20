diagram.svg:	diagram.py weepeople.css
	python3 diagram.py > $@

weepeople.css:
	curl -qsL 'https://raw.githubusercontent.com/propublica/weepeople/master/weepeople.css' > $@
