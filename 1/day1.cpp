#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<std::string> readFileLineByLine(const string& filename) {
    ifstream file(filename);
    vector<string> lines;
    string line;

    if (!file.is_open()) {
        cerr << "Error opening file: " << filename << endl;
        return lines;
    }

    while (getline(file, line)) {
        lines.push_back(line);
    }

    return lines;
}

int main() {
    vector<std::string> input = readFileLineByLine("input.txt");
    int total = 0;
    vector<int> id1, id2;
    for(string line : input) {
        int num1, num2;
        
        stringstream ss(line);
        
        ss >> num1 >> num2;
        id1.push_back(num1);
        id2.push_back(num2);   
    }
    sort(id1.begin(), id1.end());
    sort(id2.begin(), id2.end());
    for (int i = 0; i < id1.size(); i++) {
        int multiples = 0;
        for (int j = 0; j < id2.size(); j++) {
            if(id1[i] == id2[j]){
                multiples++;
            }
        }
        total += id1[i] * multiples;
    }
    
    cout << endl << total;
}