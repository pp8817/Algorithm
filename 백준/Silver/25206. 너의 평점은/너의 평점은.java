import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        double sumNumXScore = 0; //총 과목 평점
        double sumNum = 0; //총 학점

        for (int i = 0; i < 20; i++) {
            st = new StringTokenizer(br.readLine());
            String Object = st.nextToken();
            double num = Double.parseDouble(st.nextToken()); //학점
            String alp = st.nextToken(); //과목 등급
            double score = 0; //과목 평점

            if (!(alp.equals("P"))) {
                switch (alp) {
                    case "A+":
                        score = 4.5;
                        break;
                    case "A0":
                        score = 4.0;
                        break;
                    case "B+":
                        score = 3.5;
                        break;
                    case "B0":
                        score = 3.0;
                        break;
                    case "C+":
                        score = 2.5;
                        break;
                    case "C0":
                        score = 2.0;
                        break;
                    case "D+":
                        score = 1.5;
                        break;
                    case "D0":
                        score = 1.0;
                        break;
                    case "F":
                        score = 0.0;
                        break;
                    default:
                        break;
                }
                sumNumXScore += (num * score);
                sumNum += num;
            }
           
        }
        System.out.printf("%.6f", sumNumXScore / sumNum);
        br.close();
    }
}