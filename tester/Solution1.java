import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Solution1 {
	public static void main (String args[])throws IOException{
		InputStreamReader im =new InputStreamReader(System.in);
		BufferedReader in=new BufferedReader(im);
		int T=Integer.parseInt(in.readLine());
		for(int t=1;t<=T;t++){
			int N=Integer.parseInt(in.readLine());
			factorial(N);
		}
	}
	public static void factorial(int n) {
	       BigInteger fact = new BigInteger("1");
	       for (int i = 1; i <= n; i++) {
	           fact = fact.multiply(BigInteger.valueOf(i));
	       }
	       BigInteger num=new BigInteger("1000000007");
	       BigInteger fact1=fact.mod(num);
	       System.out.println(fact1);
	}
}
