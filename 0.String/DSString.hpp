#ifndef STRING
#define STRING

#include <iostream>
#include <cstring>

class DSString{

public:

    DSString();
    DSString(const char*);
    DSString(const DSString&);

    DSString& operator= (const char*);
    DSString& operator= (const DSString&);
    DSString operator+ (const DSString&);

    bool operator== (const char*);
    bool operator== (const DSString&);
    bool operator!= (const char*);
    bool operator!= (const DSString&);
    bool operator> (const DSString&);
    bool operator< (const DSString&);

    char& operator[] (const int);

    int size() const;
    DSString substring(int, int);
    char* c_str() const;

    void toUpper();
    void toLower();

    friend std::ostream& operator<< (std::ostream&, const DSString&);

    ~DSString();

private:

    char* charArray;
    int sizeOf;
};


#endif
