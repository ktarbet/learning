# program to scan repositories with goals:
# 1 - get overall lines of code and files
# 2 - estimat amount of HEC-DSS usage


import os
import re
import subprocess


class Repository:
    def __init__(self, root_directory, file_extension):
        self.root_directory = root_directory
        self.file_extension = file_extension
        self.file_content = self.load_file_content()
        self.name = os.path.basename(root_directory)

    def load_file_content(self):
        file_content = {}
        for root, _, files in os.walk(self.root_directory):
            for file_name in files:
                if file_name.endswith(self.file_extension):
                    file_path = os.path.join(root, file_name)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            file_content[file_name] = file.readlines()
                    except UnicodeDecodeError:
                        print(f"Error reading {file_path}")

        return file_content

    def count_total_lines(self):
        total_lines = 0
        for lines in self.file_content.values():
            total_lines += len(lines)
        return total_lines

    def count_files_matching_regex(self, pattern):
        regex = re.compile(pattern)
        matching_files = 0
        for lines in self.file_content.values():
            for line in lines:
                if regex.search(line):
                    matching_files += 1
                    break
        return matching_files

    def get_last_commit_datetime(self):
        command = ['git', '-C', self.root_directory, 'log', '-1', '--format=%ai']
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout.strip()

    def __str__(self):
        return self.root_directory


repo_list = [
    {"name": "cwms-server", "language": ".java"},
    {"name": "efmsim", "language": ".java"},
    {"name": "fia-rts-plugin", "language": ".java"},
    {"name": "hec-client-server", "language": ".java"},
    {"name": "hec-cwms-data-access", "language": ".java"},
    {"name": "hec-cwmsvue", "language": ".java"},
    {"name": "hec-data-exchange", "language": ".java"},
    {"name": "hec-dssvue", "language": ".java"},
    {"name": "hec-ssp", "language": ".java"},
    {"name": "hec-fia", "language": ".java"},
    {"name": "hec-hms", "language": ".java"},
    {"name": "hec-jasper-dss-util", "language": ".java"},
    {"name": "hec-monolith", "language": ".java"},
    {"name": "hec-nucleus", "language": ".java"},
    {"name": "hec-ressim", "language": ".java"},
    {"name": "hec-rts", "language": ".java"},
    {"name": "hec-statistics", "language": ".java"},
    {"name": "hec-wqengine", "language": ".java"},
    {"name": "hec-metvue", "language": ".java"},
    {"name": "flooddamageassessment", "language": ".cs"},
#    {"name": "hecjavadev", "language": ".java"},
    {"name": "hecnf", "language": ".java"},
    {"name": "wat", "language": ".java"}
]

package_names = ["hec.heclib", "hec.heclib.util", "hec.heclib.dss"]
print("repository,language,last updated, file count, lines of code," + ",".join(package_names))
for item in repo_list:
    repo_dir = rf"C:\project\code-study\{item['name']}"
    repo = Repository(repo_dir, item["language"])

    print(f'{repo.name}, '
          f'{item["language"]},',
          f'{repo.get_last_commit_datetime()},',
          f'{len(repo.file_content)},',
          f'{repo.count_total_lines()},',
          end="")
    for package in package_names:
        escaped_package = package.replace(".", "\\.")
        expression = r'^\s*import\s+' + escaped_package
        # print(repo.count_lines_matching_regex(r'^\s*import hec\.heclib\.util\.Heclib'), end="")
        print(f"{repo.count_files_matching_regex(expression)}, ", end="")

    for method in ["Heclib\."]:

    print()
