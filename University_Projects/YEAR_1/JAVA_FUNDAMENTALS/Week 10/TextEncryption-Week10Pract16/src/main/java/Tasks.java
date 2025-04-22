/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author x7e30
 */

public class Tasks 
{

    
    public static void main(String[] args)
    {
        Encrypter encr = new Encrypter();
        String encryptedTextA = encr.encryptWithKey("gelidity", "&*()sHASIHs!¬`/~~#sRQJAL");
        String encryptedTextB = encr.encryptWithKey("aWord", "&*()sHASIHs!¬`/~~#sRQJAL");
        String encryptedTextC = encr.encryptWithKey("of today", "&*()sHASIHs!¬`/~~#sRQJAL");
        
        System.out.println(encr.decipher(encryptedTextA));
        System.out.println(encr.decipher(encryptedTextB));
        System.out.println(encr.decipher(encryptedTextC));
        System.out.println("Size before reallocation: " + Encrypter.encryptedTextID.length);
        
        String encryptedTextD = encr.encryptWithKey("of today", "&*()sHASIHs!¬`/~~#sRQJAL");
        System.out.println("Size after reallocation: " + Encrypter.encryptedTextID.length);
        System.out.println(encr.decipher(encryptedTextA));
        System.out.println(encr.decipher(encryptedTextB));
        System.out.println(encr.decipher(encryptedTextC));
//        String[] eg = {"dds", "cake", "bread"};
//        System.out.println("Size before allocation " + eg.length);
//        
//        System.out.println("Size after allocation " + eg.length);
    }
}
