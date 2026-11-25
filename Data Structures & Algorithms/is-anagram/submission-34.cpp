class Solution {
public:
    bool isAnagram(string s, string t) {
     unordered_map<char, int> sCounts;
     for (int i = 0; i < s.size(); i++) {
        sCounts[s[i]]++;
     };

     unordered_map<char, int> tCounts;
     for (int i = 0; i < t.size(); i++) {
        tCounts[t[i]]++;
     };

     return sCounts == tCounts;
    }
};
