package ktarbet;

import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class CsvFile {

    private final String[] columnNames;
    private final Map<String, Integer> columnIndex;
    private final List<String[]> rows;

    public CsvFile(String filename) throws IOException {
        this(Path.of(filename));
    }

    public CsvFile(Path path) throws IOException {
        rows = new ArrayList<>();
        columnIndex = new LinkedHashMap<>();

        try (BufferedReader reader = Files.newBufferedReader(path)) {
            String line = reader.readLine();
            if (line == null) {
                throw new IOException("Empty CSV file");
            }
            columnNames = parseLine(line);
            for (int i = 0; i < columnNames.length; i++) {
                columnIndex.put(columnNames[i], i);
            }

            while ((line = reader.readLine()) != null) {
                rows.add(parseLine(line));
            }
        }
    }

    private String[] parseLine(String line) {
        List<String> fields = new ArrayList<>();
        int i = 0;
        int len = line.length();

        while (i <= len) {
            if (i == len) {
                // trailing comma produces empty final field
                fields.add("");
                break;
            }
            if (line.charAt(i) == '"') {
                // quoted field
                StringBuilder sb = new StringBuilder();
                i++; // skip opening quote
                while (i < len) {
                    char c = line.charAt(i);
                    if (c == '"') {
                        if (i + 1 < len && line.charAt(i + 1) == '"') {
                            sb.append('"');
                            i += 2;
                        } else {
                            i++; // skip closing quote
                            break;
                        }
                    } else {
                        sb.append(c);
                        i++;
                    }
                }
                fields.add(sb.toString());
                // skip comma after closing quote
                if (i < len && line.charAt(i) == ',') {
                    i++;
                }
            } else {
                // unquoted field
                int comma = line.indexOf(',', i);
                if (comma == -1) {
                    fields.add(line.substring(i));
                    break;
                } else {
                    fields.add(line.substring(i, comma));
                    i = comma + 1;
                }
            }
        }
        return fields.toArray(new String[0]);
    }

    public String get(int row, String column) {
        Integer col = columnIndex.get(column);
        if (col == null) {
            throw new IllegalArgumentException("Unknown column: " + column);
        }
        String[] r = rows.get(row);
        return col < r.length ? r[col] : "";
    }

    public String[] getRow(int row) {
        return rows.get(row);
    }

    public String[] getColumnNames() {
        return columnNames.clone();
    }

    public int getRowCount() {
        return rows.size();
    }

    public int getColumnCount() {
        return columnNames.length;
    }
}
