 import java.util.Scanner;
 
 class Calculator {
     static void cleaner() {
         System.out.print("\033[H\033[2J");
     }
     static void calculator() {
         Scanner input = new Scanner(System.in);
         System.out.print("Enter the first number: ");
         int num1 = input.nextInt();
         System.out.print("Enter the second number: ");
         int num2 = input.nextInt();
         System.out.print("Enter the operation: ");
         char opr = input.next().charAt(0);
         cleaner();
         int res = 0;
         
         switch (opr) {
             case '+':
                 res=num1+num2;
                 break;
             case '-':
                 res=num1-num2;
                 break;
             case '*':
                 res=num1*num2;
                 break;
             case '/':
                 res=num1/num2;
                 break;
             case '%':
                 res=num1%num2;
                 break;
             default: System.out.println("Operation not supported :-(");
                 break;
         }
         System.out.printf("%s %s %s is %s",num1,opr, num2,res);
     }
     public static void main(String[] args) {
         calculator();
         System.out.println("\n\n");
     }
 }
