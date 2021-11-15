#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "peintre.h"
#include "liste.h"

struct toile *enonce(){
  struct rectangle rect_vert = {.x = 165, .y = 10, .larg = 60, .haut = 20,
                           .c = {.r = 0, .g = 200, .b = 0 } };
  struct rectangle rect_bleu = {.x = 80, .y = 40, .larg = 60, .haut = 40,
                           .c = {.r = 0, .g = 0, .b = 255 } };
  struct rectangle rect_rouge = {.x = 40, .y = 60, .larg = 80, .haut = 30,
                           .c = {.r = 255, .g = 0, .b = 0 } };
  struct toile *fond = canevas(200, 120);
  trace(&rect_vert, fond);
  trace(&rect_bleu, fond);
  trace(&rect_rouge, fond);
  return fond;
}

//feet Kasimir Malevitch
struct toile *suprematism1915(){
  struct toile *fond = canevas(400, 600);
  struct rectangle rect[] =
    { {.x = 200, .y = 10, .larg = 40, .haut = 600,
       .c = {.r = 0, .g = 0, .b = 0 } },
      {.x = 20, .y = 10, .larg = 370, .haut = 25,
       .c = {.r = 200, .g = 0, .b = 0 } },
      {.x = 60, .y = 60, .larg = 300, .haut = 50,
       .c = {.r = 200, .g = 0, .b = 0 } },
      {.x = 20, .y = 150, .larg = 230, .haut = 20,
       .c = {.r = 200, .g = 0, .b = 0 } },
      {.x = 80, .y = 550, .larg = 300, .haut = 25,
       .c = {.r = 200, .g = 0, .b = 0 } },
      {.x = 0, .y = 330, .larg = 380, .haut = 20,
       .c = {.r = 0, .g = 0, .b = 0 } },
      {.x = 95, .y = 380, .larg = 25, .haut = 120,
       .c = {.r = 200, .g = 0, .b = 0 } },
      {.x = 5, .y = 430, .larg = 80, .haut = 60,
       .c = {.r = 255, .g = 234, .b = 128 } },
      {.x = 290, .y = 225, .larg = 20, .haut = 30,
       .c = {.r = 255, .g = 234, .b = 128 } },
      {.x = 300, .y = 160, .larg = 40, .haut = 60,
       .c = {.r = 102, .g = 25, .b = 255 } }
    };
  for(int i=0; i<10; i=i+1){
    trace(&rect[i], fond);
  }
  return fond;
}

struct toile *canevas(int largeur, int hauteur){
	struct toile* result = (struct toile*) malloc(sizeof(struct toile));
	result->larg = largeur;
	result->haut = hauteur;
	result->c = (struct couleur**) malloc(hauteur*sizeof(struct couelur*));
	for(int i = 0; i < hauteur; i++){
		result->c[i] = (struct couleur*) malloc(largeur*sizeof(struct couleur));
		for(int j = 0; j < largeur; j++){
			result->c[i][j] = blanc;
		}
	}
	return result;	
}


void detruit_toile(struct toile* tableau){
	for(int i = 0; i < tableau->haut; i++){
			free(tableau->c[i]);
	}
	free(tableau->c);
	free(tableau);
}

void trace(struct rectangle* rect, struct toile* tableau){
	for(int i = 0; i < tableau->haut; i++){
		if(i >= rect->x && i <= rect->x + tableau->haut - 1){
			for(int j = 0; j < tableau->larg; j++){
				if(j >= rect->y && j <= rect->y + tableau->larg - 1){
					tableau->c[i][j] = rect->c;
				}
			}
		}
	}
}

void affiche(struct toile* tableau){
	printf("P3\n%d %d\n%d\n", tableau->larg, tableau->haut, 255);
	for(int i = 0; i < tableau->haut; i++){
		for(int j = 0; j < tableau->larg; j++){
			affiche_couleur(tableau->c[i][j]);
		}
		printf("\n");
	}
}

void perspective(struct toile* talbeau, struct maillon* m){
	do{
		trace(m->rect, tableau);
		m = m->m;
	}while(m->depth != 1);
}

struct maillon* ajout_objet(struct maillon* rects, struct rectangle* rect, int depth){
	struct maillon* result = (struct maillon*) malloc(sizeof(struct maillon));
	int i; 
	bool spotted = false;	
	do{
		if(spotted){
			result->m = (struct maillon*) malloc(sizeof(struct maillon));
			result->rect = rects->rect;
			result->depth = depth + i;
			i++; 
			result = result->m;
			rects = rects->m;
		else if(rects->depth == depth){
			result->rect = rect;
			result->depth = depth;
			result->m = (struct maillon*) malloc(sizeof(sturct maillon));
			result = result->m;
			i = 1;
			spotted = true;
		else{
			result->rect = rects->rect;
			result->depth = rects->depth;
			result->m = (struct maillon*) malloc(sizeof(struct maillon));
			result = result->m;
			rects = rects->m;
		}			
	}while(rects->depth != 1);
}

int main(){
	struct toile *t = enonce();
	affiche(t);
	detruit_toile(t);
}
