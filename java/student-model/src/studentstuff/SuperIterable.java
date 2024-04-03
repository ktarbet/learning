package studentstuff;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.function.Predicate;
import java.util.function.Consumer;
import java.util.function.Function;
//interface Conusmer<E> {
//  void accept(E e);
//}

//interface Function<E, F> {
//  F apply(E e);
//}

public class SuperIterable<E> implements Iterable<E> {
    private Iterable<E> self;

    public SuperIterable(Iterable<E> self) {
        this.self = self;
    }

    public SuperIterable<E> filter(/*SuperIterable<E> this, */ Predicate<E> pred) {
        List<E> res = new ArrayList<>();
        for (E e : this.self) {
            if (pred.test(e)) {
                res.add(e);
            }
        }
        return new SuperIterable<>(res);
    }

    public <F> SuperIterable<F> map(Function<E, F> op) {
        List<F> res = new ArrayList<>();
        for (E e : this.self) {
            F f = op.apply(e);
            res.add(f);
        }
        return new SuperIterable<>(res);
    }

    public <F> SuperIterable<F> flatMap(Function<E, SuperIterable<F>> op) {
        List<F> res = new ArrayList<>();
        for (E e : this.self) {
            SuperIterable<F> manyF = op.apply(e);
            for(F f: manyF) {
                res.add(f);
            }
        }
        return new SuperIterable<>(res);
    }

    public void forEvery(Consumer<E> op) {
        for (E e : this.self) {
            op.accept(e);
        }
    }

    public Iterator<E> iterator() {
        return self.iterator();
    }
}
