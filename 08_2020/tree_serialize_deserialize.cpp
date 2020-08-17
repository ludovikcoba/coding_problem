/*Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

*/
#include <iostream>
#include <string>
#include <cassert>
#include <vector>

using std::string;
using std::cout;
using std::vector;

class Node{
    public:
        string val;
        Node *left = NULL;
        Node *right = NULL;

        Node(string val): val(val){};
};

string serialize(Node *root){
    if (root == NULL) return "/";
    
    string s = root->val;

    s += "++" + serialize(root->left);
    s += "++" + serialize(root->right);

    return s;
}

Node *deserializer(vector<string>::iterator &it){
    if(*it == "/") return NULL;

    Node *n = new Node(*it);
    it++;
    n->left = deserializer(it);
    n->right = deserializer(it);

    return n;

}

Node *deserialize(string text){
    vector<string> values;

    string temp = "";

    int i = 0;
    size_t pos;
    
    while (pos = text.find("++") != string::npos)//<- not working as expected
    {
        throw "Requires fixing";
        cout << pos << " "<< text.substr(i,pos-i)<< std::endl;
        values.push_back(text.substr(i,pos));
        i=pos+1;
    }

    for (string a: values){
        cout << a << " ";
    }
        
    vector<string>::iterator it = values.begin();   

    Node *root = deserializer(it);   

}


void printInOrder(Node *n){
    if (n==NULL) return;
    printInOrder(n->left);
    cout << n->val << " ";
    printInOrder(n->right);

}

int main(){
    Node *n = new Node("root");
    n->left = new Node("left");
    n->left->left = new Node("left.left");
    n->right = new Node("right");

   

    cout << serialize(n);

     cout << std::endl;

    printInOrder(deserialize(serialize(n)));

}