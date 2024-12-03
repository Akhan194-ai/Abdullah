package lab05;

public class DepositThread extends Thread {
	private BankAccount account;
    private double amount;

    public DepositThread(BankAccount account, double amount) {
        this.account = account;
        this.amount = amount;
    }

    @Override
    public void run() {
        account.deposit(amount);
        try {
            Thread.sleep(1000); // Simulating time taken for transaction
        } catch (InterruptedException e) {
            System.out.println(e.getMessage());
        }
    }
}

