all: nbody.so

nbody.so: nbody.pyx
	cython -a nbody.pyx
	python3 setup.py build_ext -fi

clean:
	-rm -r build nbody.so nbody.c nbody.html
