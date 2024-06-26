import warnings
from pathlib import Path
from typing import Union

import pandas as pd

from fundus_evaluation.analysis import (
    compute_rouge_lsum_scraper_summary,
    compute_rouge_lsum_scraper_to_publisher_summary,
    draw_complexity_boxplot,
    draw_rouge_lsum_f1_score_stripplot,
    draw_rouge_lsum_stripplot,
)


def analysis(
    output_directory: Union[str, Path],
    complexity_path: Union[str, Path, None] = None,
    rouge_lsum_path: Union[str, Path, None] = None,
) -> None:
    output_directory = Path(output_directory)
    output_directory.mkdir(parents=True, exist_ok=True)

    if complexity_path is not None:
        complexity: pd.DataFrame = pd.read_csv(complexity_path, sep="\t")
        if complexity.isna().any(axis=None):
            warnings.warn("NaN values detected in complexity results.")

        draw_complexity_boxplot(complexity, out=output_directory)

    if rouge_lsum_path:
        rouge_lsum: pd.DataFrame = pd.read_csv(rouge_lsum_path, sep="\t")
        if rouge_lsum.isna().any(axis=None):
            warnings.warn("NaN values detected in ROUGE-LSum results.")

        draw_rouge_lsum_stripplot(rouge_lsum, out=output_directory)
        draw_rouge_lsum_f1_score_stripplot(rouge_lsum, out=output_directory)
        compute_rouge_lsum_scraper_summary(rouge_lsum, out=output_directory)
        compute_rouge_lsum_scraper_to_publisher_summary(rouge_lsum, out=output_directory)
