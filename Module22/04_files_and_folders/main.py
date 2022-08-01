import os

def directory_features(path):
    for i_elem in os.listdir(path):
        current_path = os.path.join(path, i_elem)
        if os.path.isfile(i_elem):
            features_result['file_count'] += 1
            features_result['directory_size'] += os.path.getsize(i_elem) / 1024
        elif os.path.isdir(current_path):
            features_result['subdirectory_count'] += 1
            directory_features(current_path)


path_input = os.path.abspath(os.path.join('..', '..', '..'))
features_result = {'directory_size': 0, 'subdirectory_count': 0, 'file_count': 0}
directory_features(path_input)

print(path_input)
print('Размер каталога (в Кб):', features_result['directory_size'])
print('Количество подкаталогов:', features_result['subdirectory_count'])
print('Количество файлов:', features_result['file_count'])

