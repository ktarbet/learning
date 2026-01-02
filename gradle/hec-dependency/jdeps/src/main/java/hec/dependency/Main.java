package hec.dependency;

import hec.dependency.JDeps.PackageDependency;

import java.io.IOException;
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

    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage:  <classpath> file1.jar file2.jar ...");
            System.out.println("\nWhere:");
            System.out.println("  <classpath>       The classpath for the dependencies of the JAR being analyzed (e.g., 'libs/*').");
            System.out.println("  list of jars to study for dependencies.");

            return;
        }

        String classPath = args[0];
        String jarToAnalyze = args[1];

        System.out.printf("Analyzing dependencies for: '%s'%n", jarToAnalyze);
        System.out.printf("Using Classpath: '%s'%n%n", classPath);

        try {
            JDeps jdepsAnalyzer = new JDeps(classPath, jarToAnalyze);
            List<PackageDependency> dependencies = jdepsAnalyzer.run();

            if (dependencies.isEmpty()) {
                System.out.println("No package dependencies were found.");
                return;
            }


            List<PackageDependency> hecDependencies = dependencies.stream()
                    //.filter(d -> filter.isEmpty() || d.location().equals(filter))
                    .toList();

            if (hecDependencies.isEmpty()) {
                System.out.printf("No dependencies found ");
            } else {
                // Print a formatted table header
                System.out.printf("%-50s -> %-50s %s%n", "Dependent Package", "Target Dependency", "Location");
                System.out.println("-".repeat(120));

                for (PackageDependency dep : hecDependencies) {
                    System.out.printf("%-50s -> %-50s %s%n",
                            dep.dependentPackage(),
                            dep.dependencyPackage(),
                            dep.location());
                }
            }

        } catch (IOException e) {
            System.err.println("\n[ERROR] An I/O error occurred while running jdeps: " + e.getMessage());
            System.err.println("Please ensure 'jdeps' is installed and available in your system's PATH.");
        } catch (InterruptedException e) {
            System.err.println("\n[ERROR] The dependency analysis process was interrupted.");
            Thread.currentThread().interrupt(); // Restore the interrupted status
        }
    }
}

