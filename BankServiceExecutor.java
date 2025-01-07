package lab11scd;

public class BankServiceExecutor {
    public static void main(String[] args) {
        // Instantiate concrete services
        BankService billPaymentService = new BillPaymentService();
        BankService accountOpeningService = new AccountOpeningService();
        BankService loanFollowUpService = new LoanFollowUpService();

        // Execute each service
        System.out.println("Executing Bill Payment Service:");
        billPaymentService.performService();

        System.out.println("\nExecuting Account Opening Service:");
        accountOpeningService.performService();

        System.out.println("\nExecuting Loan Follow-Up Service:");
        loanFollowUpService.performService();
    }
}