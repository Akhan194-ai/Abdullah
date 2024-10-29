package lab3Task3;

import java.util.Date;

public class Main {
    public static void main(String[] args) {
        // Create a customer instance
        Customer customer = new Customer('C', 'Abdullah', '123 Street', 1234567890, 30);
        customer.addDetails();
        customer.modifyDetails();

        // Create an agent and use common functions
        Agent agent = new Agent(101, 'A');
        agent.fillDetails();
        agent.searchTicket();
        agent.bookTicket();
        agent.makePayment();
        agent.cancelTicket();

        // Create a ticket instance
        Ticket ticket = new Ticket('A', 'B', new Date(), "10:00 AM", '123', 'A1');

        // Create and process a refund
        Refund refund = new Refund(100.0f, 'C');
        refund.refundAmount();

        // Initialize BookingCounter if needed
        BookingCounter bookingCounter = new BookingCounter();
        // BookingCounter functionality can be added as needed
    }
}
