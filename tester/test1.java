import java.io.IOException;
import java.util.Scanner;

public class test1 {
	public static void main (String args[])throws IOException{
		Scanner im=new Scanner(System.in);
		String s= im.next();
		System.out.println(s);
		int i=im.nextInt();
		System.out.println(i);
		im.close();
	}
}
