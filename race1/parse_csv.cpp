loadTennisData(std::filesystem::path const & tennisPath)
{
    io::CSVReader<5> csvReader(tennisPath);

    std::vector<std::vector<int>> features;
    std::vector<int> labels;

    int f1, f2, f3, f4, label;

    while (csvReader.read_row(f1, f2, f3, f4, label))
    {
        features.push_back({f1, f2, f3, f4});
        labels.push_back(label);
    }

    return {features, labels};
}
