import java.util.Scanner;

// Using java, write a program that prints out the numbers in the Fibonacci series
// between 1 and 50 i.e.
// The first ten Fibonacci numbers are:
// ```
// 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
// ```
// The logic behind is that each subsequent number is the sum of the previous two i.e
// 0,1 are the first two, then 1,1 are the next then 1,2 follows e.t.c
public class fibonacci{
	//fibonacci using loop
	public static int fiboNum(int num){
		if(num == 1 || num ==2){
			return 1;
		}
		int n1=0,n2=1,n3 = 1;
		System.out.println(n1+" "+n2);
		for(int i=3;i<=num;i++){
			n3=n1+n2;
			//System.out.println(" "+n3);
			n1=n2;
			n2=n3;
		}
		return n3;
	}
	public static void main(String args[]){
		System.out.print("Enter the number");
		int num = new Scanner(System.in).nextInt();
		System.out.println(num + " : ");
		//print upto num
		for(int i = 1; i<=num; i ++){
			System.out.println(fiboNum(i));
		}
	}
}
