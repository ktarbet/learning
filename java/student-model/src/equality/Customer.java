package equality;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Customer {
    private String name;
    private String address;
    private long creditLimit;

    public Customer(String name, String address, long creditLimit) {
        this.name = name;
        this.address = address;
        this.creditLimit = creditLimit;
    }

    @Override
    public boolean equals(Customer this, Object other){
        //if( other instanceof Customer otherC) // newer Java
        if( other instanceof Customer){
            Customer otherC = (Customer)other;
            return otherC.name.equals(this.name) && otherC.address.equals(this.address);
        }
        return false;
    }

    @Override
    public int hashCode(){
        return 1; //name.length();
    }

    public static void main(String[] args) {
        Customer c1 = new Customer("Fred","aqui, ", 1_000);
        Customer c2 = new Customer("Jim","ahí, ", 2_000);
        Customer c3 = new Customer("Fred","aqui, ", 4_000);

        System.out.println(c1.equals(c2)); // false
        System.out.println(c1.equals(c3)); // true
        List<Customer> lc = List.of(c1,c2);
        System.out.println( lc.contains(c3)); // true
        Set<Customer> sc = new HashSet<>();
        sc.add(c1);
        sc.add(c2);
        System.out.println(sc.contains(c3));
    }
}
