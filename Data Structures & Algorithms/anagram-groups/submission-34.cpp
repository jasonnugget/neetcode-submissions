class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> ana;
        for (const string& s : strs) {
            vector<int> counts(26, 0);
            for (const char& c : s) {
                counts[c - 'a']++;
            }

            string key = to_string(counts[0]);
            for (int i = 1; i < 26; i++) {
                key+= ',' + to_string(counts[i]);
            }

            ana[key].push_back(s);
        }
        
        vector<vector<string>> res;
        for (const auto& [key, val]: ana) {
            res.push_back(val);
        }

        return res;
    }
};
