import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	
	static int N;
	static int M;
	static int[] arr;
	
	public static void main(String[] args) throws Exception {
		
		st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		arr = new int[N+1];
		
		for(int i=1;i<=N;++i) {
			arr[i] = i;
		}
		
		for(int i=0;i<M;++i) {
			st = new StringTokenizer(br.readLine());
			
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			
			reverse(s,e);
		}
		
		for(int i=1;i<=N;++i) {
			sb.append(arr[i] + " ");
		}
		System.out.println(sb);
	}
	
	static void reverse(int start,int end) {
		
		for(int i=0;i<=(end-start)/2;++i) {
			int temp = arr[start+i];
			arr[start+i] = arr[end-i];
			arr[end-i] = temp;
		}
	}
}