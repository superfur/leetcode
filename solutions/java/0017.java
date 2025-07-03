class Solution {
    public List<String> letterCombinations(String digits) {
        if (digits.isEmpty()) {
            return new ArrayList<>();
        }

        Map<Character, String> map = new HashMap<>();
        map.put('2', "abc");
        map.put('3', "def");
        map.put('4', "ghi");
        map.put('5', "jkl");
        map.put('6', "mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");

        List<String> result = new ArrayList<>();
        StringBuilder combination = new StringBuilder();

        backtrack(digits, 0, map, combination, result);
        return result;
    }

    private void backtrack(String digits, int index, Map<Character, String> map, StringBuilder combination, List<String> result) {
        if (index == digits.length()) {
            result.add(combination.toString());
            return;
        }

        String letters = map.get(digits.charAt(index));
        for (char letter : letters.toCharArray()) {
            combination.append(letter);
            backtrack(digits, index + 1, map, combination, result);
            combination.deleteCharAt(combination.length() - 1);
        }
    }
}