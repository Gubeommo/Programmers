class Solution {
    public long solution(int price, int money, int count) {
        long answer = 0;
        int basic = price;
        for (int i=0; i< count; i++){
            answer += price;
            price += basic;
        }
        if(money < answer){
            return answer-money;
        }else{
            return 0;
        }
    }
}