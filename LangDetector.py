import re
import keyword
import os
from collections import Counter


def add_keywords(python_kw, cpp_kw, java_kw):
    # keyword.kwlist is a list with python language keywords
    python_kw.extend(keyword.kwlist)
    # list of cpp keywords: http://www.cplusplus.com/doc/oldtutorial/variables/
    cpp_kw.extend(['asm', 'auto', 'bool', 'break', 'case', 'catch', 'char', 'class', 'const', 'const_cast', 'continue',
                   'default', 'delete', 'do', 'double', 'dynamic_cast', 'else', 'enum', 'explicit', 'export', 'extern',
                   'false', 'float', 'for', 'friend', 'goto', 'if', 'inline', 'int', 'long', 'mutable', 'namespace',
                   'new', 'operator', 'private', 'protected', 'public', 'register', 'reinterpret_cast', 'return',
                   'short', 'signed', 'sizeof', 'static', 'static_cast', 'struct', 'switch', 'template', 'this',
                   'throw', 'true', 'try', 'typedef', 'typeid', 'typename', 'union', 'unsigned', 'using', 'virtual',
                   'void', 'volatile', 'wchar_t', 'while'])
    # list of java keywords: https://docs.oracle.com/javase/tutorial/java/nutsandbolts/_keywords.html
    java_kw.extend(['abstract', 'continue', 'for', 'new', 'switch', 'assert', 'default',  'goto', 'package',
                    'synchronized', 'boolean', 'do', 'if', 'private', 'this', 'break', 'double', 'implements',
                    'protected', 'throw', 'byte', 'else', 'import', 'public', 'throws', 'case', 'enum', 'instanceof',
                    'return', 'transient', 'catch', 'extends', 'int', 'short', 'try', 'char', 'final', 'interface',
                    'static', 'void', 'class', 'finally', 'long', 'strictfp', 'volatile', 'const', 'float', 'native',
                    'super', 'while'])


def word_frequency(file):
    # separate words in the given file
    words = re.findall(r'\w+', open(file).read().lower())
    # returns a counter with the number of appearances of each word in the file
    word_counter = Counter(words)
    return word_counter


def guess_language(file):
    python_kw = []
    cpp_kw = []
    java_kw = []
    # fill the lists with each language keywords
    add_keywords(python_kw, cpp_kw, java_kw)
    # get words frequency
    word_counter = word_frequency(file)
    # count appearances of each language keywords in the given file
    kw_counter = {'python': 0, 'cpp': 0, 'java': 0}
    for kw in python_kw:
        kw_counter['python'] += word_counter[kw]
    for kw in cpp_kw:
        kw_counter['cpp'] += word_counter[kw]
    for kw in java_kw:
        kw_counter['java'] += word_counter[kw]
    # print guessed language depending on the number of each language keywords encountered
    language = max(kw_counter, key=kw_counter.get)
    # print('File: ', file, '\tGuessed language: ', language)
    return language


def main():
    # We will test guess_language function with some real cpp, java and python files. They were retrieved from
    # Github trending repositories. To test with another files, put them in the directories called 'cpp', 'java' and
    # 'python'. The output will show a summary of the given files, the prediction success percentage and the files in
    # which it failed.
    cpp_files = os.listdir('cpp/')
    java_files = os.listdir('java/')
    python_files = os.listdir('python/')
    total_files = cpp_files.__len__() + java_files.__len__() + python_files.__len__()
    total_hits = 0

    # Iterate over all the files
    for file in cpp_files:
        if guess_language('cpp/' + file) == 'cpp':
            total_hits = total_hits + 1
        else:
            print('Missed prediction: ', file, '\tLanguage: cpp\tPredicted: ', guess_language('cpp/' + file))
    for file in java_files:
        if guess_language('java/' + file) == 'java':
            total_hits = total_hits + 1
        else:
            print('Missed prediction: ', file, '\tLanguage: java\tPredicted: ', guess_language('java/' + file))
    for file in python_files:
        if guess_language('python/' + file) == 'python':
            total_hits = total_hits + 1
        else:
            print('Missed prediction: ', file, '\tLanguage: python\tPredicted: ', guess_language('python/' + file))

    print('\nTotal files: ', total_files)
    print('Files correctly classified: ', total_hits)
    print('Hit percentage: ', round(total_hits / total_files * 100, 2), '%')


if __name__ == "__main__":
    main()
