package lab06SCD;

public class Main {
	public static void main(String[] args) {
        // Initialize the bank account with a balance of 50,000
        BankAccount account = new BankAccount(50000);

        // Create two threads for user A and user B
        UserThread userA = new UserThread(account, 45000, "User A");
        UserThread userB = new UserThread(account, 20000, "User B");

        // Start both threads
        userA.start();
        userB.start();
        
        try {
            // Wait for both threads to finish
            userA.join();
            userB.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Final balance after both withdrawals (if successful)
        System.out.println("Final account balance: " + account.getBalance());
    }
}

