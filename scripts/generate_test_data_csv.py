from pathlib import Path

from scripts.data import test_data


batches_dir = Path(__file__).parent.parent.joinpath("load-test-batches")


def dummy_test_data_csv(file_name, n):
    dataset = test_data.dummy_dataset_double_n_times(n)
    dataset.to_dataframe().to_csv(file_name, sep=";", encoding="utf-8", index=False)


if __name__ == "__main__":
    batches = (1, 5, 10, 20, 30)

    for batch in batches:
        file_name = f"dummy-data-loadtest_{batch*5000}.csv"
        dummy_test_data_csv(batches_dir.joinpath(file_name), batch)
