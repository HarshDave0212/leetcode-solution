class Solution {
    public String reverseWords(String s) {
        s=s.trim();
        int a = s.length();
        ArrayList<String> result= new ArrayList<>();
        StringBuilder sb = new StringBuilder("");
        for (int i = a-1; i>=0; i--){
            if (s.charAt(i) == ' '){
                if (sb.length() != 0){
                result.add(sb.toString());
                }
                sb.setLength(0); 
            }
            else{
                sb.insert(0, s.charAt(i));
            }
        }

        result.add(sb.toString());
        String ans = String.join(" ",result);
        return (ans);
        
    }
}