struct point{
	double x, y;
}

struct nuage{
	int taille;
	struct point* P;
}

struct cluster{
	struct nuage* N;
	int taille;
	int* abs;
	int* ord;
}
