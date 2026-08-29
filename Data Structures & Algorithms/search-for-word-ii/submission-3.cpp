struct TrieNode {
    public:
    unordered_map<char, TrieNode*> children;
    bool isEnd = false;
};

class Solution {
public:
    void mapWords(vector<vector<char>>& board, int i, int j, vector<vector<bool>>& visited, TrieNode* node, unordered_set<string>& res, string& currWord){ 
        int m = board.size(); 
        int n = board[0].size();
        if(node->isEnd)
            res.insert(currWord);
        visited[i][j] = true;
        vector<vector<int>> posUpdate = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for(auto updated: posUpdate){ 
            int new_i = i+updated[0]; 
            int new_j = j+updated[1];
            if(new_i>=0 && new_j>=0 && new_i<m && new_j<n && !visited[new_i][new_j]){
                char c = board[new_i][new_j];
                if(node->children.find(c)!=node->children.end()) {
                    string originalWord = currWord;
                    currWord+=board[new_i][new_j];
                    mapWords(board, new_i, new_j, visited, node->children[c], res, currWord);
                    currWord=originalWord;
                }           
            }
        } 
        visited[i][j] = false;
    }

    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        int m = board.size(); 
        int n = board[0].size();

        unordered_set<string> res;
        TrieNode* root = new TrieNode();

        for(auto word: words){ 
            TrieNode* node = root;
            for(auto letter: word) {
                if(node->children.find(letter) == node->children.end())
                    node->children[letter] = new TrieNode();
                node = node->children[letter];
            }
            node->isEnd = true;
        }

        vector<vector<bool>> visited(m, vector<bool>(n, false));
        for(int i=0; i<m; i++){ 
            for(int j=0; j<n; j++){ 
                char c = board[i][j]; 
                if(root->children.find(c)!=root->children.end()){
                    string currWord = "";
                    currWord += c;
                    mapWords(board, i, j, visited, root->children[c], res, currWord);
                }
            }
        }
        vector<string> res_list(res.begin(), res.end());
        return res_list;
    }
};
