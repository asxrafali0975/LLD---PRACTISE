#include <iostream>
#include <mutex>
using namespace std;

class Singleton
{
private:
    static Singleton *instance;
    int some_value = 10;
    static mutex mtx;

    Singleton(int some_value)
    {
        cout << "singleton object made" << endl;
        this->some_value = some_value;
    }

public:
    static Singleton *getInstance(int value)
    {
        if (Singleton::instance == nullptr)
        {
            lock_guard<mutex> lock(mtx);
            if (Singleton::instance == nullptr)
            {
                Singleton *s1 = new Singleton(value);
                Singleton::instance = s1;
            }
        }

        return Singleton::instance;
    }

    static void giveData(Singleton *object)
    {
        cout << object->some_value << endl;
    }
};

Singleton *Singleton::instance = nullptr;
mutex Singleton::mtx;

int main()
{

    Singleton *s1 = Singleton::getInstance(50);
    Singleton *s2 = Singleton::getInstance(100);

    Singleton::giveData(s1);
    Singleton::giveData(s2);

    cout << (s1 == s2);

    return 0;
}
