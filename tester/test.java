import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class test {
	public static void main (String args[])throws IOException{
		InputStreamReader im =new InputStreamReader(System.in);
		BufferedReader in=new BufferedReader(im);
		String s=in.readLine();
		int i=Integer.parseInt(in.readLine());
		System.out.println(s);
		System.out.println(i);
	}
}