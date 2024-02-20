import java.util.Scanner;

public class ujian {
    int[] HimpunanA;
    int[] HimpunanB;
    int[] HimpunanRelasi;
    int[] HimpunanAsal;
    int jumlahHimpunanA, jumlahHimpunanB, jumlahRelasi;
    Scanner input = new Scanner(System.in);

    public static void main(String args[]) {
        ujian obj = new ujian();
        obj.inputAnggota();
        obj.cetakHimpunan();
        obj.inputRelasi();
        obj.cekFungsi();
        obj.cetakRelasi();
    }

    public void inputAnggota() {
        System.out.println("ADE BINTANG SEPTIAN | 50423036");
        System.out.print("masukkan jumlah himpunan A = ");
        jumlahHimpunanA = input.nextInt();
        HimpunanA = new int[jumlahHimpunanA];
        for (int i = 0; i <= (jumlahHimpunanA - 1); i++) {
            System.out.print("Himpunan A yang ke " + (i+1) + " : ");
            HimpunanA[i] = input.nextInt();
        }

        System.out.print("masukkan jumlah himpunan B = ");
        jumlahHimpunanB = input.nextInt();
        HimpunanB = new int[jumlahHimpunanB];
        for (int i = 0; i <= (jumlahHimpunanB - 1); i++) {
            System.out.print("Himpunan B yang ke " + (i+1) + " : ");
            HimpunanB[i] = input.nextInt();
        }
    }

    public void cetakHimpunan() {
        System.out.print("Anggota Himpunan A = { ");
        for (int i = 0; i <= (jumlahHimpunanA - 1); i++) {
            System.out.print(HimpunanA[i] + " ");
        }
        System.out.println("}");

        System.out.print("Anggota Himpunan B = { ");
        for (int i = 0; i <= (jumlahHimpunanB - 1); i++) {
            System.out.print(HimpunanB[i] + " ");
        }
        System.out.println("}");

    }

    public void inputRelasi(){
        int jumlahRelasiMaks = jumlahHimpunanA * jumlahHimpunanB;
        System.out.println("Relasi maksimal adalah " + jumlahRelasiMaks);
        System.out.print(" ");

        do {
            System.out.print("Masukkan Jumlah Relasi yang terjadi : ");
            jumlahRelasi = input.nextInt();
        } while (jumlahRelasi > jumlahRelasiMaks);
        HimpunanRelasi = new int[jumlahRelasi];
        HimpunanAsal = new int[jumlahRelasi];
        System.out.println("Masukkan relasi yang terjadi : ");
        for (int i = 0; i <= (jumlahRelasi - 1); i++) {
            int[] temp = new int[jumlahRelasi];
            int[] temp2 = new int[jumlahRelasi];
            boolean SamaA = false;
            boolean SamaB = false;

            System.out.println("Relasi ke " + (i +1) + " : ");
            do {
                System.out.print(" Masukkan Asal A : ");
                temp[i] = input.nextInt();
                System.out.print("Masukkan Tujuan B : ");
                temp2[i] = input.nextInt();

                for (int j = 0; j <= (jumlahHimpunanA - 1); j++) {
                    if (temp[i] == HimpunanA[j]){
                        SamaA = true;
                    }
                }
                for (int k = 0; k <= (jumlahHimpunanB - 1); k++) {
                    if (temp2[i] == HimpunanB[k]){
                        SamaB = true;
                    }
                }
                if (SamaA == false || SamaB == false) {
                    System.out.println("Anggota Himpunan Tidak terdapat dihimpunan A atau B");
                }
                if (SamaA == true && SamaB == true) {
                    HimpunanRelasi[i] = temp2[i];
                    HimpunanAsal[i] = temp[i];
                }
            } while (SamaA == false || SamaB == false);
        }
    }

    public void cekFungsi() {
        int jumlahAnggota = 0;
        boolean adaSama = false;

        for (int i = 0; i <= (jumlahHimpunanA - 1); i++){
            for (int j = 0; j <= (jumlahRelasi - 1); j++){
                if (HimpunanA[i] == HimpunanAsal[j]) {
                    jumlahAnggota++;
                }
            }
        }
        for (int i = 0; i <+ (jumlahRelasi - 1); i++){
            for (int j = i + 1; j <= (jumlahRelasi - 1); j++){
                if (HimpunanA[i] == HimpunanAsal[j]) {
                    adaSama = true;
                }
            }
        }
        if (jumlahAnggota == jumlahHimpunanA && adaSama == false) {
            System.out.println("ADE BINTANG SEPTIAN");
            System.out.println("Relasi yang di input adalah fungsi");
        } else {
            System.out.println("Relasi yang di input bukan fungsi hanya relasi biasa" + jumlahAnggota + adaSama);
        }
    }

    public void cetakRelasi() {
        System.out.print("Daerah Domain = { ");
        for (int i = 0; i <= jumlahHimpunanA - 1; i++){
            System.out.print(HimpunanA[i] + " ");
        }
        System.out.println(" } ");

        System.out.print("Daerah Kodomain = { ");
        for (int i = 0; i <= jumlahHimpunanB - 1; i++){
            System.out.print(HimpunanB[i] + " ");
        }
        System.out.println(" } ");

        System.out.print("Daerah range adalah : { ");
        for (int i = 0; i <= jumlahRelasi - 1; i++){
            boolean adaSama = false;
            for (int j = i+1; j <= jumlahRelasi - 1; j++){
                if (HimpunanRelasi[i] == HimpunanRelasi[j]) {
                    adaSama = true;
            }   }
            if (adaSama == false) {
                System.out.print(HimpunanRelasi[i] + " ");
            }
        }
        System.out.print(" }");

    }
}