#include <iostream>
#include <cmath>
#include <cstdlib>

using namespace std;

// La función que se desea integrar, que retornará un valor de tipo double (decimal)
// Recibe el argumento numérico x
double f(double x) {
	// Función exponencial, e^x
	//return exp(x);

	// Si desea integrar x al cubo de a -> b:
	// return x*x*x;
	// ó podría hacer:
	//return pow(x, 3);
	// Deberá dejar solo un return activo

	return 1.0/(1+exp(-x));
}

// Función que ejecuta la regla de Simpson, recibe 3 argumentos: a, b y N
// Donde:
//  a: límite inferior
//  b: límite superior
//  N: cuantas divisiones se harán
// Devuelve un valor de tipo double (decimal)
double Simpson(double a, double b, int N) {
	// Si N no es número par, abortar.
	if (N % 2) {
		cout << "N debe de ser un número par" << endl;
		exit(EXIT_FAILURE);
	}

	// La separación entre cada suma
	double dx = (b-a)/N;
	
	// Se declara una variable, a la cual se le irán sumando todas las evaluaciones, desde x = a, hasta x = b, con pasos a+xi
	double Suma = 0;

	// Repetir el siguiente bucle N veces, i empieza en 0, y termina en N
	for (int i = 0; i <= N; i++) {
		// Si es el inicio del búcle, evaluar f(a+xi) y agregar a la variable Suma
		if(i == 0) {
			Suma += f(a);
		// Si es el final del búcle, evaluar f(a+xi) y agregar a la variable Suma
		} else if (i == N) {
			Suma += f(b);
		// Sí i es par, entonces evaluar f(a+xi), multiplicar por 2, y agregar a la variable Suma
		} else if (!(i % 2)) {
			Suma += 2*f(a+i*dx);
		// Sí i es impar, entonces evaluar f(a+xi), multiplicar por 4, y agregar a la variable Suma
		} else {
			Suma += 4*f(a+i*dx);
		}
		// Lo anterior es igual a: (f(X0) + 4f(X1) + 2f(X2) + 4f(X3)... 2f(Xn-2) + 4f(Xn-1) + f(n))
	}
	// Multiplicar la suma por dx/3, y devolver el valor.
	return Suma*(dx/3.0);
}

// Aquí inicia el programa
int main()
{
	// Se crea una variable sum
	// a la cual se le asignará el valor de la funcion Simpson
	// evaluada entre 2 y 6, con N=40 divisiones
	double SumaSimpson = Simpson(2, 6, 40);
	
	// Imprimir a la consola el valor de la integral
	cout << SumaSimpson << std::endl;

	// Termina el programa sin problemas.
	return 0;
}
