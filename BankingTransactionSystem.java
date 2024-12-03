package lab05;

public class BankingTransactionSystem {
	public static void main(String[] args) {
        BankAccount account = new BankAccount(1000.0); // Initial balance of 1000

        // Creating multiple deposit and withdraw threads
        Thread deposit1 = new DepositThread(account, 200.0);
        Thread deposit2 = new DepositThread(account, 500.0);
        Thread withdraw1 = new WithdrawThread(account, 300.0);
        Thread withdraw2 = new WithdrawThread(account, 400.0);

        // Starting threads
        deposit1.start();
        deposit2.start();
        withdraw1.start();
        withdraw2.start();

        try {
            // Waiting for all threads to finish
            deposit1.join();
            deposit2.join();
            withdraw1.join();
            withdraw2.join();
        } catch (InterruptedException e) {
            System.out.println("Main thread interrupted: " + e.getMessage());
        }

        System.out.println("Final Account Balance: " + account.getBalance());
    }
}

