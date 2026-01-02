package hec.dependency;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Utility {



    public static List<String> runCommand(List<String> args) throws IOException {

        ProcessBuilder processBuilder = new ProcessBuilder(args);
        processBuilder.redirectErrorStream(true);
        Process process = processBuilder.start();

        List<String> rval = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {

            rval.add(reader.readLine());
        }
        return rval;
    }
}