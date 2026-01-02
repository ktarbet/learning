import java.util.ArrayList;
import java.util.List;

public class Generics {

    public abstract static class TimeSeriesBase {
        private int count;

        public int getCount() {
            return count;
        }
    }
    public static class DailyTimeSeries extends TimeSeriesBase {
    }
    public static class MonthlyTimeSeries extends TimeSeriesBase {
    }

    public static class TimeSeries<E extends TimeSeriesBase> {

    }

    public static void main(String[] args) {

        restrictGenericToTimeSeries();
        hackTypeErasure();
    }

    private static void restrictGenericToTimeSeries() {

            TimeSeries<DailyTimeSeries> ts = new TimeSeries<>();

    }

    private static void hackTypeErasure() {
        List<String> items = new ArrayList<>();

        AddItem(items, "abc");
        AddItem(items, "def");

        List x = items;
        AddItemHacked(x,12);

        System.out.println(x);
    }

    private static void AddItem(List<String> items, String s) {
        items.add(s);
    }

    private static void AddItemHacked(List items, int i) {
        items.add(i);
    }

}