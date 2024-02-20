import java.util.Scanner;
public class percabangan {
  public static void main(String[] arg) {
    Scanner input = new Scanner(System.in);

    String nama, kelas, npm, grade;
    Double nUTS, nUAS, nAkhir;

    System.out.println("-! MENGHITUNG NILAI MAHASISWA !-");
    System.out.println("Masukkan Nama   : ");
    nama = input.nextLine();
    System.out.println("Masukkan Kelas  : ");
    kelas = input.nextLine();
    System.out.println("Masukkan NPM    : ");
    npm = input.nextLine();
    System.out.println("Nilai UTS       : ");
    nUTS = input.nextDouble();
    System.out.println("Nilai UAS       : ");
    nUAS = input.nextDouble();

    nAkhir = (0.7*nUTS + 0.3*nUAS);

    if (nAkhir >= 89) {
      System.out.println("Selamat, anda mendapat nilai A" + "\n" + "Dengan niali total : " + nAkhir);
    } else if (nAkhir < 89 && nAkhir >= 75) {
      System.out.println("Anda mendapat nilai B" + "\n" + "Dengan niali total : " + nAkhir);
    } else if (nAkhir < 75 && nAkhir >= 61) {
      System.out.println("Anda mendapat nilai C" + "\n" + "Dengan niali total : " + nAkhir);
    } else {
      System.out.println("Anda mendapat nilai D" + "\n" + "Dengan niali total : " + nAkhir);
    }
  }
}