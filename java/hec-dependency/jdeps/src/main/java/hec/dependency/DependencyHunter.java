package hec.dependency;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.List;

import tech.tablesaw.api.IntColumn;
import tech.tablesaw.api.Row;
import tech.tablesaw.api.StringColumn;
import tech.tablesaw.api.Table;
import tech.tablesaw.columns.Column;
import tech.tablesaw.selection.Selection;

import ktarbet.utility.JarUtility;

public class DependencyHunter {


    private static final String CLASSNAME = "ClassName";
    private static final String JARS = "Jars";
    Table dataTable;
    /**
     * DependencyHunter looks at the referenceJar and finds incoming references
     * @param referenceJar
     */
    public DependencyHunter(String referenceJar) throws IOException {

        String refJarName = Paths.get(referenceJar).getFileName().toString();
        dataTable = Table.create(refJarName);
        dataTable.addColumns(StringColumn.create(CLASSNAME));
        dataTable.addColumns(StringColumn.create(JARS));

        var classNames = JarUtility.getClassNames(referenceJar);
        for(var c : classNames) {
             Row r = dataTable.appendRow();
             r.setString(CLASSNAME, c);
             r.setString(JARS, refJarName);
        }
    }

    public void saveAsCsv(String csvFilename) {
        dataTable.write().csv(csvFilename);
    }

    protected void addReferences(String classPath, String jarToAnalyze, String filter){
        String jarToAnalyzeName = Paths.get(jarToAnalyze).getFileName().toString();
        dataTable.addColumns(IntColumn.create(jarToAnalyzeName));
        System.out.printf("Adding references for: '%s'%n", jarToAnalyze);
        System.out.printf("Using Classpath: '%s'%n%n", classPath);

        try {
            JDeps jdepsAnalyzer = new JDeps(classPath, jarToAnalyze);
            List<JDeps.PackageDependency> dependencies = jdepsAnalyzer.run();

            if (dependencies.isEmpty()) {
                System.out.println("No package dependencies were found.");
                return;
            }

            List<JDeps.PackageDependency> filtered = dependencies.stream()
                    .filter(d -> filter.isEmpty() || d.location().contains(filter))
                    .toList();

            for (JDeps.PackageDependency dep : filtered) {

                Selection selection = dataTable.stringColumn(CLASSNAME).isEqualTo(dep.dependencyPackage());

                if (selection.isEmpty()) {
                    System.err.printf("Error: can't find %s",dep.dependencyPackage());
                    Row r =dataTable.appendRow();
                    r.setString(CLASSNAME,dep.dependencyPackage());
                    r.setString(JARS, dep.location());
                    r.setInt(jarToAnalyzeName, 1);
                }
                else{
                    int rowIndex = selection.get(0);
                    IntColumn c = dataTable.intColumn(jarToAnalyzeName);
                    int currentVal = c.isMissing(rowIndex) ? 0 : c.get(rowIndex);
                    c.set(rowIndex,currentVal+1);
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
