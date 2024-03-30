all: index.html

index.html: index.md template.html
	pandoc --template template.html -f markdown -t html5 index.md -o index.html
	prettier index.html --write

clean:
	rm -rf index.html
