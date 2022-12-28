#include <math.h>
#include <stdio.h>
#include "pythTriple.h"

struct pythTriple pythTrip[3];

void takeTwoSides(double sideAIn, double sideBIn, int indexIn) {

  double hyp = sqrt(pow(sideAIn, 2) + pow(sideBIn, 2));

  pythTrip[indexIn].sideA = sideAIn;
  pythTrip[indexIn].sideB = sideBIn;
  pythTrip[indexIn].hyp = hyp;
}

void takeOneSideAndHyp(double sideAIn, double hypIn, int indexIn) {

  double sideB = sqrt(pow(hypIn, 2) - pow(sideAIn, 2));

  pythTrip[indexIn].sideA = sideAIn;
  pythTrip[indexIn].sideB = sideB;
  pythTrip[indexIn].hyp = hypIn;
}

int main(void) {

  takeTwoSides(3, 4, 0);

  takeOneSideAndHyp(1, sqrt(2), 1);

  takeOneSideAndHyp(2, 3, 2);

  for (int i = 0; i < 3; i++) {

    printf("PythTriple %d [", i + 1);
    printf("sideA = %.3f", round(pythTrip[i].sideA * 1000) / 1000);
    printf(", sideB = %.3f", round(pythTrip[i].sideB * 1000) / 1000);
    printf(", hyp = %.3f", round(pythTrip[i].hyp * 1000) / 1000);


    printf("]\n");
  }
  return 0;
}