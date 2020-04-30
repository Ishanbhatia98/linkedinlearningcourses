#include<iostream>
#include<vector>
#include<string>
#include<memory>


using namespace std;

class Fruit{
	string _name;
	string _flavor;
	string _color;
	public:
	Fruit(const string &n, const string &f, const string &c): _name(n), _flavor(f), _color(c) {};
	string flavor() const{return _flavor;}
	string color() const {return _color;}
	string name() const {return _name;}
};


int main(){
	
	string s = "ishan";
	vector<int> v = {1, 2, 3, 4, 5};

	//Defining a unique pointer
	std::unique_ptr<Fruit> a( new Fruit("Apple", "sweet", "red"));
	cout << "Name: " << a->name() << endl;
	cout << "flavour: " << a->flavor() << endl;
	cout << "color: " << a->color() << endl;

	a.reset(new Fruit("pear", "sour", "green"));
	cout << "Name: " << a->name() << endl;

	//cannot copy a unique pointer
	//auto b = std::make_unique<Fruit>(("banana", "sweet", "yellow"));
	
	
	//Defining a Shared pointer
	auto b = std::make_shared<Fruit>("grapes", "sugary", "purple");

	
	//Can copy shared pointers!
	auto d = b;
	cout << "Name: " << d->name() << endl;
	cout << "Flavor: " << d->flavor() << endl;
	cout << "Color: " << d->color() << endl;
	
	b.reset(new Fruit("orange" , "sour", "orange"));
	
	//reference to d is also released
	cout << "Name: " << d->name();
	
	//releasing a pointer doesnt destroy the object
	a.release();
	
	//Fruit f("tomato", "bland", "red");
	//std::unique_ptr<Fruit> g(*f);
	
	return 0;
}
