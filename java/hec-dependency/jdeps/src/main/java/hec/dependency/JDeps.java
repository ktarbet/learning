package hec.dependency;

import ktarbet.utility.SystemUtility;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * A Java wrapper for the command-line jdeps program.
 * This class simplifies the execution of the jdeps tool by encapsulating
 * the command-line arguments, process execution, and output parsing.
 */
public class JDeps {

    /**
     * Represents a dependency between two packages.
     *
     * @param dependentItem  The package/class that has a dependency.
     * @param dependencyItem The package/class that is being depended on.
     * @param location          The location of the dependency, such as a JAR file or module name.
     */
    public record PackageDependency(
            String dependentItem,
            String dependencyItem,
            String location
    ) {}

    private final String classPath;
    private final String[] jarPath;

    /**
     * Constructs a JDeps wrapper with the specified classpath and JAR file.
     *
     * @param classPath The classpath to be used by jdeps.
     * @param jarPath   The path to the .jar file to be analyzed.
     */
    public JDeps(String classPath, String[] jarPath) {
        if (classPath == null || classPath.trim().isEmpty()) {
            throw new IllegalArgumentException("Class path cannot be null or empty.");
        }
        if (jarPath == null || jarPath.length == 0) {
            throw new IllegalArgumentException("JAR path cannot be null or empty.");
        }
        this.classPath = classPath;
        this.jarPath = jarPath;
    }

    /**
     * Executes the jdeps command and parses its output into a list of package dependencies.
     * The command executed is: jdeps --multi-release 11 -verbose:package -cp [classPath] [jarPath]
     *
     * @return A List of {@link PackageDependency} objects representing the parsed output.
     * @throws IOException          If an I/O error occurs during the process execution or if the jdeps process exits with an error.
     * @throws InterruptedException If the execution thread is interrupted while waiting for the process to complete.
     */
    public List<PackageDependency> run() throws IOException, InterruptedException {
        List<String> command = new ArrayList<>();
        command.add("jdeps");
        command.add("--multi-release");
        command.add("11");
        command.add("-verbose:class");
        command.add("-cp");
        command.add(classPath);
        command.addAll(List.of(jarPath));

        List<PackageDependency> dependencies = new ArrayList<>();

        List<String> lines = SystemUtility.runCommand(command);
         for (String line: lines){

             /* example output.
Warning: split package: org.xml.sax.ext jrt:/java.xml .\xml-apis-1.4.01.jar
Warning: split package: org.xml.sax.helpers jrt:/java.xml .\xml-apis-1.4.01.jar
dssgui-4.0.9.jar -> .\context-specific-help-1.1.0.jar
dssgui-4.0.9.jar -> .\flogger-0.7.4.jar
...
   hec.dssgui.AbstractGridInfoTab                     -> hec.heclib.grid.GridData                           hec-monolith-7.0.4.jar
   hec.dssgui.AbstractGridInfoTab                     -> java.awt.LayoutManager                             java.desktop
   hec.dssgui.AbstractGridInfoTab                     -> java.awt.event.MouseEvent                          java.desktop
              */
                if (line.startsWith("Warning:") || !line.startsWith(" ")) {
                    continue;
                }
                String[] parts = line.trim().split("->");
                if (parts.length > 1) {
                    String dependent = parts[0].trim();
                    String dependencyPart = parts[1].trim();

                    int idx = dependencyPart.indexOf(" ");// find first space
                    if (idx >0) {
                        String dependency = dependencyPart.substring(0,idx);
                        String location = dependencyPart.substring(idx).trim();
                        dependencies.add(new PackageDependency(dependent, dependency, location));
                    }
                }
        }

        return dependencies;
    }
}
