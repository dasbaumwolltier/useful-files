#!/usr/bin/env python3

from os import path
import argparse
import shutil
import tempfile

def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""

    # from whichcraft import which
    from shutil import which

    return which(name) is not None

def download_tarfile(url: str, directory: str) -> str:
    import tarfile
    import urllib.request

    filename = path.join(directory, 'sources.tar.gz')

    response = urllib.request.urlretrieve(url, filename=filename)
    tar = tarfile.open(filename)
    tar.extractall(path=directory)
    tar.close()

    return directory

def download_git(url: str, directory: str) -> str:
    from git import Repo

    Repo.clone_from(url, directory)

    return directory

def download(url: str, directory: str) -> str:
    if url.startswith('git://'):
        if not is_tool('git'):
            print('No git is installed! Specify another source or install git')
            exit(1)
        
        return download_git(url, directory)

    elif url.endswith('.tar.gz'):
        return download_tarfile(url, directory)

def benchmark(directory: str):
    


def main():
    parser = argparse.ArgumentParser(description='A program that measures the time it takes a program to build with various thread sizes')
    parser.add_argument('--max-threads', metavar='m', type=int, default=0, help='The max number of threads to check')
    parser.add_argument('--min-threads', metavar='M', type=int, default=1, help='The min number of threads to check')
    parser.add_argument('--source', metavar='s', type=str, default='git://sourceware.org/git/binutils-gdb.git', help='The source which shall be used to test the threads')
    # parser.add_argument('--source', metavar='s', type=str, default='git://sourceware.org/git/binutils-gdb.git', help='The source which shall be used to test the threads')

    args = parser.parse_args()
    dirpath = tempfile.mkdtemp()

    directory = download(args.source, dirpath)
    benchmark(directory)

    shutil.rmtree(dirpath)
    pass

    #directory = download(args.source, dirname)

main()
