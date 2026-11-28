class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<vector<int>, vector<string>> ana;
        for (const string& s : strs) {
            vector<int> counts(26, 0);
            for (const char& c : s) {
                counts[c - 'a']++;
            }

            ana[counts].push_back(s);
        }
        
        vector<vector<string>> res;
        for (const auto& [key, val]: ana) {
            res.push_back(val);
        }

        return res;
    }
};
