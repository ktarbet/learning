package hec.dependency;

import hec.dependency.JDeps.PackageDependency;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * A program to analyze dependencies in different HEC products.
 * It uses the JDK tool 'jdeps' to mine dependency information.
 * https://docs.oracle.com/en/java/javase/11/tools/jdeps.html
 *
 * Goal:
 *  1. Generate a table of dependencies on specific packages (e.g., from a monolith)
 *     for a given application JAR.
 */
public class Main {

    public static void main(String[] args) throws IOException {
        if (args.length < 3) {
            System.out.println("Usage: reference.jar <classpath> file1.jar <filter> ");
            System.out.println("\nWhere:");
            System.out.println("  <classpath>  - the classpath for the dependencies of the JAR being analyzed (e.g., 'libs/*').");
            System.out.println("  file1.jar  - jar to study for dependencies.");
            System.out.println("  filter - optional filter to limit dependencies ");
            System.out.println("example: ");
            System.out.println(" hec-monolith-7.0.4.jar .\\*;.\\ext\\* dssgui-4.0.9.jar   hec-monolith");
            System.out.println("");
            System.out.println(" in the example above hec-monolith-7.0.4.csv will be created/used for the results");

            return;
        }

        String refJar = args[0];
        String classPath = args[1];
        String jarToAnalyze = args[2];
        String filter = args.length>3 ? args[3] : "";

        DependencyHunter h = new DependencyHunter(refJar);
        h.addReferences(classPath, jarToAnalyze, filter);
        h.saveAsCsv("c:\\tmp\\out.csv");

    }
}

