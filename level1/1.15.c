

int merg(int a, int arr_a[] , int b, int arr_b[],){

    int n = a+b;
    int merged[n];
    int j = 0; 
    int k = 0;
    
    for (int i = 0; i < n; i++){
        if (arr_a[j] > arr_b[k]){
            merged[i] = arr_a[j];
            j++;
        }
        else{
            merged[i] = arr_b[k];
            k++;
        };

    };

    return merged;
};