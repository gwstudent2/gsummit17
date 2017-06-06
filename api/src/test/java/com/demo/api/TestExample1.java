// File: src/test/java/com/demo/api/TestExample1.java

import org.junit.Assert;
import org.junit.Test;
import java.util.concurrent.TimeUnit;

public class TestExample1 {

  @Test public void example1() {
try {
    Thread.sleep(5000);
} catch(InterruptedException ex) {
    Thread.currentThread().interrupt();
}

	Assert.assertEquals("Testing with Gradle is easy", "Testing with Gradle is easy");
  }
}
