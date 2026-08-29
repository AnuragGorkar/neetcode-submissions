class Solution {
public:
    bool isPalindrome(string &s, int i, int j){ 
        while(i<j)
            if(s[i++]!=s[j--])
                return false;
        return true;
    }

    void recurLongestPalindromicSubString(int i, int j, string &s, int &ansI, int &ansJ, vector<vector<int>> &memo){ 
        if(i<=j){ 
           if(memo[i][j])
                return;
           else{ 
                memo[i][j] = true;
                if(isPalindrome(s, i, j) && (j-i)>(ansJ-ansI)){ 
                    ansI = i; 
                    ansJ = j;
                }else{ 
                    recurLongestPalindromicSubString(i+1, j, s, ansI, ansJ, memo);
                    recurLongestPalindromicSubString(i, j-1, s, ansI, ansJ, memo);
                    recurLongestPalindromicSubString(i+1, j-1, s, ansI, ansJ, memo);
                }
           }
        }
    }

    string longestPalindrome(string s) {
        int ansI=0, ansJ=0;
        vector<vector<int>> memo(s.length(), vector<int>(s.length(), false));
        recurLongestPalindromicSubString(0, s.length()-1, s, ansI, ansJ, memo);
        return s.substr(ansI, ansJ-ansI+1);
    }
};
