#include<iostream>
#include<vector>

using namespace std;

template<typename T>
void printv(vector<T> &v){
	if (v.empty()) return;
	for (auto i:v){
		cout << i << " ";
	}
	cout << endl;
}

int main(){
	vector<int> v1 = {1, 2, 3, 4, 5};
	vector<int> v2(v1.size());
	
	cout << "v1: ";
	printv<int>(v1);
	cout << "v2: ";
	printv<int>(v2);

	v2 = std::move(v1);
	
	cout << "v1: "; 
	printv<int>(v1);
	cout << "v2: ";
	printv<int>(v2);

	return 0;
}
