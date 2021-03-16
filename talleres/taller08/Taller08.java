import java.util.Arrays;

public class Taller8{

  public static void mergeSort(int[] a){
    mergeSort(a, 0, a.length - 1);
  }

  private static void mergeSort(int[] a, int i, int f){     
    if (i < f){
      int mitad = i + ((f - i)/2);
      mergeSort(a, i, mitad);
      mergeSort(a, mitad+1, f);
      merge(a, i, mitad, f);
    }
  }
  
  private static void merge(int[] a, int inicio, int mitad, int fin){       
        int[] copy = Arrays.copyOf(a, a.length);

        int i = inicio;
        int j = mitad+1;
        int k = i;
 
        while (i <= mitad && j <= fin){
            if (copy[i] < copy[j]) {
              a[k] = copy[i]; 
              i++;       
            }
            else {
              a[k] = copy[j];
              j++;         
            }
          k++;     
        }

        while(i <= mitad){
          a[k] = copy[i];
          k++;
          i++;
        }
    }
  
  public static void quickSort(int[] a){
    quickSort(a, 0, a.length - 1);
  }

  private static void quickSort(int[] a, int i, int f){
    if (i>f)
      return;
      
    int pos = partition(a, i, f);    
    quickSort(a, i, pos-1);
    quickSort(a, pos+1, f);
  }

  private static int partition(int[] a, int i, int f){    
    int pivote = a[f];
    int indicePreviosAlPivote = i;
    for (int index = i; index < f; index++){
      if (a[index] <= pivote){
        swap(a, index, indicePreviosAlPivote);
        indicePreviosAlPivote++;
      }
    }
    swap(a, f, indicePreviosAlPivote);
    return indicePreviosAlPivote;
  }
  
  private static void swap(int[] a, int i, int j){
    int temp = a[i];
    a[i] = a[j];
    a[j] = temp;
  }  
}
