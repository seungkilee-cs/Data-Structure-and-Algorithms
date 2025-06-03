#include "DSString.hpp"

using namespace std;

//default constructor
DSString::DSString()
{
    charArray=nullptr;
    sizeOf=0;
}

//cstring constructor
DSString::DSString(const char* incomingArray)
{
    int count=0;
    //create copy of pointer for the count
    const char* ptr=incomingArray;
    //iterate over char array to determine length
    while(*ptr++)
    {
        count++;
    }
    //create char array
    charArray = new char[count + 1];
    sizeOf = count;
    //iterate over original char array -> assign to destination array
    for(int i=0;i<count+1;i++)
    {
        charArray[i]=incomingArray[i];
    }
    //ensure final char value in array is null
    charArray[count] = '\0';
    return;
}

char* DSString::c_str() const
{
    return charArray;
}

int DSString::size() const
{
    return sizeOf;
}

//copy constructor
DSString::DSString(const DSString& incomingString)
{
    int count=0;
    //create copy of pointer for the count
    const char* ptr=incomingString.c_str();
    while(*ptr++)
    {
        count++;
    }
    //create char array
    charArray = new char[count + 1];
    sizeOf = count;
    //iterate over original char array from String object -> assign to destination array
    for(int i=0;i<count+1;i++)
    {
        charArray[i]=incomingString.c_str()[i];
    }
    //ensure final char value in array is null
    charArray[count] = '\0';
    return;

}

//assignment operator from cstring
DSString& DSString::operator= (const char* incomingArray)
{
    //remove previous char array to prepare for new char array
    delete[] charArray;
    int count=0;
    //copy pointer from incoming char array
    const char* ptr=incomingArray;
    //iterate over char values to determine length
    while(*ptr++)
    {
        count++;
    }
    charArray = new char[count + 1];
    sizeOf = count;
    //iterate over original char array -> assign to destination array
    for(int i=0;i<count+1;i++)
    {
        charArray[i]=incomingArray[i];
    }
    //ensure final char value in array is null
    charArray[count] = '\0';
    return *this;
}

//assignment operator from String object
DSString& DSString::operator= (const DSString& incomingString)
{
    return operator=(incomingString.c_str());
}

//concatenation operator
DSString DSString::operator+ (const DSString& incomingString)
{
    //logic check for empty string object
    if(incomingString.size() == 0)
    {
        return *this;
    }
    //create length value for current string object + second string
    int newLength=(this->sizeOf+(incomingString.size()));
    char* tempChar = new char[newLength];
    //copy current char value(s)
    for(int i=0;i<this->sizeOf;i++)
    {
        tempChar[i]=this->charArray[i];
    }
    //copy second string object char value(s)
    for(int i=0;i<(incomingString.size());i++)
    {
        tempChar[i+sizeOf]=incomingString.c_str()[i];
    }
    //ensure final char value in array is null
    tempChar[newLength]='\0';
    return DSString(tempChar);
}

//not equals operator from char array
bool DSString::operator !=(const char* incomingArray)
{
    return !(*this==incomingArray);
}

//not equals operator from String object
bool DSString::operator !=(const DSString& incomingString)
{
    return !(*this==incomingString);
}


//equivalency operator from char array
bool DSString::operator==(const char* incomingArray)
{
    if((strcmp(charArray,incomingArray)) == 0)
    {
        return true;
    }
    else
        return false;

}

//equivalency operator from String object
bool DSString::operator== (const DSString& incomingString)
{
    //call previously defined equivalency operator with String method for char*
    return operator==(incomingString.c_str());
}

//greater than operator
bool DSString::operator> (const DSString& incomingString)
{

//    if(sizeOf > incomingString.sizeOf)
//    {
//        return true;
//    }

//    else if(sizeOf < incomingString.sizeOf)
//    {
//        return false;
//    }

    return std::strcmp(charArray,incomingString.c_str()) > 0;
}

//less than operator
bool DSString::operator< (const DSString& incomingString)
{

//    if(sizeOf < incomingString.sizeOf)
//    {
//        return true;
//    }

//    else if(sizeOf > incomingString.sizeOf)
//    {
//        return false;
//    }

    return std::strcmp(charArray,incomingString.c_str()) < 0;
}

//@ operator -> choose single element of String object's char array at specified index location
char& DSString::operator[] (const int index)
{
    //duplicate value due to passing const
    int element=index;
    //negative index value
    if(element<0)
    {
        element+=sizeOf;
    }
    else if(element>sizeOf)
    {
        element-=sizeOf;
    }
    return charArray[element];
}

//substring -> return new String object made of substring from supplied index location (start,stop) inclusive
DSString DSString::substring(int start, int end)
{
    //negative starting index location
    if(start<0)
    {
        start+=sizeOf+1;
        end+=sizeOf+1;
    }
    //negative ending index location
    if(end<0)
    {
        end+=sizeOf+1;
    }
    //determine length of new String object
    int length=(end-start);
    char* newArray = new char[length];
    //copy char by char into new String object
    for(int i=0;i<length;i++)
    {
        newArray[i]=charArray[i+start];
    }
    //ensure final char value in array is null
    newArray[length]='\0';
    return DSString(newArray);
}

//stream insertion operator
std::ostream& operator<< (std::ostream& stream, const DSString& string)
{
    stream<<string.charArray;
    return stream;
}

//destructor
DSString::~DSString()
{
    delete[] charArray;
}

void DSString::toUpper()
{
    if(this->size()>0)
    {
        for(int i=0;i<sizeOf;i++)
        {
            if(charArray[i]>= 'a' && charArray[i]<= 'z')
            {
                charArray[i]-=32;
            }
        }
    }
}

void DSString::toLower()
{
    if(this->size()>0)
    {
        for(int i=0;i<sizeOf;i++)
        {
            if(charArray[i]>= 'A' && charArray[i]<= 'Z')
            {
                charArray[i]+=32;
            }
        }
    }
}
