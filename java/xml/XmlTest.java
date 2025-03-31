import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import java.io.File;

// /ratings/simple-rating/rating-points/point
public class XmlTest {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        try {
            File xmlFile = new File("C:/project/java/xml/sample.xml"); // Replace with your file name
            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
            Document doc = dbFactory.newDocumentBuilder().parse(xmlFile);

            // Normalize the document (optional, but good practice)
            doc.getDocumentElement().normalize();

            // Example: Get the office-id from the first rating-template element
            Element ratingTemplate = (Element) doc.getElementsByTagName("rating-template").item(0);
            String officeId = ratingTemplate.getAttribute("office-id");
            System.out.println("Office ID: " + officeId);

            // Example: Get the rating-spec-id from the first rating-spec element
            Element ratingSpec = (Element) doc.getElementsByTagName("rating-spec").item(0);
            String ratingSpecId = ratingSpec.getAttribute("rating-spec-id");
            System.out.println("Rating Spec ID: " + ratingSpecId);

            Element ratingPoint1 = (Element) doc.getElementsByTagName("rating-points").item(0);
            System.out.printf(ratingPoint1.toString());

        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}