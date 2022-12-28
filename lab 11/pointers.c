#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Use this struct definition:
struct student
{
    char name[10];
    int id;
    double gpa;
};

// prototypes
int search_by_id(struct student *students, int length);
int search_by_name(struct student *students, int length);
void show_student(struct student *curr, int index);

int id; 
char name[10];

// shows output for the student at the specified index
void show_student(struct student *curr, int index) {
    printf("%s has id %d and gpa %.2f", curr[index].name, curr[index].id, curr[index].gpa);
}

int search_by_name(struct student *students, int length) {
    // asks the user for a student name
    printf("Enter the name to search for:\n");
    scanf("%11s", &name);

    // searches the array for a student with that name
    for (int i = 0; i < length; i++) {

        // If a student is found, return the array index.
        if (strcmp(students[i].name, name) == 0)
            return i;

    }
    // Otherwise return -1.
    return -1;
}

int search_by_id(struct student *students, int length) {
    // asks the user for a student id
    printf("Enter the id to search for:\n");
    scanf("%d", &id);

    // searches the array for a student with that id
    for (int i = 0; i < length; i++) {
        // If a student is found, return the array index.
        if (students[i].id == id)
            return i;
    }
    // Otherwise return -1.
    return -1;
}

// int main(void)
int main(void) {
    // creates an array of 4 students on the heal (use malloc) 
    struct student *students = (struct student *)malloc(4 * sizeof(struct student));

    // hard codes values for their names, ids, and gpas
    // Use the string functtion strcpy to set the name of each student
    // like this: strcpy(curr->name, "Fred"); 
    struct student *curr = students;

    strcpy(curr->name, "Angy");
    curr->id = 1;
    curr->gpa = 4.0;

    curr = students + 1;
    
    strcpy(curr->name, "Loki");
    curr->id = 2;
    curr->gpa = 3.69;

    curr = students + 2;

    strcpy(curr->name, "Jessy");
    curr->id = 3;
    curr->gpa = 5.43;

    curr = students + 3;

    strcpy(curr->name, "Carlos");
    curr->id = 4;
    curr->gpa = 2.0;

    // asks the user to choose search_by_name or search_by_id,
    printf("Enter n for search by name or i for search by ID:\n");
    char idOrName = getchar();

    // sets the function pointer to the correct function,
    int (*search_by_id_ptr)(struct student *, int) = &search_by_id;
    int (*search_by_name_ptr)(struct student *, int) = &search_by_name;

    // and calls the function
    if (idOrName == 'n') {
        int index = (*search_by_name_ptr)(students, 4);
        // if the search function returns -1
        if (index == -1)
            // shows that no student was found
            printf("Not found");
        else
            // otherwise uses the return value of the function
            // to call show_student to show data for that student.
            show_student(students, index);
    }

    // and calls the function
    if (idOrName == 'i') {

        int index = (*search_by_id_ptr)(students, 4);
        // if the search function returns -1
        if (index == -1)
            printf("Not found");
        else
            show_student(students, index);
    }
}