
import java.lang.IndexOutOfBoundsException; // Usar esto cuando se salga el índice
import Node;

// Una lista simplemente enlazada
public class LinkedListDennis {

    Node first;
    private int size;
    
    public LinkedListDennis() {
        size = 0;
        first = null;
    }

    /**
     * Returns the node at the specified position in this list.
     *
     * @param index - index of the node to return
     * @return the node at the specified position in this list
     * @throws IndexOutOfBoundsException
     */
    private Node getNode(int index) throws IndexOutOfBoundsException {
        if (index >= 0 && index < size) {
            Node temp = first;
            for (int i = 0; i < index; i++) {
                temp = temp.next;
            }
            return temp;
        } else {
            throw new IndexOutOfBoundsException();
        }
    }

    /**
     * Returns the element at the specified position in this list.
     *
     * @param index - index of the element to return
     * @return the element at the specified position in this list
     */
    public int get(int index) {
        Node temp = null;
        try {
            temp = getNode(index);
        } catch (IndexOutOfBoundsException e) {
            e.printStackTrace();
            System.exit(0);
        }
        return temp.data;
    }

// Retorna el tamaño actual de la lista
    public int size() {
        return size;
    }

// Inserta un dato en la posición index
    public void insert(int data, int index)  {
        if index < 0 or index >= size:{
            return Exception("index : "+i)
        }
        if size == 0 and index > 0:{   
            return Exception("index : "+i)
        }   
        temp = Node(data)
        if index == 0:{
            temp.next = self.first
            self.first = temp
            self.size++
            return
        }
        Node temp = self.first
        for i in range (1, index): {
            temp = temp.next  
        temp = Node(data)
        temp.next= anterior.next
        anterior.next = temp     
        self.size+
        }
    }
// Borra el dato en la posición index

    public void remove(int index) 
    {
        Node borrar;
        borrar= this.getNode(index);
        if(index==0){
            first=first.next;
        }else{
            Node anterior=this.getNode(index-1);
            anterior.next=borrar.next;
            borrar.next=null;

        }
        size--;
    }

// Verifica si está un dato en la lista
    public boolean contains(int data) {
    
    Node temp=first;
    while (temp != null){
        if (temp.data=data)
        {
            return true;
            temp=temp.next
        }
    return false;
    }
    }
}

