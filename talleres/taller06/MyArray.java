import java.util.Arrays;

public class MyArray {
    private int size;
    private final int TAMAÑO_INICIAL = 4;
    private Coordenada[] arr;

    public MyArray(){
        size = 0;
        arr = new Coordenada[TAMAÑO_INICIAL];
    }

    public void add(Coordenada a){
        if (size == arr.length){
            arr = Arrays.copyOf(arr, arr.length*2);
        }
        arr[size] = a;
        size++;
    }

    public void add(Coordenada a, int index) throws Exception{
        if (index < 0 || index > size)                          //arr.length - 1){
            throw new Exception("index: " + index);
        
        else if (size == arr.length)
            arr = Arrays.copyOf(arr, arr.length * 2);

        Coordenada temp = arr[index];
        for (int i = index ; i < size - 1; i++){
            Coordenada temp2 = arr[i+1];
            arr[i+1] = temp;
            temp = temp2;
        }
        arr[size] = temp;
        arr[index] = a;
        size++;
    }

    public Coordenada get(int index) throws Exception{
        if (index < 0 || index >= size)
            throw new Exception("index: " + index);
        
        return arr[index];
    }

    public void remove(){
        arr[size - 1] = null;
        size--;
    }

    public void remove(int index) throws Exception{
        if (index < 0 || index >= size)
            throw new Exception("index: " + index);

        for (int i = index; i < size - 1; i++){
            arr[i] = arr[i+1];
        }
        arr[size-1] = null;
        size--;
    }

    public String toString(){
        String temp = "[";
        for (int i = 0; i < size; i++){
            if (i != size - 1) temp += arr[i] + ",";
            else temp += arr[i];
        }
        temp += "]";
        return temp;
    }

}
