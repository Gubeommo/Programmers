import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        List<Integer> list = new ArrayList<Integer>(Arrays.asList(0,1,2,3,4,5,6,7,8,9));
        
        for(Integer number : numbers){
             list.remove(Integer.valueOf(number));
        }
        
       for(int result : list){
           answer += result;
       }
       
        return answer;
    }
}