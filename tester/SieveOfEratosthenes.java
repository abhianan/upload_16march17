package code.tester;
import java.io.IOException;

public class SieveOfEratosthenes {
    public static void main(String args[]) throws IOException{
        int n = 30;
        System.out.print("Following are the prime numbers ");
        System.out.println("smaller than or equal to " + n);
        sieveOfEratosthenes(n);
    }

    private static void sieveOfEratosthenes(int n) {
        boolean prime[] = new boolean[n+1];
        for(int i=1;i<=n;i++){
            prime[i]=true;
        }
        for(int j=2;j*j<=n;j++){
         if(prime[j]==true){
             for (int k=2*j;k<=n;k=k+j){
                 prime[k]=false;
             }
         }
        for(int i = 2; i <= n; i++)
        {
            if(prime[i] == true)
                System.out.print(i + " ");
        }
        }
    }
}
