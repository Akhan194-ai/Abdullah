package lab3Task3;

import java.util.Date;

public class Ticket {
    private char source;
    private char destination;
    private Date dateOfJourney;
    private String time;
    private char busNo;
    private char seatNo;

    // Constructor
    public Ticket(char source, char destination, Date dateOfJourney, String time, char busNo, char seatNo) {
        this.source = source;
        this.destination = destination;
        this.dateOfJourney = dateOfJourney;
        this.time = time;
        this.busNo = busNo;
        this.seatNo = seatNo;
    }

    // Getters and Setters (optional)
}
