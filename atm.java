package javaapplication1;

import java.util.Scanner;

public class atm {
    private static Scanner input = new Scanner(System.in);
    private static String pin, Try, norek, JenisBayar;
    private static int pilihan, tarik, transfer, bayar, bank;
    private static int saldo = 500000000;
    
    public static void main(String[] args) {
        System.out.println("\tPT BANK BRI CABANG ENRKANG\n");
        System.out.println("massukkan PIN [Tekan \"ENTER\" Jika selesai memasukkan PIN]");
        pin = input.nextLine();
        
        if (pin.equals("1234 5678")){
            Try = "";
            do{
                transaksi();
                System.out.println("\naApakah Anda ingin mencoba lagi? Y/N");
                Try = input.nextLine();
            }while (Try.equalsIgnoreCase("Y"));
            
        }else{
            System.out.println("\nMaaf, nomor pin anda salah");
        }
    }

    private static void transaksi() {
        System.out.println("\n\tPT BRI CABANG ENREKANG");
        System.out.println("\tPilih jenis transaksi");
        System.out.println("1.Penarikan \t 3.Pembayaran");
        System.out.println("2.Transfer \t 4.Info Rekening");
        System.out.println("masukkan pilihan = ");
        pilihan = input.nextInt();
        
        switch(pilihan){
            case 1:
                System.out.println("\nPENARIKAN");
                penarikan();
                break;
            
            case 2:
                System.out.println("\nTRANSFER");
                transfer();
                break;
                
            case 3:
                System.out.println("\nPEMBAYARAN");
                pembayaran();
                break;
                
            case 4:
                System.out.println("\nINFO REKENING");
                inforek();
                break;
                
        }
    }     
    private static void penarikan() {
        int [] nominal = {50000, 100000, 200000, 300000, 500000, 750000, 1000000};
        System.out.println("1. 50000 \t 5. 500000");
        System.out.println("2. 100000 \t 6. 750000");
        System.out.println("3. 200000 \t 7. 1000000");
        System.out.println("4. 300000");
        tarik = input.nextInt();
        saldo = saldo - nominal [tarik-1];
        System.out.println("Penarikan tunai anda berhasil");
        System.out.println("saldo anda tersisa" + saldo);
        Try = input.nextLine();
    }
    private static void transfer() {
        System.out.println("\nmasukkan Jumlah Nominal Yang Akan Ditransfer = ");
        transfer = input.nextInt();
        
        System.out.println("\nPilih Tujuan Transfer = ");
        String [] Bank = {"Mandiri", "BRI", "BCA", "BNI", "CIMB Niaga"};
        System.out.println("1. Mandiri");
        System.out.println("2. BRI");
        System.out.println("3. BCA");
        System.out.println("4. BNI");
        System.out.println("5. CIMB Niaga");
        bank = input.nextInt();
        
        System.out.println("\nmasukkan Nomor Rekening Tujuan = ");
        input.nextLine();
        norek = input.nextLine();
        saldo = saldo - transfer;
        System.out.println("\nTransaksi Anda Berhasil, Berikut Rinciannya = ");
        System.out.println("BANK: "+Bank[bank-1] + "\nNo. Rek: " +norek + "\njumlah: "+transfer);
        System.out.println("Tekan \"ENTER\" untuk melanjuatkan");
        Try = input.nextLine();
        
    }
    private static void pembayaran() {
        System.out.println("Silahkan Masukkan Jenis Pembayaran = ");
        input.nextLine();
        String jenisBayar = input.nextLine();
        System.out.println("Masukkan Jumalah Uang Untuk Pembayaran = ");
        bayar = input.nextInt();
        saldo = saldo - bayar;
        System.out.println("\nPembayaran Anda Kepada "+ jenisBayar +" Berhasil");
        System.out.println("Saldo Anda Tersisa" + saldo);
        Try = input.nextLine();
        
    }
    private static void inforek() {
        System.out.println("\t Informasi Saldo");
        System.out.println("Saldo = "+ saldo);
        Try = input.nextLine();
    }
}
