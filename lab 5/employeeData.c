#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct employeeData {
    
    char empName[30];
    double empWage;
    double empHours;
};

int arrIndex = 0;
int numofEmps = 0;

void addEmployee(struct employeeData **empInfo, char name[], double hourlyWage, double hoursWorked) {
    
    strcpy((*empInfo)[arrIndex].empName, name);
    (*empInfo)[arrIndex].empWage = hourlyWage;
    (*empInfo)[arrIndex].empHours = hoursWorked;
    
    arrIndex++;
    numofEmps++;
}

void calcPaychecks(struct employeeData *empInfo) {
    
    double empCheck = 0;
    double avgCheck = 0;
    
    for (int i = 0; i < numofEmps; i++) {
        
        empCheck = empInfo[i].empWage * empInfo[i].empHours;
        
        printf
            ("Employee Data: %s, Wage: $%.2f, Hours: %.2f, Total Pay: $%.2f\n", 
            empInfo[i].empName, empInfo[i].empWage, empInfo[i].empHours, empCheck);
    
    avgCheck += empCheck;
    
    }

    printf("\nAverage paycheck: $%.2f\n", (avgCheck / numofEmps));
}

int main() {
    
    struct employeeData *empInfo = (struct employeeData *) malloc (5 * sizeof(struct employeeData));

    addEmployee(&empInfo, "Hulk Smith", 21, 21);
    addEmployee(&empInfo, "Loki Jones", 22.30, 12);
    addEmployee(&empInfo, "Kitty Cat", 21.55, 15);

    calcPaychecks(empInfo);
    
    return 0;
}