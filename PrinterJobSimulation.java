package lab06SCD;

public class PrinterJobSimulation {
    public static void main(String[] args) {
        // Create a printer with an initial amount of pages (e.g., 10 pages)
        Printer printer = new Printer(10);

        // Create and start the RemainingPagesThread (for adding pages)
        RemainingPagesThread remainingPagesThread = new RemainingPagesThread(printer);
        remainingPagesThread.start();

        // Create and start PrintJobThreads with different print jobs (e.g., printing 15 pages)
        PrintJobThread printJobThread1 = new PrintJobThread(printer, 15);
        printJobThread1.start();

        PrintJobThread printJobThread2 = new PrintJobThread(printer, 5);
        printJobThread2.start();

        // Main thread waits for all threads to finish
        try {
            printJobThread1.join();
            printJobThread2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Once the print jobs are done, stop the RemainingPagesThread gracefully
        remainingPagesThread.stopThread();
    }
}