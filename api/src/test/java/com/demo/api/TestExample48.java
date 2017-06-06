// File: src/test/java/com/demo/api/TestExample48.java

import org.junit.Assert;
import org.junit.Test;
import java.util.concurrent.TimeUnit;

public class TestExample48 {

  @Test public void example48() {
try {
    Thread.sleep(5000);
} catch(InterruptedException ex) {
    Thread.currentThread().interrupt();
}

	Assert.assertEquals("Testing with Gradle is easy", "Testing with Gradle is easy");
  }
}
