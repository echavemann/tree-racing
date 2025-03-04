inline loadZooData()
{
    std::filesystem::path const carEvalPath = util::getSrcPath().append(DATASET_DIR).append(CATEGORICAL_DIR).append(ZOO_FILENAME);
    io::CSVReader<17> csvReader(carEvalPath);

    std::vector<std::vector<int>> features;
    std::vector<int> labels;
    int label;
    int f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16;
    while (csvReader.read_row(f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, label))
    {
        features.push_back({f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16});
        labels.push_back(label);
    }
    return {features, labels};
}

