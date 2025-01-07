package lab10;

public class FailedStudent {
	 private final String rollNumber;
	    private final String subjectCode;
	    private final String subjectName;

	    // Constructor to initialize the values
	    public FailedStudent(String rollNumber, String subjectCode, String subjectName) {
	        this.rollNumber = rollNumber;
	        this.subjectCode = subjectCode;
	        this.subjectName = subjectName;
	    }

	    // Getter methods for the fields
	    public String getRollNumber() {
	        return rollNumber;
	    }

	    public String getSubjectCode() {
	        return subjectCode;
	    }

	    public String getSubjectName() {
	        return subjectName;
	    }
	}

