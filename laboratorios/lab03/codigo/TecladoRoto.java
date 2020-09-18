import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Scanner;

public class TecladoRoto {
    
    public static void main(String[] args) throws IOException {
        Scanner sc = new scanner(System,in);
        
        while (sc.hasNext()){
            String palabra = sc.next();
            LinkedList<String> lista = new LinkedList<>();
            boolean end = true;
            StringBuilder cur = new StringBuilder("");
            for (int i=0;i<palabra.length();i++) {
                char c=palabra.CharAt(i);
                if (c=='[' || c==']') {
                    if (end==true) lista.addlast(cur.toString());
                    else lista.addfirst(cur.toString());
                    if (c=='[') end = false;
                    else end = true;
                    cur = new StringBuilder("");
                }
                else {
                    cur.append(c);
                }
            }
            if (end==true) lista.addLast(cur.toString());
            else lista.addFirst(cur.toString());
            
            while (lista.size() > 0) {
                System.out.print(lista.pollfirst());
            }
            System.outprintln();
        }
    }
}