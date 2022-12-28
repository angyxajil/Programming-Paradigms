#include <stdio.h>
#include <stdlib.h>
#include <time.h>
struct student
{
    int id;
    int age;
    double balance_owed;
};

double get_total(struct student *s, int length)
{
    float total = 0;
    
    for (int i = 0; i < length; i++)
    {
        total += s[i].balance_owed;
    }
    return total;
}

int main(int argc, char **argv)
{
    const int num_students = 10;
    srand(time(NULL)); // initialize random number generator
    struct student *curr_student;
    struct student *students = (struct student *)malloc(num_students * sizeof(struct student));

    for (int i = 0; i < num_students; i++)
    {
        curr_student = students + i;
        curr_student->id = i + 1;
        curr_student->age = (double)rand() / RAND_MAX * 25 + 15;
        curr_student->balance_owed = (double)rand() / RAND_MAX * 10000;
    }
    double total_balance = get_total(students, num_students);
    printf("Total owed = $%.2f\n", total_balance);
    return 0;
}