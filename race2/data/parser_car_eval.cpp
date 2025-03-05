loadCarEvalData(std::filesystem::path const & carEvalPath)
{
    io::CSVReader<7> csvReader(carEvalPath);

    std::vector<std::vector<int>> features;
    std::vector<int> labels;
    int label;
    int f1, f2, f3, f4, f5, f6;
    while (csvReader.read_row(f1, f2, f3, f4, f5, f6, label))
    {
        features.push_back({f1, f2, f3, f4, f5, f6});
        labels.push_back(label);
    }
    return {features, labels};
}
