#ifndef ARRAY_UTILITY_HPP
#define ARRAY_UTILITY__HPP

#include <vector>

/*
** \brief Create an std::array of type double of a certain dimension
*/

class ArrayUtil
{

public:

    // public construction, just need to specify the array "size"
    ArrayUtil(int size);

private:
    std::vector<double> vec;

};


#endif
