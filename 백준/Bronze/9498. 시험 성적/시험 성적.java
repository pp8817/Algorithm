import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int exam;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        exam = Integer.parseInt(st.nextToken());

        System.out.println(check(exam));
    }

    public static String check(int exam) {
        if (exam >= 90) {
            return "A";
        } else if (exam>=80) {
            return "B";
        } else if (exam>=70) {
            return "C";
        } else if (exam >= 60) {
            return "D";
        } else {
            return "F";
        }
    }
}