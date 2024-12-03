package lab05;

public class WithdrawThread extends Thread  {
	private BankAccount account;
    private double amount;

    public WithdrawThread(BankAccount account, double amount) {
        this.account = account;
        this.amount = amount;
    }

    @Override
    public void run() {
        account.withdraw(amount);
        try {
            Thread.sleep(1000); // Simulating time taken for transaction
        } catch (InterruptedException e) {
            System.out.println(e.getMessage());
        }
    }
}

