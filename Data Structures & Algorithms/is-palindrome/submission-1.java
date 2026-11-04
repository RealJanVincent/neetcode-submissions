class Solution {
    public boolean isPalindrome(String s) {
        int start = 0;
        s = s.toLowerCase();
        int end = s.length() - 1;
        while(start < end) {
            if(!Character.isLetterOrDigit(s.charAt(start))) {
                start++;
            }else if(!Character.isLetterOrDigit(s.charAt(end))) {
                end--;
            }else if (s.charAt(start) != s.charAt(end)) {
                return false;
            } else {
                start++;
                end--;
            }
        }
        return true;
    }
}
