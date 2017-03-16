import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
	public static void main (String args[])throws IOException{
		InputStreamReader im =new InputStreamReader(System.in);
		BufferedReader in=new BufferedReader(im);
		int T=Integer.parseInt(in.readLine());
		for(int t=1;t<=T;t++){
			int N=Integer.parseInt(in.readLine());
			if(N%11==0){
				System.out.println("Yes");
			}else{
				int s=0;
				for(int i = 1;i<=10;i++){
					if((N+i) % 11 ==0 || (N-i)%11 ==0){
						s=i;
						break;
					}
				}
				System.out.println(s);
			}
		}
	}
}
