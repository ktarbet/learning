package immutable;

import java.util.ArrayList;
import java.util.List;

public class BadWordList{ // can't extend if base is finale extends WordList{
    private List<String> myWords = new ArrayList<>();
    public BadWordList(){
        //super("Dodgy",null);
    }

   //

    @Override
    public String toString(){
        return "";
    }
}
