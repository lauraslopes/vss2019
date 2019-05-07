
all: 
	g++ visao.cpp `pkg-config --cflags opencv` `pkg-config --libs opencv`-o visao
