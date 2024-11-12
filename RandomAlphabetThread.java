package synchronization;

import java.util.concurrent.TimeUnit;

public class RandomAlphabetThread extends Thread {
	public void run() {
        // Loop to print 26 alphabets A-Z
        for (int i = 0; i < 26; i++) {
            // Generate a random number between 0 and 25
            int randomDelay = (int) (Math.random() * 500);  // Random delay up to 500 ms
            char alphabet = (char) ('A' + i); // Convert index to alphabet A-Z

            try {
                // Print the alphabet
                System.out.print(alphabet + " ");
                // Sleep for a random time (between 0 and 500 ms)
                TimeUnit.MILLISECONDS.sleep(randomDelay);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println(); // Move to the next line after printing all alphabets
    }

    public static void main(String[] args) {
        // Create and start the thread
        RandomAlphabetThread thread = new RandomAlphabetThread();
        thread.start();

        // Optional: Main thread waits for the alphabet thread to finish
        try {
            thread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

