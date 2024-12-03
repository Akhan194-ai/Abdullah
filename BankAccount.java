package lab05;

public class BankAccount {
	   private double balance;

	    public BankAccount(double initialBalance) {
	        this.balance = initialBalance;
	    }

	    // Synchronized method to ensure only one thread can withdraw at a time
	    public synchronized void withdraw(double amount) {
	        if (amount > balance) {
	            System.out.println(Thread.currentThread().getName() + ": Insufficient funds for withdrawal of " + amount);
	        } else {
	            System.out.println(Thread.currentThread().getName() + ": Withdrawing " + amount);
	            balance -= amount;
	            System.out.println(Thread.currentThread().getName() + ": New Balance: " + balance);
	        }
	    }

	    // Synchronized method to ensure only one thread can deposit at a time
	    public synchronized void deposit(double amount) {
	        System.out.println(Thread.currentThread().getName() + ": Depositing " + amount);
	        balance += amount;
	        System.out.println(Thread.currentThread().getName() + ": New Balance: " + balance);
	    }

	    public double getBalance() {
	        return balance;
	    }
	}

