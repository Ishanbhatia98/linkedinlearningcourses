#include<iostream>
#include<algorithm>
//#include<locale>

constexpr size_t _maxlen = 128;

using namespace std;

class ftitle{
	char lastc;
	public:
	ftitle():lastc(0){};
	char operator () (const char &c);
};

char ftitle::operator () (const char &c){
	const char r = (lastc==' ' || lastc==0)? toupper(c):tolower(c);
	lastc = c;
	return r;
	
}

int main(){
	char lastc = 0;	
	char s[] = "The sky is a beautiful shade of blue today!";
	//transform(s, s+strnlen(s, _maxlen), s, ftitle());
	transform(s, s+strnlen(s, _maxlen), s, [&lastc ](const char &c ) -> char {
			const char r = (lastc==' ' || lastc==0)? toupper(c):tolower(c);
        		lastc = c;
        		return r;
		});
	
	puts(s);
	return 0;
}
