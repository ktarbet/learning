package flyweight;

import java.util.HashMap;
import java.util.Map;

public class Sport {
    public String getName() {
        return name;
    }
    private String name;

    private static Map<String,Sport> values = new HashMap<>();
    private Sport(String name) {
        this.name = name;
    }

    public static Sport of(String t){
       if( !values.containsKey(t)){
           Sport s = new Sport(t);
           values.put(t,s);
       }
        return values.get(t);
    }
}

class UseSport{
    public static String expressoinOpionion(Sport s){
        if( s.getName().equals("Cricket")) return "Kinda";
        if( s.getName().equals("Shinty")) return "Ouch...";
        throw new IllegalArgumentException("can't happen");

    }
    public static void main(String[] args) {

        Sport s1 = Sport.of("Cricket");
        Sport s2 = Sport.of("Cricket");
        Sport s3 = Sport.of("Shinty");

        System.out.println(s1 == s2);
        System.out.println(expressoinOpionion(s1));
        System.out.println(expressoinOpionion(s3));

    }
}
