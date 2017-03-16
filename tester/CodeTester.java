package code.tester;
import java.io.*;
import java.util.Scanner;

public class CodeTester {
    public static void main(String[] args) throws IOException{
        Scanner scan=new Scanner(System.in);
        String inp=scan.nextLine();
        String[] parts = inp.split(" ");
        int n=Integer.parseInt(parts[0]);
        int m=Integer.parseInt(parts[1]);
        int k=Integer.parseInt(parts[2]);
        String blank=scan.nextLine();
        int [][][]a=new int[k][n][m];
        for (int i=0;i<k;i++){
            for(int j=0;j<n;j++){
                for(int z=0;z<m;z++){
                    String ab=scan.next();
                    a[i][j][z]=Integer.parseInt(ab);
                }
                scan.nextInt();
            }
            String blank1=scan.nextLine();
        }
        System.out.println(a[0][0][0]);
    }
}