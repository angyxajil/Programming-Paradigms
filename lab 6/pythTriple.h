// put the struct definition and function prototypes in a .h file and include it
// in the .c file

#ifndef PYTHTRIPLE
#define PYTHTRIPLE

struct pythTriple {
  double sideA;
  double sideB;
  double hyp;
};

void inputTwoSides(double, double, int);
void inputOnseSideAndHyp(int, double, double);
void takeOneSideAndHypSecond(void);

#endif