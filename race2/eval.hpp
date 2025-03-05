#pragma once


#include <chrono>

static constexpr int N_TRIALS = 1'000;

void evaluateModels()
{

    auto [tennisFeatures, tennisLabels] = loadTennisData();
    auto tuneStart = std::chrono::high_resolution_clock::now();
    auto bestConfig = optimizeParameters(tennisFeatures, tennisLabels);
    auto tuneEnd = std::chrono::high_resolution_clock::now();

    // run the loop, collect acc and whatnot.


}
