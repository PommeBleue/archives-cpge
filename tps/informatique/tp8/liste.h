#ifndef _LISTE_H
#define _LISTE_H

#include "couleur.h"

struct maillon {
	int depth;
	struct rectange* rect;
	struct maillon* m;
};
