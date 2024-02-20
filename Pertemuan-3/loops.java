import java.util.Scanner;
public class loops {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println(" ! MENCETAK SEGITIGA BINTANG ! ");
        System.out.println();

        int tinggi, i, j;

        System.out.print("Masukkan Tinggi : ");
        tinggi = input.nextInt();

        System.out.println();

        for(i=1; i<=tinggi; i++) {
            for(j=1; j<=i; j++) {
                System.out.print("*");
            }
            System.out.println("");
        }

    }
}