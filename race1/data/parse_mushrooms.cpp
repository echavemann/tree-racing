inline loadMushroomData()
{
    std::filesystem::path const mushroomPath = util::getSrcPath().append(DATASET_DIR).append(CATEGORICAL_DIR).append(MUSHROOM_FILENAME);
    io::CSVReader<23> csvReader(mushroomPath);

    std::vector<std::vector<int>> features;
    std::vector<int> labels;
    int label;
    int f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22;
    while (csvReader.read_row(label, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22))
    {
        features.push_back({f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22});
        labels.push_back(label);
    }
    return {features, labels};
}
