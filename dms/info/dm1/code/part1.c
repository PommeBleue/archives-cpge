#include <math.h>
#include "part1.h"
#include "struct.h"

/*
	Input: 
		p1: parameter of type struct point containing the coordinates of a point in an eucledian sapce
		p2: parameter of type struct point containing the coordinates of a point in an eucledian sapce
	Output: eucledian distance between these two points.
*/
double distance(struct point p1, struct point p2){
	return sqrt((p2.x-p1.x)*(p2.x-p1.x)+(p2.y-p1.y)*(p2.y-p1.y));
}

/*
	Input:
	Output: Void. Changes the values of p and q setting them to the indexes of the two closest points in the cloud.
*/
void plus_proches(struct nuage* n, int* p, int* q){
	if(n == NULL || p == NULL || q == NULL){
		return 
	}
	assert(n->taille > 1);
	double ref = distance(n->P[0], n->P[1]);
	*p = 0, *q = 0;
	for(int i = 0; i < n->taille; i++){
		for(int j = 0; j < n->taille; j++){
			if(distance(n->P[i], n->P[j]) < ref){
				*p = i, *q = j;
			}
		}
	}
}

int main(int argc, char** argv){
	return 0;
}
