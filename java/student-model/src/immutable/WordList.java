package immutable;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public final class WordList {
    private final String name;
    private final List<String> words;

    WordList(String name, List<String> words){
        this.name = name;
        this.words = words;
    }
//    public static WordList of(String name, List<String> words){
    public static WordList of(String name,String ... words){
        return new WordList(name,List.of(words));
        //return new WordList(name, Arrays.asList(words)); // VIEW (not-immulatable)
        //return new WordList(name,List.copyOf(words));
      //  return new WordList(name, Collections.unmodifiableList(words));
    }
    public String getName(){
        return name;
    }
    public List<String> getWords(){
        return Collections.unmodifiableList(words);
    }
    @Override
    public String toString(){
        return "WordList: name="+name+", words = "+words;
    }

    public static void main(String[] args) {
      // List<String> words = new ArrayList<>();
      // words.add("the");
      // words.add("rain");
      // words.add("in");
      // words.add("spain");
//        WordList wl = new WordList("karl's", words);
        WordList wl = new WordList("karl's", List.of("the","rain","in","spain"));

        //words.add("oops..../11");
        System.out.println(wl);
    }
}
