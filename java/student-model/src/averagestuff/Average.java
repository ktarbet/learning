package averagestuff;

import java.util.Optional;
import java.util.concurrent.ThreadLocalRandom;
import java.util.stream.DoubleStream;

public class Average {
    private final double sum;
    private final long count;
    private Average(double sum,long count){
        this.sum =sum;
        this.count = count;
    }

    public static Average of(double sum, long count){
        return new Average(sum,count);
    }

    public Average merge(Average this, Average a)
    {
        return new Average(
                this.sum+ a.sum
                ,this.count + a.count);
    }

    public Optional<Double> get(){
        if(count >0){
            return Optional.of(sum/count);
        }
        else{
            return Optional.empty();
        }
    }

    public static void main(String[] args) {

        DoubleStream.generate(() ->
                ThreadLocalRandom.current().nextDouble(-1,1))
                .limit(1000)
                .mapToObj(x -> new Average(x,1))
                .reduce(new Average(0,0),(a,b) -> a.merge(b))
                .get()
                .map(v-> "The average is "+v)
                .ifPresentOrElse(s -> System.out.println(s),
                        () -> System.out.println("oops, no data.."));

    }
}
