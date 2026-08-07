#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""逐節 append cell 規格到 *.jsonl 的共用小工具（paper-to-notebook 技能 §5 步驟 3a）。

用法（在 _work/ 底下）：
    py -X utf8 paper_01.py      # 會 append 到 a_paper.jsonl
最後由 assemble.py 依 a_paper -> b_ai -> c_disc 的順序串成 Schubert2006.cells.jsonl。
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def write(fname, cells):
    """把 cells（list[str]）整份覆寫成一個 jsonl，方便重跑不重複。"""
    path = os.path.join(HERE, fname)
    with open(path, "w", encoding="utf-8") as f:
        for src in cells:
            f.write(json.dumps({"cell_type": "markdown", "source": src},
                               ensure_ascii=False) + "\n")
    return len(cells)


def append(fname, cells):
    path = os.path.join(HERE, fname)
    with open(path, "a", encoding="utf-8") as f:
        for src in cells:
            f.write(json.dumps({"cell_type": "markdown", "source": src},
                               ensure_ascii=False) + "\n")
    return len(cells)
