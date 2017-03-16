import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class solution2 {
	public static void main (String args[])throws IOException{
		InputStreamReader im =new InputStreamReader(System.in);
		BufferedReader in=new BufferedReader(im);
		int T=Integer.parseInt(in.readLine());
		for(int t=1;t<=T;t++){
			int n=Integer.parseInt(in.readLine());
			int a=Integer.parseInt(in.readLine());
			int b=Integer.parseInt(in.readLine());
			for(int i=a;i<=b;i++){
				int c=0;
				for(int j=1;j<=i;j++){
					if(i%j==0){
						c=c+1;
					}
				}
				if(c==n){
					System.out.println(i);
				}
			}
		}
	}
}