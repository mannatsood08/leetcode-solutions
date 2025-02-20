class Solution {
    public boolean isAdditiveNumber(String num) {
        if (num.length() < 3) return false;
        for (int ia = 1; ia < num.length() / 2 + 1; ia++) {
            String a = num.substring(0, ia);
            if (a.startsWith("0") && a.length() > 1) return false;
            for (int ib = ia + 1; ib < num.length() / 3 * 2 + 1; ib++) {
                String b = num.substring(ia, ib);
                if (b.startsWith("0") && b.length() > 1) continue;
                if (solve(a, b, num, ib)) return true;
            }
        }
        return false;
    }

    private static boolean solve(String a, String b, String num, int cur) {
        if (cur == num.length()) return true;
        StringBuilder sb = new StringBuilder();
        int carry = 0;
        for (int ia = a.length() -1, ib = b.length() - 1; ia >= 0 || ib >= 0 ;ia--, ib--) {
            int c = (ia < 0 ? '0' : a.charAt(ia)) + (ib < 0 ? '0' : b.charAt(ib)) + carry - '0';
            if (c > '9') {
                c -= 10;
                carry = 1;
            } else carry = 0;
            sb.append((char)c);
        }
        if (carry == 1) sb.append('1');
        String s = sb.reverse().toString();
        if (!num.substring(cur).startsWith(s)) return false;
        return solve(b, s, num, cur + s.length());
    }
}