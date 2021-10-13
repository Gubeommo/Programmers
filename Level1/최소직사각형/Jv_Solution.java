import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int[] result = {0,0};
        
        for (int[] tempNumber : sizes)
        {
            Arrays.sort(tempNumber);
            if (result[0] < tempNumber[0])
            {
                result[0] = tempNumber[0];
            }
            if (result[1] < tempNumber[1])
            {
                result[1] = tempNumber[1];
            }

        }
        return result[0] * result[1];
    }
}