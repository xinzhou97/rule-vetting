from os.path import join as oj

import os
import unittest

import mrules
import mrules.api.util

PROJECT_PATH = oj(os.path.dirname(os.path.abspath(__file__)), '..', 'mrules', 'projects')


class TestAllFilesPresent(unittest.TestCase):
    def test_all_files_present(self):
        """Check that all required files are present
        """
        for project_id in os.listdir(PROJECT_PATH):
            if not os.path.isdir(oj(mrules.PROJECTS_PATH, project_id)):
                continue
            if 'cache' in project_id:
                continue

            project_dir = oj(PROJECT_PATH, project_id)
            project_files = os.listdir(project_dir)
            assert 'readme.md' in project_files
            assert 'data_dictionary.md' in project_files
            assert '__init__.py' in project_files
            assert 'dataset.py' in project_files
            assert 'baseline.py' in project_files
