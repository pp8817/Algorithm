import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int i;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        i = Integer.parseInt(st.nextToken());
        check(i);
    }

    public static void check(int i) {
        for (int j = 1; 10 > j; j ++) {
            System.out.println(i+" * "+j+" = "+(j*i));
        }
    }
}