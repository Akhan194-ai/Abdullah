package lab10;

public final class Pi {
    public static final double VALUE = 3.141592653589793;  // Value of Pi

    // Private constructor to prevent instantiation
    private Pi() {
        throw new UnsupportedOperationException("Pi is a constant and cannot be instantiated.");
    }
}
