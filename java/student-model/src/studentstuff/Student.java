package studentstuff;

import java.security.InvalidParameterException;
import java.time.LocalDate;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.UUID;

public class Student {
    private String name;
    private String id;

    Set<String> Courses = new HashSet();
    private LocalDate enrollDate;

    private double overallGrade;

    public Student(String name, LocalDate enrollDate,
                   float overallGrade,String[] courses) {
        if( !isValid(name,enrollDate,overallGrade,courses))
        {
            throw new InvalidParameterException("");
        }
        this.name = name;
        setEnrollDate(enrollDate);
        this.id = String.valueOf(UUID.randomUUID());
        this.setCourses(courses);
        this.overallGrade=overallGrade;
    }

    public LocalDate getEnrollDate() {
        return enrollDate;
    }

    public void setEnrollDate(LocalDate enrollDate) {
        this.enrollDate = enrollDate;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String[] getCourses() {
        return Courses.toArray(new String[]{});
    }

    public void setCourses(String[] courses) {
        Courses.clear();
        Courses.addAll(List.of(courses));
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String toString(){
     return id+","+ name+", grade:"+getGrade()+","+enrollDate.toString();
    }

    public double getGrade() {
       return overallGrade;
    }

    @Override
    public int hashCode(){
        int c = this.name.hashCode()
                +this.enrollDate.hashCode()
                +this.getId().hashCode();
        return c;
    }

    @Override
    public boolean equals(Student this, Object o){
        if ( o instanceof Student){
            Student s = (Student) o;
            return s.id == this.id;
        }
        return false;
    }
    public static boolean isValid(String name, LocalDate enrollDate,
                                  double overallGrade,
                                  String[] courses){
        if( name == null || name.length()==0) {
            return false;
        }
        if(enrollDate == null ){
            return false;
        }
        if ( overallGrade <0 || overallGrade >4.0) {
            return false;
        }
        if( courses == null){
            return false;
        }

        return true;
    }
}
