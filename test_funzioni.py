from main import funzione

def test_1():
	assert funzione(3,2,1) == 5

def test_2():
	assert funzione(3,3,2) != 4

def test_3():
	assert funzione(3,3,2) == 9


