package equality;

public class workshop {
    public static void main(String[] args){
        int x1 = 99;
        int x2 = 99;
        int x3 = 100;
        System.out.println(x1 == x2);
        System.out.println(x1 == x3);

        String s1 = "Hello";
        String s2 = "Hello";
        String s3 = "Goodbye";
        String s4 = "He";
        s4 += "llo";
        String s5 = s4.intern();

        System.out.println(s1 == s2);
        System.out.println(s1 == s3);
        System.out.println(s1 == s4);
        System.out.println(s1 == s5);



    }
}
