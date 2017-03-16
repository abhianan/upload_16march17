import java.util.Scanner;

public class Code {
	public static void main (String args[])throws Exception{
		Scanner in =new Scanner(System.in);
		int T=in.nextInt();
		for(int t=1;t<=T;t++){
			int c=in.nextInt();
			int nitem=in.nextInt();
			int[] item=new int[nitem];
			for(int i=0;i<nitem;i++){
				item[i]=in.nextInt();
			}
			int f=0;
			int g=0;
			int h=0;
			for(int j=0;j<item.length;j++){
				for(int k=0;k<item.length;k++){
					if(j!=k){
						if(item[j]+item[k]==c){
							f=j+1;
							g=k+1;
							h++;
							break;
						}
					}
				}if(h>0){
					System.out.printf("Case #%d: %d %d\n", t,f,g);
					break;
				}
			}
		}
		in.close();
	}
}
