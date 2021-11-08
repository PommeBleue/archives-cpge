#include "struct.h"
#include "part1.h"

void tri_cluster(struct nuage* n){
	int pos;
	for(int i = 0; i < n->taille; i++){
		pos = i;
		while(pos > 0 && n->P[pos].x < n->P[pos - 1].x){
			struct point tmp = n->P[pos];
			n->P[pos] = n->P[pos - 1];
			n->P[pos - 1] = tmp;
			pos = pos - 1;
		}
	}
}

void plus_proches_cluster(struct cluster* c, int* p, int* q){
	if(n == NULL || p == NULL || q == NULL){
		return 
	}
	assert(c->taille > 1);
	double ref = distance(c->N->P[0], c->N->P[1]);
	*p = 0, *q = 0;
	for(int i = 0; i < c->taille; i++){
		for(int j = 0; j < c->taille; j++){
			if(distance(c->N->P[i], c->N->P[j]) < ref){
				*p = i, *q = j;
			}
		}
	}
}

/*
	Input:	
		c: paramètre de type pointeur sur struct cluster; cluster dont on veut former un sous-cluster
		min: paramètre de type double; abscisse minimale
		max: paramètre de type double; abscisse maximale
	Output: Sous-cluster du cluster c dont les abscisses sont comprises entre min et max.
**/
struct cluster* sous_cluster(struct cluster* c, double min, double max){
	assert(!(c == NULL))
	struct cluster* result;
	struct nuage* N;
	int a, b;
	for(int i = 1; i < c->taille; i++){
		if(c->N->P[c->abs[i]] >= min){
			a = i;
		}
	}
	for(int i = c->taille - 1; i >= 0; i--){
		if(c->N->P[c->abs[i]] <= max){
			b = i;
		}
	}
	result = (struct cluster*) malloc((b - a + 1)*sizeof(struct cluster));
	N = (struct nuage*) malloc((b - a + 1)*sizeof(struct nuage));
	result->abs = (int*) malloc((b - a +1)*sizeof(int));
	result->ord = (int*) malloc((b - a +1)*sizeof(int));
	N->taille = b - a + 1;
	result->taille = N->taille;
	for(int i = 0; i + a <= b; i++){
		result->abs[i] = c->abs[i + a];
		result->ord[i] = c->abs[i + a];
		N->P[i] = c->N->P[result->abs[i]];
	}
	result->N = N;
	return result;
}

/*
	Input:	
		c: paramètre de type pointeur sur struct cluster; cluster dont on veut récupérer la médiane
	Output: médiane du cluster fourni en paramètre
**/
double mediane(struct cluster* c){
	assert(!(c == NULL));
	return c->N->P[c->abs[c->taille/2]].x;
}

/*
	Input:	
		c: paramètre de type pointeur sur struct cluster; cluster dont on veut récupérer la partie gauche
	Output: Partie gauche du cluster fourni en paramètre
**/
struct cluster* gauche(struct cluster *c){
	return sous_cluster(c, c->N->P[c->abs[0]].x, mediane(c));
}

/*
	Input:	
		c: paramètre de type pointeur sur struct cluster; cluster dont on veut récupérer un sous-clusters dont les points sont à une distance au plus d0 de la médiane.
		d0: paramètre de type double; distance maximale de la médiane.
	Output: Bande centrale de largeur 2*d0.
**/
struct cluster* bande_centrale(struct cluster* c, double d0){
	return sous_cluster(c, mediane(c) - d0, mediane(c) + d0);
}

/*
	Input:	
		c: paramètre de type pointeur sur struct cluster; cluster nous permettant de retrouver G et D
		delta: paramètre de type double; distance maximale de la médiane.
		p: paramètre de type pointeur sur int; coordonnée du premier point
		q: paramètre de type pointeur sur int; coordonnée du second point
	Output: Vrai si les points G et D ont été trouvés, faux sinon. Modifie p et q en conséquence.
**/
bool cluster* fusion(struct cluster* c, double delta, int* p, int* q){
	double current, min;
	bool result = false;
	for(int i = 1; i <= 7; i++){
		for(int j = 0; j < c->taille - i; j++){
			if((c->ord[j] <= c->taille/2 && c->ord[j + i] <= c->taille/2) || (c->ord[j] > c->taille/2 && c->ord[i + j] > c->taille/2)) continue;
			current = distance(c->N->P[c->ord[j]], c->N->P[c->ord[j + i]]);
			if(current < delta){
				if(!result){
					result = true;
					min = current;
					*p = c->ord[j], *q = c->ord[j + i];
				}else{
					if(current < min){
						*p = c->ord[j], *q = c->ord[j + i];
					}
				}
			}
		}
	}
	return result;
}

void distance_minimale_rec(struct cluster* c, int* p, int* q){
	int p1 = 0, q2 = 0, p2 = 0, q2 = 0;
	double delta;
	bool f;
	if(c->taille <= 3){
		plus_proches_cluster(p, q);
		return;
	}
	distance_minimale_rec(gauche(c), &p1, &q1);
	distance_minimale_rec(droite(c), &p1, &q1);
	if(distance(c->N->P[p1], c->N->P[q1]) > distance(c->N->P[p2], c->N->P[q2])){
		*p = p2, *q = q2;
	}else{
		*p = p1, *q = q1;
	}
	delta = distance(c->N->P[p], c->N->P[q]);
	fusion(bande_centrale(c, delta), delta, p, q);
}

void distance_minimale(struct nuage* N, int* p, int* q){
	distance_minimale_rec(cluster_complet(N), p, q);
}


int main(){
	return 0;
}	
