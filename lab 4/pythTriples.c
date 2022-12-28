#include <stdio.h>
#include <math.h>

double sideA;
double sideB;
double hyp;
double triples[3][3];

void takeTwoSides(double sideAIn, double sideBIn, int indexIn){
    sideA = sideAIn;
    sideB = sideBIn;

    hyp = sqrt(pow(sideA, 2) + pow(sideB, 2));

    triples[indexIn][0]= sideA;
    triples[indexIn][1] = sideB;
    triples[indexIn][2] = hyp;
}


void takeOneSideAndHyp(double sideAIn, double hypIn, int indexIn){
    sideA = sideAIn;
    hyp = hypIn;

    sideB = sqrt(pow(hyp, 2) - pow(sideA, 2));

    triples[indexIn][0] = sideA;
    triples[indexIn][1] = sideB;
    triples[indexIn][2] = hyp;
}

void takeOneSideAndHypSecond(void){
    sideA = 2;
    hyp = 3;

    sideB = sqrt(pow(hyp, 2) - pow(sideA, 2));

    triples[2][0] = sideA;
    triples[2][1] = sideB;
    triples[2][2] = hyp;
}

int main(void)
{

    takeTwoSides(3, 4, 0);

    takeOneSideAndHyp(1, sqrt(2), 1);

    takeOneSideAndHyp(2, 3, 2);

    for (int i = 0; i < triples[2][2]; i++)
    {

        int num = i + 1;

        printf("PythTriple %d [", num);
        for (int j = 0; j < triples[2][2]; j++)
        {
            switch (j)
            {
            case 0:
                printf("sideA = ");
                break;

            case 1:
                printf("sideB = ");
                break;

            case 2:
                printf("hyp = ");
                break;

            default:
                break;
            }
            printf("%.3f", round(triples[i][j] * 1000)/1000);

            if (j == 0 | j == 1)
            {
                printf(", ");
            }
        }
        printf("]\n");
    }
    return 0;
}