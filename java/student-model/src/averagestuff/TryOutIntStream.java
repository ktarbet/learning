package averagestuff;

import java.util.function.IntBinaryOperator;
import java.util.function.IntUnaryOperator;
import java.util.stream.IntStream;

public class TryOutIntStream {
    public static void main(String[] args) {


        Sum1();

    }

    private static void Sum1() {
        IntUnaryOperator op = operand -> operand+1;
        IntBinaryOperator bo = (x,y) -> x+y;

        var answer = IntStream.iterate(1,op)
                .parallel()
                .limit(10)
                .reduce(0 , bo);

        System.out.println(answer);

        answer = IntStream.iterate(1,a -> a+1)
               .limit(10)
               .reduce(0 , (x,y) -> x+y);
        System.out.println(answer);
    }
}
