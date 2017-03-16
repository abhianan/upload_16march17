import java.util.*;
import java.lang.*;
import java.io.*;

public class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
        Scanner scan=new Scanner(System.in);
        int n=scan.nextInt();
        int a[]=new int[n];
        for(int i=0;i<n;i++){
            a[i]=scan.nextInt();
        }
        System.out.println(maxor(a,n));
	}
	public static int maxor(int a[],int n){
	    int maxim=Integer.MIN_VALUE;
	    for(int i=0;i<n;i++){
	        int temp=0;
	        for(int j =i;j<n;j++){
	            temp=temp^a[j];
	            maxim=Math.max(temp,maxim);
	        }
	    }
	    return maxim;
	}
}
