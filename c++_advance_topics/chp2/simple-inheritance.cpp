#include<iostream>
#include<string>

using namespace std;

class Animal{
	string _name;
	string _type;
	string _sound;
	protected:
		Animal(const string &name, const string &type, const string &sound):_name(name), _type(type), _sound(sound) {};
	public:
		void speak() const;
		const string name() const{return _name;}
		const string type() const{return _type;}
		const string sound() const{return _sound;}
};

void Animal::speak() const {
	printf("%s the %s says  %s \n", &_name, &_type, &_sound);
}

class Dog:public Animal{
	int _walked;
	public:
	Dog(string n): Animal(n, "dog", "woof"), _walked(0) {};
	int walk() {return ++_walked;}
};

class Cat: public Animal{
	int _purr;
	public:
	Cat(string n):Animal(n, "cat", "meow"), _purr(0) {};
	int purr() {return ++_purr;}
};

int main(){
	Dog d("Boozo");
	cout << "Name: " << d.name() << endl;
	cout << "Type: " << d.type() << endl;
	cout << "Sound: " <<d.sound() << endl;
	d.speak();
	
	Cat c("Daisy");
	c.speak();
	cout << "Purr: " << c.purr() << endl;
	cout << c.purr() << endl;
	cout << c.purr() << endl;
	return 0;
}
