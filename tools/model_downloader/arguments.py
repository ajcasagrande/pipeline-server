'''
* Copyright (C) 2019-2020 Intel Corporation.
*
* SPDX-License-Identifier: BSD-3-Clause
'''

import argparse

def parse_args(args=None):
    parser = argparse.ArgumentParser(description="Download & Convert models from Open Model Zoo.")
    parser.add_argument('--output', '--output-dir', required=False, default=".",
                        dest="output_dir",
                        help='path where to save models')
    parser.add_argument('--model-list', default="models_list/models.list.yml",
                        help='input file with model names and properties')
    parser.add_argument('--model-proc-version', default="v1.3",
                        dest="dl_streamer_version",
                        help='Intel(R) DL Streamer Framework version for model proc files')
    parser.add_argument("--force", required=False, dest="force", action="store_true",
                        default=False, help='force download and conversion of existing models')

    args = parser.parse_args(args)
    return args
