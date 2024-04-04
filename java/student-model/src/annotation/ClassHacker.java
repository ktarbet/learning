package annotation;

import java.io.FileReader;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.Properties;

public class ClassHacker {
    public static void main(String[] args) throws Throwable {
        Properties props = new Properties();
        props.load(new FileReader("Hacker.properties"));
        String className = props.getProperty("class");
        System.out.println("Classname to be hacked is " + className);
        Class cl = Class.forName(className);

        Constructor cons = cl.getConstructor();
        Object obj = cons.newInstance();
        System.out.println(obj);

        //var fields = cl.getFields();
        var fields = cl.getDeclaredFields();
        for (Field f : fields){
            f.setAccessible(true);
            Hackable annot = f.getAnnotation(Hackable.class);
            if (annot != null) {
                System.out.println("@Hackable field: "+f.getName()+" value="+f.get(obj)+"  name= "+annot.name());
                System.out.println("setting field... ");
                f.set(obj,annot.name());
                System.out.println("@Hackable field: "+f.getName()+" value="+f.get(obj)+"  name= "+annot.name());

            }
            else{
                System.out.print("non-hackable field: "+f.getName()+" value:"+f.get(obj));
            }
        }

        Method[] methods = cl.getDeclaredMethods();
//    Method[] methods = cl.getMethods();
        for (Method m : methods) {
            System.out.println("> " + m);
            Hackable annot = m.getAnnotation(Hackable.class);
            if (annot != null) {
                System.out.println("****** Hackable found!!!");
                System.out.println("****** name is " + annot.name());
                m.setAccessible(true);
                /*var res = */m.invoke(obj);
            }
        }
    }
}
