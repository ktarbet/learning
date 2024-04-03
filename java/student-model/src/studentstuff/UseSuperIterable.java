package studentstuff;

import java.security.spec.RSAOtherPrimeInfo;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.function.Function;

public class UseSuperIterable {

    public static List<Student> getStudents() {
        List<Student> students = new ArrayList<>();
        students.add(new Student("Karl1", LocalDate.now().plusDays(-5), 3.5f, new String[]{"Algebra"}));
        students.add(new Student("Karl1", LocalDate.now().plusDays(-5), 1.5f, new String[]{"bit-wise operations"}));
        students.add(new Student("Karl2", LocalDate.now().plusDays(-5), 3.5f, new String[]{"Music Theory"}));
        students.add(new Student("Karl3", LocalDate.now().plusDays(-4), 2.5f, new String[]{"Music Theory"}));
        students.add(new Student("Karl4", LocalDate.now().plusDays(-3), 1.5f, new String[]{}));
        students.add(new Student("Karl5", LocalDate.now().plusDays(-2), 3.5f, new String[]{}));
        students.add(new Student("Karl6", LocalDate.now().plusDays(-1), 4.0f, new String[]{"Celestial Mechanics"}));
        students.add(new Student("Karl7", LocalDate.now().plusDays(-0), 2.5f, new String[]{}));
        students.add(new Student("Karl8", LocalDate.now().plusDays(+1), 0.5f, new String[]{"Fishing","camping","ski mechanics"}));

        return students;
    }

    public static void main(String[] args) {


        SuperIterable<Student> sis = new SuperIterable<>(getStudents());

        System.out.println("------All Students------------");
        sis.forEach(s-> System.out.println(s));

        System.out.println("------All Students and grades------------");
        sis = new SuperIterable<>(getStudents());
        sis.forEach(s-> System.out.println("Student "+s.getName()+" has grade "+s.getGrade()));


        System.out.println("------Smart Students and grades------------");
        sis = new SuperIterable<>(getStudents());
        sis.filter(s-> s.getGrade() >3.4999)
                .forEach(s-> System.out.println("Student "+s.getName()+" has grade "+s.getGrade()));

        System.out.println("------Smart Students but un-enthusiastic grades------------");
        sis = new SuperIterable<>(getStudents());
        sis.filter(s-> s.getGrade() >3)
                .filter(s -> s.getCourses().length <2)
                .forEach(s-> System.out.println("Student "+s.getName()+" has grade "+s.getGrade()+"smart but unenthusiastic, students"));

        System.out.println("------print grades------------");
        sis = new SuperIterable<>(getStudents());
        sis.forEach(s-> System.out.println(s.getGrade()));

        System.out.println("------print all courses------------");

        //Set<String> allCourses = new HashSet<>();
        sis = new SuperIterable<>(getStudents());
        sis.flatMap(s -> new SuperIterable<>(List.of(s.getCourses())))
                //.forEach(c -> allCourses.add(c));
                .forEach(c -> System.out.println(c));

        sis = new SuperIterable<>(getStudents());
        sis

              .filter(s -> s.getGrade()>3.3)
                .flatMap(c -> new SuperIterable<>( List.of(c.getCourses())))
                .forEach(c -> System.out.println("A smart student is taking "+c+" course"));


        sis = new SuperIterable<>(getStudents());
        sis

                .filter(s -> s.getGrade()>3.3)
                .flatMap(
                        (Student s) ->{
                         return new SuperIterable<>(List.of(s.getCourses())).map(
                                 c -> "Student "+s.getName()+" takes "+ c);
                        })

                .forEach(c -> System.out.println("A smart student is taking "+c+" course"));


    }
}
