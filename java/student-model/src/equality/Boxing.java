package equality;

import java.util.ArrayList;
import java.util.List;

public class Boxing {
    public static void main(String[] args) {
        Integer i1= 99; // auto boxing
        Integer i = Integer.valueOf(99); // explicity box
        Integer i2 = new Integer(99);

        System.out.println(i == i1);// true
        System.out.println(i == i2); // false
        System.out.println(i == i2);

        List<Object> stuff = new ArrayList<>();
        stuff.add(99);
        Object o = stuff.get(0);
    }
}
