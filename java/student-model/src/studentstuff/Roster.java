package studentstuff;

import javax.naming.CompositeName;
import java.sql.Array;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Stream;

class StudentGradeComparator implements Comparator<Student>{

    @Override
    public int compare(Student o1, Student o2) {
        return Double.compare(o1.getGrade(),o2.getGrade());
    }
}
public class Roster {

    List<Student> students;
    public Roster(String fileName){
        this.students = new ArrayList<>();
        students.add(new Student("Karl1", LocalDate.now().plusDays(-5),3.5f,new String[]{}));
        students.add(new Student("Karl1", LocalDate.now().plusDays(-5),1.5f,new String[]{}));
        students.add(new Student("Karl2", LocalDate.now().plusDays(-5),3.5f,new String[]{}));
        students.add(new Student("Karl3", LocalDate.now().plusDays(-4),2.5f,new String[]{}));
        students.add(new Student("Karl4", LocalDate.now().plusDays(-3),1.5f,new String[]{}));
        students.add(new Student("Karl5", LocalDate.now().plusDays(-2),3.5f,new String[]{}));
        students.add(new Student("Karl6", LocalDate.now().plusDays(-1),4.0f,new String[]{}));
        students.add(new Student("Karl7", LocalDate.now().plusDays(-0),2.5f,new String[]{}));
        students.add(new Student("Karl8", LocalDate.now().plusDays(+1),0.5f,new String[]{}));
    }

    public void print(boolean sorted){
        if(sorted){
            print(students.stream().sorted((a,b) -> Double.compare(a.getGrade(), b.getGrade())));
        }
        else {
            print(students.stream());
        }
    }
    public void print(Comparator<Student> c){
        print(students.stream().sorted(c));
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

        Student s1 = new Student("joe",LocalDate.now(),3.81f,new String[]{});
        Student s2 = new Student("fred",LocalDate.now().plusDays(-399),2.5f,new String[]{});

        List<Student> a = new ArrayList();
        a.add(s1);
        a.add(s2);
        Comparator<Student> c = (o1, o2) -> Double.compare(o1.getGrade(),o2.getGrade());
        //Comparator<Student> c = Comparator.comparingDouble(Student::getGrade);
        a.sort(new StudentGradeComparator());
        a.sort(c);

        Roster r = new Roster("roster.csv");
//        System.out.println("all");
//        r.print(false);
//        System.out.println("smart..");
//        r.printSmart(3.0);
//        System.out.println("3rd year");
//        r.printThirdYear();
//        System.out.println("sorted by grade");
//        r.print(true);
//        System.out.println("Sort my grade");
 //       r.print( (x,y) -> Double.compare(x.getGrade(),y.getGrade()));
          System.out.println("reverse Sort my grade");
          r.print( (x,y) -> Double.compare(y.getGrade(),x.getGrade()));

          System.out.println("Sort by Name");
          r.print( (x,y) -> CharSequence.compare(y.getName(),x.getName()) );

          System.out.println("Sort by Name, then by grade");
          r.print( (x,y) -> {
              final int compName = CharSequence.compare(x.getName(),y.getName());
              if(compName ==0)
                  return 0;
              return Double.compare(x.getGrade(),y.getGrade());
          } );

    }

}
