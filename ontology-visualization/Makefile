all:
	python ontology_viz.py -o test.dot test.ttl -O test2.ttl
	dot -Tsvg -o ontology.svg test.dot
	xdg-open ontology.svg