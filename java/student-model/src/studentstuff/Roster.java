package studentstuff;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Stream;

public class Roster {

    List<Student> students;
    public Roster(String fileName){
        this.students = new ArrayList<>();
        students.add(new Student("Karl2", LocalDate.now().plusDays(-5),"id123",3.5f,new String[]{}));
        students.add(new Student("Karl3", LocalDate.now().plusDays(-4),"id124",2.5f,new String[]{}));
        students.add(new Student("Karl4", LocalDate.now().plusDays(-3),"id125",1.5f,new String[]{}));
        students.add(new Student("Karl5", LocalDate.now().plusDays(-2),"id126",3.5f,new String[]{}));
        students.add(new Student("Karl6", LocalDate.now().plusDays(-1),"id127",4.0f,new String[]{}));
        students.add(new Student("Karl7", LocalDate.now().plusDays(-0),"id128",2.5f,new String[]{}));
        students.add(new Student("Karl8", LocalDate.now().plusDays(+1),"id129",0.5f,new String[]{}));
    }

    public void print(boolean sorted){
        if(sorted){
            print(students.stream().sorted((a,b) -> Double.compare(a.getGrade(), b.getGrade())));
        }
        else {
            print(students.stream());
        }
    }
    public void printSmart(double threshold)
    {
        print(filter(s -> s.getGrade() >= threshold));
    }
    public void printThirdYear(){
      print(filter(s -> s.getEnrollDate().getYear() == LocalDate.now().getYear()+2)); // 3rd year
    }
    private void print(Stream<Student> ss){
        ss.forEach(s -> System.out.println(s));
    }

    private Stream<Student> filter(Predicate<Student> filter){
     return students.stream().filter(filter);
    }

    public static void main(String[] args){
        Roster r = new Roster("roster.csv");
        System.out.println("all");
        r.print(false);
        System.out.println("smart..");
        r.printSmart(3.0);
        System.out.println("3rd year");
        r.printThirdYear();
        System.out.println("sorted by grade");
        r.print(true);

    }

}
