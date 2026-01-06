package hec.dependency;

import picocli.CommandLine;
import picocli.CommandLine.Command;
import picocli.CommandLine.Option;
import picocli.CommandLine.Parameters;

import java.io.File;
import java.io.IOException;
import java.util.concurrent.Callable;

/**
 * A program to analyze dependencies, and comapare across different java
 * applications.
 * It uses the JDK tool 'jdeps' to mine dependency information.
 * https://docs.oracle.com/en/java/javase/11/tools/jdeps.html
 *
 * Goal:
 *  1. Generate a table of dependencies on specific packages (e.g., from a monolith)
 *     for a given application JAR.
 */
@Command(name = "dependency-hunter", mixinStandardHelpOptions = true,
        description = "Analyzes JAR dependencies using jdeps.")
public class Main implements Callable<Integer> {

    @Option(names = {"-c", "--column"}, required = true, description = "The column to add to the output file.")
    private String resultsColumn;

    @Option(names = {"-r", "--reference-jar"}, required = true, description = "The reference JAR used to generate a list of class names.")
    private File refJar;

    @Option(names = {"-f", "--filter"}, required = true, description = "Filter to limit output (typically the name of the reference jar).")
    private String filter;

    @Option(names = {"-cp", "--classpath"}, required = true, description = "The classpath for the dependencies of the JAR(s) being analyzed (e.g., 'libs/*').")
    private String classPath;
    
    @Option(names = {"-o", "--output-file"}, required = true, description = "The path to the output CSV file.")
    private File outputFile;

    @Parameters(description = "One or more JAR files to study for dependencies.", arity = "1..*")
    private String[] jars;

    public static void main(String[] args) {
        int exitCode = new CommandLine(new Main()).execute(args);
        System.exit(exitCode);
    }

    @Override
    public Integer call() throws IOException {
        DependencyHunter h = new DependencyHunter(refJar.getPath());
        h.addReferences(classPath, resultsColumn, jars, filter);
        h.saveAsCsv(outputFile.getPath());

        System.out.println("Dependency analysis complete. Output saved to " + outputFile.getPath());
        return 0;
    }
}
