#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把 a_paper.jsonl -> b_ai.jsonl -> c_disc.jsonl 串成 Schubert2006.cells.jsonl。

完整重跑流程（在 _work/ 底下）：
    py -X utf8 paper_01.py && py -X utf8 paper_02.py && py -X utf8 paper_03.py \
        && py -X utf8 paper_04.py && py -X utf8 ai_cells.py && py -X utf8 disc_cells.py \
        && py -X utf8 assemble.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PARTS = ["a_paper.jsonl", "b_ai.jsonl", "c_disc.jsonl"]
OUT = "Schubert2006.cells.jsonl"

lines = []
for p in PARTS:
    with open(os.path.join(HERE, p), "r", encoding="utf-8") as f:
        for ln in f:
            if ln.strip():
                lines.append(ln.rstrip("\n"))

with open(os.path.join(HERE, OUT), "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

print("%s  cells=%d" % (OUT, len(lines)))
