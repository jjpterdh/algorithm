import java.util.*;


public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.next();
		
		int min = Integer.MAX_VALUE;
		
		int aCnt = 0;
		for(int i=0; i<str.length(); i++) {
			if(str.charAt(i) =='a') {
				aCnt++;
			}
		}
		
		for(int i=0; i<str.length(); i++) {
			int bCnt = 0;
			for(int j=i; j<i+aCnt; j++) {
				int idx = j%str.length();
				if(str.charAt(idx) =='b') {
					bCnt++;
				}
			}
			min = Math.min(min, bCnt);
		}
		
		System.out.println(min);
	}
}
