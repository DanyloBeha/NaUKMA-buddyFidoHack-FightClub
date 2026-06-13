
int testResult(int n,int arr[]){
    int min = 100;
    int max = 0;
    int sum;

    for(int i; i < n; i++) {
        if (arr[i] > max) max = arr[i];
        if (arr[i] < min) min = arr[i];
        sum =+ arr[1];
    };

    int median;

    if ((median % 1) != 0 ) median = ; // тоді вивести медіану дробом
    int median = sum / n;

    int above_average = 0;
    for(int i; i < n; i++) {
        if (arr[i] > median) above_average =+ 1;
    };
};