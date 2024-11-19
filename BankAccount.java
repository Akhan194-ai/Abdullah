package lab06SCD;

public class BankAccount {
	private double balance;

	    public BankAccount(double initialBalance) {
	        this.balance = initialBalance;
	    }

	    // Synchronized method to withdraw money from the account
	    public synchronized boolean withdraw(double amount) {
	        if (amount <= balance) {
	            System.out.println(Thread.currentThread().getName() + " is withdrawing: " + amount);
	            balance -= amount;
	            System.out.println(Thread.currentThread().getName() + " completed the withdrawal. New balance: " + balance);
	            return true;
	        } else {
	            System.out.println(Thread.currentThread().getName() + " attempted to withdraw " + amount + " but insufficient funds. Current balance: " + balance);
	            return false;
	        }
	    }

	    public double getBalance() {
	        return balance;
	    }
	}

	class UserThread extends Thread {
	    private BankAccount account;
	    private double amount;

	    public UserThread(BankAccount account, double amount, String name) {
	        this.account = account;
	        this.amount = amount;
	        this.setName(name);  // Set the name of the thread (user)
	    }

	    @Override
	    public void run() {
	        if (!account.withdraw(amount)) {
	            System.out.println(getName() + " could not withdraw " + amount);
	        }
	    }
	}

