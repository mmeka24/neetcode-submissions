class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false; 
        }

        s = s.toLowerCase();
        t = t.toLowerCase();

        char[] s_ort = s.toCharArray(); 
        char[] t_ort = t.toCharArray(); 
        Arrays.sort(s_ort); 
        Arrays.sort(t_ort); 

           return Arrays.equals(s_ort, t_ort);
           //must use arrays.equals. 
           //.equals compares the referene (memory loco)

    }
}
