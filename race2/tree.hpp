#include <map>
#include <string>
#include <vector>
class ID3Tree
{

ID3Tree(std::map<std::string, std::string> config)
{
}

void train(std::vector<std::vector<int>> & features, std::vector<int> & target)
{
    return;
}

int predict(std::vector<int> & features)
{
    return 0;
}

};

std::map<std::string, std::string> optimizeParameters(std::vector<std::vector<int>> & features, std::vector<int> & targets)
{
    return {};
}
