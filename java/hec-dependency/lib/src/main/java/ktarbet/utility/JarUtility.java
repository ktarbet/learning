package ktarbet.utility;

import java.io.IOException;
import java.util.List;
import java.util.jar.JarEntry;
import java.util.jar.JarFile;
import java.util.stream.Collectors;
import java.util.zip.ZipEntry;

public class JarUtility {

    /**
     * gets class names, including package prefix from a jar
     *
     * @param jarFilename name of jar file
     * @return list of class names
     * @throws IOException
     */
    public static List<String> getClassNames(String jarFilename) throws IOException {
        try (JarFile jarFile = new JarFile(jarFilename)) {
            return jarFile.stream()
                    .map(ZipEntry::getName)
                    .filter(name -> name.endsWith(".class"))
                    .map(name -> name.replaceFirst("\\.class$", ""))
                    .map(name -> name.replace('/', '.'))
                    .sorted()
                    .collect(Collectors.toList());
        }
    }

}
