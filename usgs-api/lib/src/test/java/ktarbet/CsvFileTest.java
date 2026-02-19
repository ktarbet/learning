package ktarbet;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeAll;

import java.nio.file.Path;

import static org.junit.jupiter.api.Assertions.*;

class CsvFileTest {

    static CsvFile csv;

    @BeforeAll
    static void loadCsv() throws Exception {
        Path csvPath = Path.of(CsvFileTest.class.getResource("/monitoring-locations.csv").toURI());
        csv = new CsvFile(csvPath);
    }

    @Test
    void parseLine_handlesQuotedCommas() throws Exception {
        assertEquals(42, csv.getColumnCount());
        assertEquals("monitoring_location_name", csv.getColumnNames()[6]);

        // row index 2 (third data row) has a quoted name with a comma
        assertEquals("COLORADO RIVER AT NEEDLES, CA",
                csv.get(2, "monitoring_location_name"));
        assertEquals("USGS-09423500", csv.get(2, "id"));
    }

    @Test
    void parseLine_handlesUnquotedFields() throws Exception {
        // first data row - no quotes
        assertEquals("USGS-09423350", csv.get(0, "id"));
        assertEquals("CARUTHERS C NR IVANPAH CA",
                csv.get(0, "monitoring_location_name"));
        assertEquals("U.S. Geological Survey", csv.get(0, "agency_name"));
    }

    @Test
    void rowCount() throws Exception {
        assertTrue(csv.getRowCount() > 100, "Expected many rows in monitoring-locations.csv");
    }

    @Test
    void unknownColumnThrows() throws Exception {

        assertThrows(IllegalArgumentException.class,
                () -> csv.get(0, "bogus_column"));
    }

    @Test
    void parseLine_handlesEmbeddedDoubleQuotes() throws Exception {
        // Construct a tiny CSV in a temp file with embedded double quotes
        java.nio.file.Path tmp = java.nio.file.Files.createTempFile("test", ".csv");
        java.nio.file.Files.writeString(tmp, "name,desc\n\"Alice\",\"She said \"\"hello\"\"\"\n");

        CsvFile csv = new CsvFile(tmp);
        assertEquals("Alice", csv.get(0, "name"));
        assertEquals("She said \"hello\"", csv.get(0, "desc"));

        java.nio.file.Files.delete(tmp);
    }
}
