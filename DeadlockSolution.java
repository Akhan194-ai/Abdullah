package lab08;

public class DeadlockSolution {
	 private final Object lock1 = new Object();
	    private final Object lock2 = new Object();
	    private final Object lock3 = new Object();

	    // Thread 1 acquires lock1, lock2, and lock3 in the same order
	    class Thread1 extends Thread {
	        public void run() {
	            synchronized (lock1) {
	                System.out.println("Thread1 acquired lock1");
	                synchronized (lock2) {
	                    System.out.println("Thread1 acquired lock2");
	                    synchronized (lock3) {
	                        System.out.println("Thread1 acquired lock3");
	                    }
	                }
	            }
	        }
	    }

	    // Thread 2 acquires lock1, lock2, and lock3 in the same order
	    class Thread2 extends Thread {
	        public void run() {
	            synchronized (lock1) {
	                System.out.println("Thread2 acquired lock1");
	                synchronized (lock2) {
	                    System.out.println("Thread2 acquired lock2");
	                    synchronized (lock3) {
	                        System.out.println("Thread2 acquired lock3");
	                    }
	                }
	            }
	        }
	    }

	    // Thread 3 acquires lock1, lock2, and lock3 in the same order
	    class Thread3 extends Thread {
	        public void run() {
	            synchronized (lock1) {
	                System.out.println("Thread3 acquired lock1");
	                synchronized (lock2) {
	                    System.out.println("Thread3 acquired lock2");
	                    synchronized (lock3) {
	                        System.out.println("Thread3 acquired lock3");
	                    }
	                }
	            }
	        }
	    }

	    // Main method to start the threads
	    public static void main(String[] args) {
	        DeadlockSolution example = new DeadlockSolution();
	        Thread1 t1 = example.new Thread1();
	        Thread2 t2 = example.new Thread2();
	        Thread3 t3 = example.new Thread3();

	        t1.start();
	        t2.start();
	        t3.start();
	    }
	}

