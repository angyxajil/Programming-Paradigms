#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//A house is represented by a struct with an number of bedrooms, represented by an int
//and a size in square feet, represented by a double.
struct houseArray
{
    int numOfBeds;
    double size;
};

/**
 * double get_avg_size(struct house *h, int length)
 *  calculates and returns the average size of the houses in the array.
 *  Uses *pointer arithmetic* to step through the array.
 */

double get_avg_size(struct houseArray *h, int length)
{
    int numHouses = 0;
    int allHouseSize = 0;
    int avgSize;

    for (int i = 0; i < length; i++)
    {
        numHouses++;
        allHouseSize += h[i].size;
    }
    return avgSize / allHouseSize;
}

//prints out the number of bedrooms and size of each house in the array. 
void show_houses(struct house *h, int length) {

    for (int i = 0; i < length; i++)
    {
        printf("Num of Bedrooms: %d", h[i].numOfBeds);
        printf("House Size: %d", h[i].size);
    }

}

int main(void)
{
    
}
//uses malloc to create an array of three houses and hard codes the size and number of bedrooms
//for each house, then runs show_houses, the runs get_avg_size and prints the result